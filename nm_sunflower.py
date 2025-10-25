clear()
change_hat(Hats.Brown_Hat)

hats = [Hats.Green_Hat, Hats.Purple_Hat]
world_size = get_world_size()

max_petals = 15
min_petals = 7 

def replant_systematically():
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	if get_water() < 0.5:
		use_item(Items.Water)
		
def create_worker_task(target_petal, is_replant_phase):
	
	def encapsulated_worker_task():
		if get_pos_x() < world_size - 1:
			change_hat(hats[get_pos_x() % 2])
		
		for j in range(world_size):
			if measure() == target_petal:			
				while not can_harvest():
					use_item(Items.Fertilizer)			
				harvest() 
			
			if is_replant_phase:
				if get_entity_type() != Entities.Sunflower:
					replant_systematically()
			
			move(North)
		
		return

	return encapsulated_worker_task

def drone_task_initial_setup():
	for j in range(world_size):
		if can_harvest():
			harvest()
		replant_systematically()
		move(North)
	return 

def drone_task_manager():
	global world_size
	
	change_hat(Hats.Brown_Hat)
	
	first_run = True
	
	while True:
		
		if first_run:
			for i in range(world_size - 1):
				spawn_drone(drone_task_initial_setup) 
				move(East) 
			drone_task_initial_setup() 
			move(East)
			
			first_run = False
		
		for petal_count in range(max_petals, min_petals, -1):
			
			worker_task = create_worker_task(petal_count, False) 

			for i in range(world_size - 1):
				spawn_drone(worker_task) 
				move(East) 
			worker_task() 
			move(East)
		worker_task_replant_total = create_worker_task(min_petals, True)
		
		for i in range(world_size - 1):
			spawn_drone(worker_task_replant_total)
			move(East)
		
		worker_task_replant_total()
		
		move(East)

def run_sunflower():
	drone_task_manager()
	
while True:
	run_sunflower()