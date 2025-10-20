import u

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
	 
def pumpkim(size):
	for i in range(size):
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Pumpkin)
		if i < size - 1:
			move(East)
	
	
	
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

def pumpkim_size():
	change_hat(Hats.Gold_Hat)
	pumpkim(get_world_size())
 
 
set_world_size(0)	
size = get_world_size()

# while True: 
# 	for i in range(size):
# 		print(measure())
# 		spawn_drone(pumpkim_size)      
# 		move(North)
		
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North) 
	
def plant_until_ok():
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Pumpkin)
		u.smart_water()
		while not can_harvest():
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
	
while True:	
	for_all(plant_until_ok)
	while num_drones() > 1:
		pass
	harvest()