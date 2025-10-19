def get_pos():
	return (get_pos_x(), get_pos_y())

def smart_water():
	while get_water() < 0.75:
		use_item(Items.Water)
		if num_items(Items.Water) < 1:
			break
 
def go_to_pos(xy):
	x_target, y_target = xy
	x = get_pos_x()
	y = get_pos_y()
	while x < x_target:
		move(East)
		x += 1
	while x > x_target:
		move(West)
		x -= 1
	while y < y_target:
		move(North)
		y += 1
	while y > y_target:
		move(South)
		y -= 1
  
def opposite(dir): 
	opposite   = {North: South, South: North, East: West, West: East}
	return opposite[dir]	