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
  harvest_pos = [(0,0), (0,6), (6,0), (6,6)]

  has_dead = {
	  harvest_pos[0]: False,
	  harvest_pos[1]: False,
	  harvest_pos[2]: False,
	  harvest_pos[3]: False
  }
  p_entities = [ Entities.Pumpkin, Entities.Dead_Pumpkin]
  
  while planting:
	for x in range(size):
	  for y in range(size):
		# plant pumpkin
		if get_entity_type() not in p_entities:
		  crop()
		if (x,y) in harvest_pos:
		  do_a_flip()
		  if has_dead[(x,y)] == False:
			harvest()
		  has_dead[(x,y)] = False
		  
		if x < 6 and y < 6:
		# if (x,y) < 
		  set_soil()
		  if get_entity_type() == Entities.Dead_Pumpkin:
			has_dead[harvest_pos[0]] = True
			harvest()
		  plant(Entities.Pumpkin)
		  
		if x >= 6 and y < 6:
		  set_soil()
		  if get_entity_type() == Entities.Dead_Pumpkin:
			has_dead[harvest_pos[1]] = True
			harvest()
		  plant(Entities.Pumpkin)
		  
		if x < 6 and y >= 6:
		  set_soil()
		  if get_entity_type() == Entities.Dead_Pumpkin:
			has_dead[harvest_pos[2]] = True
			harvest()
		  plant(Entities.Pumpkin)
		  
		if x >= 6 and y >= 6:
		  set_soil()
		  if get_entity_type() == Entities.Dead_Pumpkin:
			has_dead[harvest_pos[3]] = True
			harvest()
		  plant(Entities.Pumpkin)
		 
		  
		  
		move(East)
	  move(North)
	  
while True: 
  square()      
		