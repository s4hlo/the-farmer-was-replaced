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

set_world_size(14)
while True: 
		for_all(try_plant)
		do_a_flip()
		