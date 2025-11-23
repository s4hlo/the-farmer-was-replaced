from utils_drone import *
from utils_move import *
	
def _factory_till_row(args_tuple):
	start_pos = args_tuple
	def _subtask_till_row():
		recompute_ws()
		goto(start_pos)
		for _ in range(ws):
			if get_ground_type() != Grounds.Soil:
				till()
			move(East)
		return True
	return _subtask_till_row
	
def _subtask_harvest_eastwards():
	recompute_ws()
	for _ in range(ws):
		harvest()
		move(East)
	return True

def till_all():
	recompute_parallelism()
	px = get_pos_x()
	args = []
	positions = calculate_p_AA_positions("y")
	for i in range(ws):
		args.append((px, positions[i]))
	return drone_task(_factory_till_row, args)

def harvest_all():
	# Use in case you planted an expensive field of crops.
	recompute_parallelism()
	return drone_naive_AA_task(_subtask_harvest_eastwards, North)

def randcoords():
	recompute_ws()
	return ((random() * ws) // 1, (random() * ws) // 1)

def get_companion_saferand():	
	# Returns a random coordinate if
	# get_companion() fails.
	ret = (get_companion(),)
	if ret[0] == None:
		return None, randcoords()
	else:
		return ret[0][0], ret[0][1]