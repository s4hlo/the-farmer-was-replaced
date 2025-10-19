import u

def condition(orr, opps):
	if orr == 'desc':
		return measure() > measure(opps)
	else:
		return measure() < measure(opps)

def sort(dir, size, order='desc'):
	opps = u.opposite(dir)
	for i in range(1,size):
		move(dir)
		j = i
		steps_back = 0
 
		while j > 0 and condition(order, opps):
			swap(opps)
			move(opps)
			steps_back = steps_back + 1
			j = j -1
	
		for _ in range(steps_back):
			move(dir)
	 
def plant_and_sort(dir, size, order='desc'):
	opps = u.opposite(dir)
	for i in range(size):
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

clear()
set_world_size(15)
size = get_world_size()


 
def plant_sort_north():
	plant_and_sort(East, size, 'asc')
 
for i in range(size):
	spawn_drone(plant_sort_north)
	move(North)

def sort_north():
	sort(North, size, 'asc')
	
while num_drones() > 1:
	pass
for i in range(size):
	spawn_drone(sort_north)
	move(East)


while True:
		do_a_flip()


