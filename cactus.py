def sort(dir, opps):
	change_hat(Hats.Cactus_Hat)
	size = get_world_size()
	for i in range(1,size):
		move(dir)
		j = i
		steps_back = 0
		while j > 0 and measure() < measure(opps):
			swap(opps)
			move(opps)
			steps_back = steps_back + 1
			j = j -1
	
		for k in range(steps_back):
			move(dir)
	change_hat(Hats.Brown_Hat)
	 
def plant_line():
	for i in range(size):
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Cactus)
		move(East)
	

clear()
set_world_size(4)
size = get_world_size()
change_hat(Hats.Brown_Hat)
for i in range(size):
	plant_line()
	while get_pos_x() > 0:
			move(West)
	sort(East, West) 
	move(North)
 
for i in range(size):
	while get_pos_y() > 0:
			move(South)
	while get_pos_x() > i:
			move(West)
	sort(North, South) 
	move(East)
	
harvest()
while True:
	change_hat(Hats.Dinosaur_Hat)
	do_a_flip()



