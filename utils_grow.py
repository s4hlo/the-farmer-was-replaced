from utils_item import *
from utils_num import *

# Used for logic in polyculture
entity_growth_timing = {	# Entity: tuple[float, float], in seconds
	Entities.Apple: (0.2, 0.2),
	Entities.Bush: (3.2, 4.8),
	Entities.Cactus: (1.0, 1.0),
	Entities.Carrot: (4.8, 7.2),
	Entities.Dead_Pumpkin: (0, 0),	# JIC
	Entities.Dinosaur: (0.18, 0.22),
	Entities.Grass: (0.5, 0.5),
	Entities.Hedge: (0, 0),	# JIC
	Entities.Pumpkin: (0.2, 3.8),
	Entities.Sunflower: (5.6, 8.4),
	Entities.Treasure: (0, 0),	# JIC
	Entities.Tree: (5.6, 8.4),
}

entity_allowed_groundtype = {	# Entity: tuple containing allowed ground types
	Entities.Apple: (Grounds.Grassland, Grounds.Soil),
	Entities.Bush: (Grounds.Grassland, Grounds.Soil),
	Entities.Cactus: (Grounds.Soil),
	Entities.Carrot: (Grounds.Soil),
	Entities.Dead_Pumpkin: (Grounds.Soil),	# assign as if pumpkin
	Entities.Dinosaur: (Grounds.Grassland, Grounds.Soil),
	Entities.Grass: (Grounds.Grassland, Grounds.Soil),
	Entities.Hedge: (),	# JIC.
	Entities.Pumpkin: (Grounds.Soil),
	Entities.Sunflower: (Grounds.Soil),
	Entities.Treasure: (),	# JIC.
	Entities.Tree: (Grounds.Grassland, Grounds.Soil),
}

entity_needs_soil = {
	# Exclusively needs soil.
	Entities.Cactus,	
	Entities.Carrot,
	Entities.Pumpkin,
	Entities.Sunflower,
}

entity_needs_grassland = set()	# Exclusively needs grassland.

def calculate_actual_growth_time():
	# Account for water level: linear interpolation
	# which is z = val * (left*(1-y) + right*(y))
	ent = get_entity_type()
	if ent == None or ent not in entity_growth_timing:
		return 0
	return entity_growth_timing[ent][0] * (1 / (1 + 4 * get_water()))

def maintain_water(thresh):
	# Args:
	#     thresh: float threshold to maintain above
	# Returns:
	#     bool: Success state	
	if not check_has_item(Items.Water):
		return False
	thresh = clamp(thresh, 0, 1)
	while get_water() < thresh:
		use_item(Items.Water)
	return True

def till_for_entity(ent):
	# Prepare the ground for planting.
	# Simpler version but less safe:
	# if get_ground_type() not in entity_allowed_groundtype[ent]:
	#     till()
	# 
	ground = get_ground_type()
	if ent in entity_needs_soil and ground != Grounds.Soil:
		till()
	elif ent in entity_needs_grassland and ground != Grounds.Grassland:
		till()
	return True