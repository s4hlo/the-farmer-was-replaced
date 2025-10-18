change_hat(Hats.Traffic_Cone)
clear()
swap = True
found_dead = False

p_entities = [ Entities.Dead_Pumpkin, Entities.Pumpkin]
size = get_world_size()

highest_petals = 0

def set_grassland():
  if get_ground_type() == Grounds.Soil:
	till()

def set_soil():
  if get_ground_type() == Grounds.Grassland:
	till()
	
def crop():
  if can_harvest():
	harvest()
	
def smart_water():
  while get_water() < 0.75:
	if num_items(Items.Fertilizer) < 1:
	  use_item(Items.Fertilizer)
	use_item(Items.Water)
	if num_items(Items.Water) < 1:
	  break
	
def try_plant_tree():
  if (get_pos_x() + get_pos_y()) % 2 == 0:
	return plant(Entities.Tree)
  return False

def try_plat_sunflower():
  if (get_pos_x() + get_pos_y()) % 6 == 0:
	set_soil()
	return plant(Entities.Sunflower)
  return False


def try_plant_carrot():
  set_soil()
  return plant(Entities.Carrot)
	
def square():
  planting = True
  has_dead = False
  p_entities = [ Entities.Pumpkin, Entities.Dead_Pumpkin]
  while planting:
	for x in range(size):
	  for y in range(size):
		if get_entity_type() not in p_entities:
		  crop()
		if get_pos_x() == 0 and get_pos_y() == 0:
		  do_a_flip()
		  if has_dead == False:
			harvest()
		  has_dead = False
		if get_pos_x() < 6 and get_pos_y() < 6:
		  set_soil()
		  if get_entity_type() == Entities.Dead_Pumpkin:
			has_dead = True
			harvest()
		  plant(Entities.Pumpkin)
		if get_pos_y() > size - 3 :
		  use_item(Items.Fertilizer)
		  harvest()
		else:
		  if not try_plat_sunflower():
			if not try_plant_tree():
			  try_plant_carrot()
		move(East)
	  move(North)
	  
while True: 
  square()      
		