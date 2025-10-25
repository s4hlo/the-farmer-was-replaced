def get_pos():
	return (get_pos_x(), get_pos_y())

def smart_water():
	while get_water() < 0.75:
		use_item(Items.Water)
		if num_items(Items.Water) < 1:
			break
 
def go_to_pos(xy):
	x_target, y_target = xy
	x, y = get_pos()

	def try_moves(order):
		while True:
			for direction, _, _ in order:
				if move(direction):
					return get_pos()
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)

	while (x, y) != (x_target, y_target):
		if x < x_target:
			x, y = try_moves([(East, 1, 0), (North, 0, 1), (South, 0, -1), (West, -1, 0)])
		elif x > x_target:
			x, y = try_moves([(West, -1, 0), (South, 0, -1), (North, 0, 1), (East, 1, 0)])
		elif y < y_target:
			x, y = try_moves([(North, 0, 1), (East, 1, 0), (West, -1, 0), (South, 0, -1)])
		elif y > y_target:
			x, y = try_moves([(South, 0, -1), (West, -1, 0), (East, 1, 0), (North, 0, 1)])
	print("chegeui") 

	
def opposite(dir): 
	opposite   = {North: South, South: North, East: West, West: East}
	return opposite[dir]	

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