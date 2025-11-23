clear()

PLANT_TYPE_TO_UNLOCK_MAPPING = {
	Entities.Bush: Unlocks.Plant,
	Entities.Tree: Unlocks.Trees,
	Entities.Carrot: Unlocks.Carrots,
	Entities.Pumpkin: Unlocks.Pumpkins,
	Entities.Cactus: Unlocks.Cactus,
	Entities.Sunflower: Unlocks.Sunflowers,
}

DRONE_POSITIONS_32X32 = [
	(0, 0), (8, 0), (16, 0), (24, 0),
	(4, 4), (12, 4), (20, 4), (28, 4),
	(0, 8), (8, 8), (16, 8), (24, 8),
	(4, 12), (12, 12), (20, 12), (28, 12),
	(0, 16), (8, 16), (16, 16), (24, 16),
	(4, 20), (12, 20), (20, 20), (28, 20),
	(0, 24), (8, 24), (16, 24), (24, 24),
	(4, 28), (12, 28), (20, 28), (28, 28),
]

RESOURCE_CONFIG = {
	Items.Hay: {
		"plant_type": Entities.Grass,
		"fertilizer": True,
		"weird_substance": False,
		"water": True,
		"needs_preparation": False,
		"select_plant_function": None,
	},
	Items.Wood: {
		"plant_type": None,
		"fertilizer": True,
		"weird_substance": True,
		"water": True,
		"needs_preparation": False,
		"select_plant_function": "select_wood_plant",
	},
	Items.Carrot: {
		"plant_type": Entities.Carrot,
		"fertilizer": True,
		"weird_substance": True,
		"water": True,
		"needs_preparation": True,
		"select_plant_function": None,
	},
}


def navigate_to_position(target_x, target_y):
	world_size = get_world_size()
	current_position_x = get_pos_x()
	current_position_y = get_pos_y()

	horizontal_distance = (target_x - current_position_x) % world_size
	vertical_distance = (target_y - current_position_y) % world_size

	if horizontal_distance < world_size // 2:
		for _ in range(horizontal_distance):
			move(East)
	else:
		for _ in range(world_size - horizontal_distance):
			move(West)

	if vertical_distance < world_size // 2:
		for _ in range(vertical_distance):
			move(North)
	else:
		for _ in range(world_size - vertical_distance):
			move(South)


def apply_fertilizer_and_water(use_fertilizer, use_weird_substance, use_water):
	if can_harvest():
		return

	if use_fertilizer and num_unlocked(Unlocks.Fertilizer) != 0 and num_items(Items.Fertilizer) >= 1:
		use_item(Items.Fertilizer)
		if use_weird_substance and num_items(Items.Weird_Substance) >= 1:
			use_item(Items.Weird_Substance)

	if use_water and num_unlocked(Unlocks.Watering) != 0 and get_water() < 1 and num_items(Items.Water) >= 1:
		use_item(Items.Water)


def prepare_soil_and_plant(plant_type):
	current_entity_type = get_entity_type()
	current_ground_type = get_ground_type()

	if plant_type != current_entity_type:
		harvest()

	if plant_type == Entities.Grass:
		if current_ground_type != Grounds.Grassland:
			till()
	else:
		if current_ground_type != Grounds.Soil:
			till()
		if plant_type in PLANT_TYPE_TO_UNLOCK_MAPPING:
			required_unlock = PLANT_TYPE_TO_UNLOCK_MAPPING[plant_type]
			if num_unlocked(required_unlock) != 0:
				plant(plant_type)


def select_wood_plant():
	if num_unlocked(Unlocks.Trees) != 0:
		return Entities.Tree
	elif num_unlocked(Unlocks.Plant) != 0:
		return Entities.Bush
	return None


def collect_hay_solo(target_quantity):
	while num_items(Items.Hay) < target_quantity:
		prepare_soil_and_plant(Entities.Grass)
		while not can_harvest():
			apply_fertilizer_and_water(False, False, True)
		harvest()


def collect_wood_solo(target_quantity):
	while num_items(Items.Wood) < target_quantity:
		wood_plant = select_wood_plant()
		if wood_plant == None:
			return
		prepare_soil_and_plant(wood_plant)
		while not can_harvest():
			apply_fertilizer_and_water(True, True, True)
		harvest()


def collect_carrot_solo(target_quantity):
	carrot_cost = get_cost(Entities.Carrot)
	while num_items(Items.Carrot) < target_quantity:
		if num_items(Items.Hay) < carrot_cost[Items.Hay]:
			collect_hay_solo(carrot_cost[Items.Hay])
		if num_items(Items.Wood) < carrot_cost[Items.Wood]:
			collect_wood_solo(carrot_cost[Items.Wood])
		prepare_soil_and_plant(Entities.Carrot)
		while not can_harvest():
			apply_fertilizer_and_water(True, True, True)
		harvest()


def fulfill_companion_plant_requirements(companion_plant_type, carrot_cost):
	if companion_plant_type == Entities.Carrot:
		if num_items(Items.Hay) < carrot_cost[Items.Hay]:
			collect_hay_solo(carrot_cost[Items.Hay])
		if num_items(Items.Wood) < carrot_cost[Items.Wood]:
			collect_wood_solo(carrot_cost[Items.Wood])


def get_plant_type_for_resource(resource_item, config):
	if config["select_plant_function"] == "select_wood_plant":
		return select_wood_plant()
	return config["plant_type"]


def collect_resource_with_drones(resource_item, target_quantity):
	if resource_item not in RESOURCE_CONFIG:
		return

	config = RESOURCE_CONFIG[resource_item]
	carrot_cost = get_cost(Entities.Carrot)

	def drone_worker():
		current_drone_id = num_drones()

		if current_drone_id < 32:
			spawn_drone(drone_worker)
		drone_position = DRONE_POSITIONS_32X32[current_drone_id - 1]
		navigate_to_position(drone_position[0], drone_position[1])

		while num_items(resource_item) < target_quantity:
			plant_type = get_plant_type_for_resource(resource_item, config)
			if plant_type == None:
				return
			prepare_soil_and_plant(plant_type)
			companion_plant_type, (companion_x, companion_y) = get_companion()

			if (companion_x, companion_y) not in plant_position_map:
				plant_position_map[(companion_x, companion_y)] = None

			if plant_position_map[(companion_x, companion_y)] != companion_plant_type:
				navigate_to_position(companion_x, companion_y)
				fulfill_companion_plant_requirements(companion_plant_type, carrot_cost)
				prepare_soil_and_plant(companion_plant_type)
				plant_position_map[(companion_x, companion_y)] = companion_plant_type
				navigate_to_position(drone_position[0], drone_position[1])

			while not can_harvest():
				apply_fertilizer_and_water(
					config["fertilizer"],
					config["weird_substance"],
					config["water"]
				)
			harvest()

	if num_items(resource_item) < target_quantity:
		if config["needs_preparation"]:
			if num_items(Items.Hay) < carrot_cost[Items.Hay]:
				collect_hay_solo(carrot_cost[Items.Hay])
			if num_items(Items.Wood) < carrot_cost[Items.Wood]:
				collect_wood_solo(carrot_cost[Items.Wood])

		initial_world_size = get_world_size()
		plant_position_map = {}
		navigate_to_position(0, 0)

		if num_unlocked(Unlocks.Expand) == 9 and max_drones() == 32:
			temporary_world_size = 32
		else:
			return
		set_world_size(temporary_world_size)

		drone_worker()
		while num_drones() != 1:
			pass

		set_world_size(initial_world_size)


collect_resource_with_drones(Items.Wood, 1000000000000)