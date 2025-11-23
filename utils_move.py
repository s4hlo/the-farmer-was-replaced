from utils_num import *
from utils_list import *
from utils_drone import *

def get_pos():
	return (get_pos_x(), get_pos_y())

def _shortest_delta(curr, dest, size):
	d = (dest - curr) % size
	if d > size / 2:
		d -= size
	return d

def goto_x(tx):
	ws = get_world_size()
	cx = get_pos_x()
	dx = _shortest_delta(cx, tx, ws)
	if dx > 0:
		for _ in range(dx):
			move(East)
	elif dx < 0:
		for _ in range(-dx):
			move(West)
	return True

def goto_y(ty):
	ws = get_world_size()
	cy = get_pos_y()
	dy = _shortest_delta(cy, ty, ws)
	if dy > 0:
		for _ in range(dy):
			move(North)
	elif dy < 0:
		for _ in range(-dy):
			move(South)
	return True

def goto(target):
	# The drone makes use of wraparound.
	# Args:
	#     target: Tuple of length 2
	# Returns:
	#     bool: Success state
	tx, ty = target
	goto_x(tx)
	goto_y(ty)
	return True

def u_turn(dir):
	# Given a direction, return the
	# opposite direction
	if dir == North:
		return South
	elif dir == South:
		return North
	elif dir == East:
		return West
	elif dir == West:
		return East
	else:
		return None

def calculate_p_AA_positions(axis):
	# Calculates a list of all positions 
	# across an axis, ordered farthest 
	# distance first, inbetweens 
	# alternating direction, and 
	# closest distance last. 
	# For the use of reaching the 
	# farthest point first when starting
	# an axis aligned drone task.
	# Args:
	#     axis: "x" or "y"
	# Returns:
	#     list[int]
	recompute_ws()
	positions = []
	if axis == "x":
		temp_pos = get_pos_x()
	else:
		temp_pos = get_pos_y()
	farthest = temp_pos - (ws // 2)
	if farthest < 0:
		farthest += ws
	for i in range(1, ws+1):
		if is_odd(i):
			d = i // 2
		else:
			d = - i // 2
		positions.append(ring_clamp(farthest + d, ws))
	return positions