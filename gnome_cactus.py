def one_d_two_d(pos):
	world_size = get_world_size()
	return pos % world_size, pos // world_size


def two_d_one_d(x, y):
	world_size = get_world_size()
	return x + y * world_size


def move_self(tx, ty):
	ws = get_world_size()
	dx, dy = get_pos_x() - tx, get_pos_y() - ty

	ns = (None, South, North)
	we = (None, West, East)

	def inner_move(delta, move_dir):
		if abs(delta) > ws // 2:
			delta -= (delta / abs(delta)) * ws
		for i in range(0, delta, delta / abs(delta)):
			move(move_dir[delta / abs(delta)])

	inner_move(dx, we)
	inner_move(dy, ns)

	return get_pos_x(), get_pos_y()


def plant_crop(crop):
	if get_ground_type() != Grounds.Soil:
		till()

	if get_entity_type() != crop:
		return plant(crop)

	return False


def plant_cacti(x, y):
	move_self(x, y)

	return plant_crop(Entities.Cactus)


def plant_cacti_field(max_pos):
	for i in range(max_pos):
		x, y = one_d_two_d(i)
		plant_cacti(x, y)


def plant_cacti_field(max_pos):
	board = []
	for i in range(max_pos):
		x, y = one_d_two_d(i)
		if not plant_cacti(x, y):
			return False
		board.append(measure())
	return board


def gnome_basic(max_pos, cacti):
	move_self(0, 0)  # Start at the root node

	pos = 0
	board = cacti

	while pos < max_pos:
		x, y = one_d_two_d(pos)
		move_self(x, y)

		if x == 0 or board[pos] >= board[pos - 1]:
			pos += 1
		else:
			board[pos], board[pos - 1] = board[pos - 1], board[pos]
			swap(West)
			pos -= 1

def advanced_gnome_sort(cacti):
	ws = get_world_size()

	gnome_basic(ws**2, cacti)

	move_self(0, 0)  # Start at the root node

	pos = 0
	board = cacti

	while pos < ws**2:
		x, y = one_d_two_d(pos)
		move_self(x, y)

		if y > 0 and y != ws:
			pos_2 = two_d_one_d(x, y - 1)

			if board[pos_2] > board[pos]:
				swap(South)
				board[pos_2], board[pos] = board[pos], board[pos_2]
				pos = pos_2
				continue

		y += 1
		if y >= ws:
			y = 0
			x += 1
			if x >= ws:
				break
		pos = two_d_one_d(x, y)

def final_gnome_sort(cacti):
	# Reset drone to 0,0
	move_self(0, 0)
	ws = get_world_size()
	cacti_val = cacti

	# Sort all cacti using moddifed gnome sort
	pos = 0
	while pos < ws**2:
		# Swap pos to south
		x, y = one_d_two_d(pos)

		if y > 0 and y != ws:
			pos_2 = two_d_one_d(x, y - 1)
			if cacti_val[pos_2] > cacti_val[pos]:
				move_self(x, y)
				swap(South)
				cacti_val[pos_2], cacti_val[pos] = cacti_val[pos], cacti_val[pos_2]
				pos = pos_2
				continue
		# Swap pos to left
		if x == 0 or cacti_val[pos] >= cacti_val[pos - 1]:
			pos += 1
		else:
			move_self(x, y)
			cacti_val[pos], cacti_val[pos - 1] = cacti_val[pos - 1], cacti_val[pos]
			swap(West)
			pos -= 1

clear()
# ws = get_world_size()
# cacti = plant_cacti_field(ws**2)
# final_gnome_sort(cacti)
# final_gnome_sort(plant_cacti_field(get_world_size()**2))

pre_harvest = num_items(Items.Cactus)

harvest()

quick_print(num_items(Items.Cactus) - pre_harvest)