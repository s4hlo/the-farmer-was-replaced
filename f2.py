clear()

d = [North, East, South, West]
opposite = {
	North: South,
	South: North,
	East: West,
	West: East
}

# Direction -> (dx, dy). Adjust if your coordinate system differs.
dir_delta = {
	North: (0, 1),
	South: (0, -1),
	East: (1, 0),
	West: (-1, 0),
}

clear()
set_execution_speed(0)
set_world_size(0)
size = get_world_size()

visited_best_g = {}  # dict[(x, y)] = best g so far
goal = None


def generate_maze(s=size):
	plant(Entities.Bush)
	substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)


def manhattan(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def current_pos():
	return (get_pos_x(), get_pos_y())


def neighbor_pos(pos, direction):
	dx, dy = dir_delta[direction]
	return (pos[0] + dx, pos[1] + dy)


def astar(g=0, prev_direction=None):
	pos = current_pos()

	# Prune if we have already reached this cell cheaper
	best = visited_best_g.get(pos)
	if best is not None and g >= best:
		return False
	visited_best_g[pos] = g

	if pos == goal:
		harvest()
		return True

	# Generate feasible neighbors from here
	neighbors = []
	for direction in d:
		if prev_direction is not None and direction == opposite[prev_direction]:
			# Optional: skip direct backtracking to reduce thrashing
			continue
		if can_move(direction):
			npos = neighbor_pos(pos, direction)
			f = (g + 1) + manhattan(npos, goal)
			neighbors.append((f, direction, npos))

	# Explore in increasing f-order
	neighbors.sort(key=lambda t: t[0])

	for _, direction, _ in neighbors:
		move(direction)
		if astar(g + 1, direction):
			return True
		# backtrack
		move(opposite[direction])

	return False


while True:
	generate_maze()
	goal = measure()  # expected to return (gx, gy)
	visited_best_g = {}
	astar(g=0, prev_direction=None)
	do_a_flip()
