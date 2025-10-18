def sort():
	size = get_world_size()
	for i in range(size):
		j = i
		while j > 0 and measure() < measure(West):
			swap(West)
			move(West)
			j = j -1
		move(East)
clear()
size = get_world_size()

for i in range(size):
	if get_ground_type() == Grounds.Grassland:
		till()
		plant(Entities.Cactus)
  
	move(East)
print(get_pos_x())
sort() 
do_a_flip()
