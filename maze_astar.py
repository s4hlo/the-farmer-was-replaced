clear()

d = [North, East, South, West]
opposite = {
	North: South,
	South: North,
	East: West,
	West: East
}

dir_delta = {
	North: (0, 1),
	South: (0, -1),
	East: (1, 0),
	West: (-1, 0)
}

clear()
set_execution_speed(0)
set_world_size(0)
size = get_world_size()

visited_best_g = {}
goal = None


def generate_maze(s=size):
	if get_entity_type() != Entities.Hedge:
		plant(Entities.Bush)
	substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	if num_items(Items.Weird_Substance) >= substance:
		use_item(Items.Weird_Substance, substance)
	else:
		print("not enough")


def manhattan(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def current_pos():
	return (get_pos_x(), get_pos_y())


def neighbor_pos(pos, direction):
	delta = dir_delta[direction]
	return (pos[0] + delta[0], pos[1] + delta[1])


def sort_neighbors(neighbors):
	# neighbors = [(f, direction, pos), ...]
	# Ordena manualmente pelo menor f
	n = len(neighbors)
	for i in range(n):
		for j in range(i + 1, n):
			if neighbors[j][0] < neighbors[i][0]:
				temp = neighbors[i]
				neighbors[i] = neighbors[j]
				neighbors[j] = temp
	return neighbors


def astar(g, prev_direction):
	pos = current_pos()

	if pos in visited_best_g:
		best = visited_best_g[pos]
	else:
		best = None
	if best != None and g >= best:
		return False
	visited_best_g[pos] = g

	if pos == goal:
		return True

	# Gera vizinhos válidos
	neighbors = []
	for direction in d:
		if prev_direction !=None and direction == opposite[prev_direction]:
			continue
		if can_move(direction):
			npos = neighbor_pos(pos, direction)
			f = (g + 1) + manhattan(npos, goal)
			neighbors.append((f, direction, npos))

	neighbors = sort_neighbors(neighbors)

	for k in range(len(neighbors)):
		direction = neighbors[k][1]
		move(direction)
		if astar(g + 1, direction):
			return True
		move(opposite[direction])

	return False

set_world_size(3)
while True:
	generate_maze()
	goal = measure()
	visited_best_g = {}
	result = astar(0, None)
	while result:
		generate_maze()
		goal = measure()
		visited_best_g = {}
		result = astar(0, None)
	