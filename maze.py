clear()

d = [North, East, South, West]
opposite = {
	North: South,
	South: North,
	East: West,
	West: East
}

clear()
set_execution_speed(0)
set_world_size(0)
size = get_world_size()

visited = set()
goal = None


def generate_maze(s=size):
	if get_entity_type() != Entities.Hedge:
		plant(Entities.Bush)
	substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	if num_items(Items.Weird_Substance) >= substance:
		use_item(Items.Weird_Substance, substance)
	else:
		print("not enough")


def dfs(prev_direction=None):
	pos = (get_pos_x(), get_pos_y())

	if pos in visited:
		return False

	visited.add(pos)

	if pos == goal:
		generate_maze()
		return True

	for direction in d:
		if prev_direction != None and direction == opposite[prev_direction]:
			continue
		if can_move(direction):
			move(direction)
			if dfs(direction):
				return True  # Propaga o sucesso
			move(opposite[direction])

	return False

set_world_size(3)
while True:
	generate_maze()
	goal = measure()
	visited = set()
	dfs()


