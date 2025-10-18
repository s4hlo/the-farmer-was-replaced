def sort():
	size = get_world_size()
	for i in range(1,size):
		move(East)
		j = i
		steps_west = 0
		while j > 0 and measure() < measure(West):
			swap(West)
			move(West)
			steps_west = steps_west + 1
			j = j -1
	
		for i in range(steps_west):
			move(East)
	 
def plant_line():
	for i in range(size):
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Cactus)
		move(East)
	

clear()
set_world_size(5)
size = get_world_size()
for i in range(size):
	plant_line()
	move(North)
	
while get_pos_x() > 0:
		move(West)
print(get_pos_x())  # deve imprimir 0, confirmando que voltamos ao início
sort() 
do_a_flip()

