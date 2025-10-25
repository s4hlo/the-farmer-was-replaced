import u
change_hat(Hats.Traffic_Cone)
clear()
size = get_world_size()

def try_plant():
	if can_harvest():
		harvest()
	if (get_pos_x() + get_pos_y()) % 2 == 0:
		if get_ground_type() == Grounds.Grassland:
			till()
		u.smart_water()
		return plant(Entities.Tree)
	else: 
		if get_ground_type() == Grounds.Grassland:
			till()
		u.smart_water()
		return plant(Entities.Carrot)

def plant_tree():
	if can_harvest():
		harvest()
		u.smart_water()
		plant(Entities.Tree)

set_world_size(9)
while True: 
		u.for_all(try_plant)
		do_a_flip()
		