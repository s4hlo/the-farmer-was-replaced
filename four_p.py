change_hat(Hats.Traffic_Cone)
clear()

def set_soil():
	if get_ground_type() == Grounds.Grassland:
		till()
	
def remove_if_not_p():
	p_entities = [ Entities.Pumpkin, Entities.Dead_Pumpkin]
	if get_entity_type() not in p_entities:
		if can_harvest():
			harvest()
	
def square():
	planting = True
	size = get_world_size()
	half = size // 2
	harvest_pos = [(0,0), (0,half), (half,0), (half,half)]

	has_dead = {
		harvest_pos[0]: True,
		harvest_pos[1]: True,
		harvest_pos[2]: True,
		harvest_pos[3]: True
	}
	while planting:
		for x in range(size):
			for y in range(size):
				remove_if_not_p()
				if (x,y) in harvest_pos:
					if has_dead[(x,y)] == False:
						harvest()
					has_dead[(x,y)] = False
					
				if x < half and y < half:
					set_soil()
					if get_entity_type() != Entities.Pumpkin:
						has_dead[harvest_pos[0]] = True
					plant(Entities.Pumpkin)
					
				if x >= half and y < half:
					set_soil()
					if get_entity_type() != Entities.Pumpkin:
						has_dead[harvest_pos[1]] = True
					plant(Entities.Pumpkin)
					
				if x < half and y >= half:
					set_soil()
					if get_entity_type() != Entities.Pumpkin:
						has_dead[harvest_pos[2]] = True
					plant(Entities.Pumpkin)
					
				if x >= half and y >= half:
					set_soil()
					if get_entity_type() != Entities.Pumpkin:
						has_dead[harvest_pos[3]] = True
					plant(Entities.Pumpkin)
			 
				move(East)
			move(North)

set_world_size(12)	
while True: 
	square()      
		