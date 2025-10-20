import u

def condition(orr, oppsite):
	if orr == 'desc':
		return measure() > measure(oppsite)
	else:
		return measure() < measure(oppsite)

def sort(dir, size, order, do_plant=False):
	opps = u.opposite(dir)
	for i in range(size):
		if do_plant:
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Cactus)

		j = i
		steps_back = 0

		while j > 0 and condition(order, opps):
			swap(opps)    
			move(opps)    
			steps_back += 1
			j -= 1
		for _ in range(steps_back):
			move(dir)

		if i < size - 1:
			move(dir)
   
def plant_sort_north():
	sort(East, size, 'asc', True)
def sort_north():
	sort(North, size, 'asc')
 
def plant_cactus():
	for i in range(size):
		spawn_drone(plant_sort_north)
		move(North)
	while num_drones() > 1:
		pass
	for i in range(size):
		spawn_drone(sort_north)
		move(East)
	
clear()
set_world_size(max_drones() - 1)
size = get_world_size()

while True:
	plant_cactus()
	while num_drones() > 1:
		pass
	harvest()
 


