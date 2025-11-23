#     A solution to **args is to design the subtask to accept a tuple parameter.

def max_drones_safe():
	# Requires having unlocked Auto Unlock.
	if num_unlocked(Unlocks.Megafarm) < 1:
		return 1
	else:
		return max_drones()


# Drone parallelism	
def choose_parallelism(ws):
	# Recompute and decide how the main drone participates in parallel work.
	# 
	# My definition of parallelism assumes the work that needs
	# parallelism needs so under extension on one dimension
	# of the game board.	
	# 
	# Heuristic:
	# - If Megafarm is locked: no parallelism ("none").
	# - Prefer "short" (main drone is a worker) when:
	#     - The field width divides evenly among all drones, or
	# 	  - The total number of drones is small relative to worldsize.
	#     - However this assumes subtasks complete in roughly uniform
	#       time, and that the n_drones*200ticks time overhead nearing
	#       all subtasks' completion is acceptable. It could cause idle 
	#       drones or imbalance if subtask duration is random.
	# - Prefer "long" (main drone only delegates tasks) when:
	# 	  - Removing the main drone yields an even partition, or
	# 	  - The division is cleaner (greater GCD) without the main.	
	#     - There is a job requirement to proactively respawn drones
	#       or subtask length follows a non-uniform distrubution.
	# 	  - But I haven't found a solution to computing the first
	# 		job-completed drone task to efficiently manage drones 
	# 		before they become idle. (TODO)
	# This balances even workload distribution with minimal idle time.

	# Megafarm not unlocked → no parallelism
	if get_cost(Unlocks.Megafarm) == get_cost(Unlocks.Megafarm, 0):
		return "none"

	n = max_drones()
	
	# Safety. If only main drone exists: it must work
	if n <= 1:
		return "short"
	
	# If we have more drones than dimension, either mode will work.
	# "long" somehow seems safer. I can't explain.
	if n > ws:
		return "long"

	# If workforce is small, subtask-ending-overhead shouldn't be large
	if n <= 4:
		return "short"
	
	# Prefer an even partition using all workers (main included)
	if ws % n == 0:
		return "short"

	# If not even, see if excluding the main gives an even split
	if ws % (n - 1) == 0:
		return "long"
	
	# If workforce is small vs width, every hand helps
	if (n - 1) < ws // 4:
		return "short"

	# Fallback: pick the mode that yields fewer ragged strips (GCD-based)
	def _gcd(a, b):
		while b:
			a, b = b, a % b
		return a

	g_all   = _gcd(ws, n)
	g_nomin = _gcd(ws, n - 1)

	# Larger GCD → cleaner tiling. If tie, prefer delegator for less contention.
	if g_all >= g_nomin:
		return "short"
	else:
		return "long"

def recompute_ws():
	global ws
	ws = get_world_size()

def recompute_parallelism(new_type=None):
	# Corner case against runtime upgrades of worldsize or n_drones.
	# Call at the start of big entry points like till_all() or maintask().
	# Args:
	#     new_type: manual application of one of "none", "short", "long"
	recompute_ws()
	global parallelism_type
	if new_type == None:
		parallelism_type = choose_parallelism(ws)
	else:
		parallelism_type = new_type

def drone_task(factory, args, local_p_type=None):
	# This function is for usage with a "N independent jobs" pattern. 
	# Convention:
	#     Ensure subtasks are "closed" w.r.t. starting position. This is 
	#     in case of the "short" mode needing main drone to be a worker.
	#     If not, ensure so externally around your function call.
	# Args:
	#     factory: factory function taking m parameters which 
	#              can cleanly create zero-arg subtasks.
	#     args: list of m-tuple of arguments to pass into factory.
	#     (implied) length: number of jobs. Inferred as n=len(args)
	#     local_p_type: local scope parallelism_type. 
	#                   Useful for second-order delegators.
	# Returns:
	#     results: list of n results
	length = len(args)
	if length == 0: # Trivial
		return []
	if local_p_type != None:
		p_type_to_use = local_p_type
	else:
		# global keyword not needed for readonly
		p_type_to_use = parallelism_type
	
	_drones = []
	for _ in range(length):
		_drones.append(None)
	results = []
	for _ in range(length):
		results.append(None)
	
	if p_type_to_use == "none":
		# Does not account for drone parallelism.
		for i in range(length):
			res = factory(args[i])()
			results[i] = res
		return results
	elif p_type_to_use == "short":
		# Uses the main drone as a worker.
		for i in range(length):
			subtask_watcher = spawn_drone(factory(args[i]))
			if subtask_watcher:
				_drones[i] = subtask_watcher
			else:
				res = factory(args[i])()
				results[i] = res
		for i in range(len(_drones)):
			if _drones[i] != None:
				results[i] = wait_for(_drones[i])
		return results
	elif p_type_to_use == "long":
		# Uses the main drone as a task delegator.
		_drones_idx = []	# Keeps track of index w.r.t. results list.
		counter, limit = 0, length
		while counter < limit:
			if len(_drones) < max_drones():
				subtask_watcher = spawn_drone(factory(args[counter]))
				if subtask_watcher:
					_drones.insert(0, subtask_watcher)
					_drones_idx.insert(0, counter)
					counter += 1
				else:
					# n_drones under capacity but spawn_drone() failed.
					quick_print("Error: unexpected spawn_drone() failure")
					return None
			if len(_drones) >= max_drones():
				# TODO corner case for non-uniform subtask timing
				# Detect the first-job-exited drone instead of 
				# the first-job-started drone
				idx = _drones_idx.pop()
				res = wait_for(_drones.pop())
				results[idx] = res
		while _drones:
			idx = _drones_idx.pop()
			res = wait_for(_drones.pop())
			results[idx] = res
		return results
	else:
		quick_print("Error: Unknown parallelism type:", p_type_to_use)
		return None


# Insert Axis Aligned Drone Task code here because the code section was too long to put into 1 steamguide section



if __name__ != "__main__":
	ws = get_world_size()
	parallelism_type = choose_parallelism(ws)
	quick_print("parallelism_type:", parallelism_type)