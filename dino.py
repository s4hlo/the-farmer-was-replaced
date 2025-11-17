import u

def auto_dino(cut_on=1000):
	clear()
	change_hat(Hats.Dinosaur_Hat)
	count_apples = 0
	while(True):
		x, y = measure()
		go_to_pos((x,y))
		count_apples += 1
		if count_apples > cut_on:
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)
			count_apples = 0
			
def go_to_pos(xy):
		x_target, y_target = xy
		x, y = u.get_pos()
		fail = False  # inicializa

		def try_moves(order):
				for direction, _, _ in order:
						if move(direction):
								return u.get_pos(), False
				change_hat(Hats.Straw_Hat)
				change_hat(Hats.Dinosaur_Hat)
				return u.get_pos(), True

		while (x, y) != (x_target, y_target):
				if fail:
						break
				if x < x_target:
						(x, y), fail = try_moves([(East, 1, 0), (North, 0, 1), (South, 0, -1), (West, -1, 0)])
				elif x > x_target:
						(x, y), fail = try_moves([(West, -1, 0), (South, 0, -1), (North, 0, 1), (East, 1, 0)])
				elif y < y_target:
						(x, y), fail = try_moves([(North, 0, 1), (East, 1, 0), (West, -1, 0), (South, 0, -1)])
				elif y > y_target:
						(x, y), fail = try_moves([(South, 0, -1), (West, -1, 0), (East, 1, 0), (North, 0, 1)])
# auto_dino()			

def move_b(dir):
	if not move(dir):
		change_hat(Hats.Straw_Hat)
		change_hat(Hats.Dinosaur_Hat)
		move(dir)
	
def circular_path(stop_on=2000000):
	clear()
	change_hat(Hats.Dinosaur_Hat)
	size = get_world_size() 
	swap = True
	while num_items(Items.Bone) < stop_on:
		move_b(East)
		for j in range(size):
			for i in range(size - 2):
				if swap:
					move_b(East)
				else:
					move_b(West)
			if j < size - 1:
				move_b(North)
			swap = not swap
		move_b(West)
		for i in range(size - 1):
			move_b(South)
	clear()
	 
# clear()
# set_world_size(6)
# auto_dino(100)
# circular_path()


