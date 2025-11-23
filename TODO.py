# Optimizes the output of a specifc crop
# exclusively, using polyculture.
# One of the use cases of fertilizer since
# the surrounding crops don't matter.
# All we need is for them to exist to be 
# counted as a companion plant.

# For Weird Substance farming, please enable 
# the relevant flag and farm grass.


from utils_list import *
from utils_drone import *
from utils_grow import *
from utils_farm import *
from utils_move import *
from utils_item import *


ONECROP_TILE_SPACING = 5
# Caution: uses a lot of fertilizer. Always prioritize 
# the "both" strategy over solely "fert".
# With 32 drones, farming trees, the "both" strategy 
# costs approximately 100fert/sec, or 6k/min.
# Keep in mind to stock up before trying for achievements.		
SPEEDUP_STRATEGY = "none" # One of "none", "water", "fert", "both"
WATER_THRESH_ONECROP = 0.5
FLAG_FARM_WEIRD_SUBSTANCE = False
TARGET_CROP = Entities.Carrot	# Don't forget inside 
def stop_condition():			# this function!!!
	# Specify your stopping condition here.
	return num_items(Items.Carrot) > 10000000000



def get_onecrop_indices():
	# Infer if onecrop's pc tiling range (3) in 
	# a direct overlap with another onecrop is 
	# acceptable based on user's selected SPACING.
	
	# This function computes overlap acceptability 
	# in a relaxed manner;
	# (min of PC spacing and selected spacing.)
	recompute_ws()
	overlap_acceptable = ONECROP_TILE_SPACING <= 3
	step = ONECROP_TILE_SPACING
	indices = []
	y = 0
	while y < ws:
		x = 0
		while x < ws:
			indices.append(y * ws + x)
			x += step
		y += step
	if not overlap_acceptable:
		good_indices = []	# Memory in this game is pretty much free
		for i in range(len(indices)):
			temp = indices[i]
			# Consider the 0th col always occupied.
			if not temp % ws > ws - min(3 + 1, ONECROP_TILE_SPACING):
				good_indices.append(temp)
		indices = good_indices
	return indices



def _factory_goto_and_plant(args_tuple):
	companion = args_tuple[0]
	pos = args_tuple[1]

	def _subtask_goto_and_plant():
		goto(pos)
		harvest()	# destroy current plant
		till_for_entity(companion)
		if not plant(companion):
			pass # Don't return False here. 
			# Just keep going and fail silently
		return True
	return _subtask_goto_and_plant


def _factory_onecrop(args_tuple):
	pos = args_tuple[0]
	local_p_type = args_tuple[1]
	def _subtask_onecrop():
		flag_has_used_fert_this_round = False
		goto(pos)
		# This is a temporary measure while I figure out how
		# to delay high-level drones from spawning more drones 
		# while other high level drones are being spawned by
		# the main drone.
		do_a_flip()
		do_a_flip()
		
		till_for_entity(TARGET_CROP)
		plant(TARGET_CROP)
		while not stop_condition():
			if can_harvest():
				if FLAG_FARM_WEIRD_SUBSTANCE:
					use_item(Items.Weird_Substance)
				harvest()
				flag_has_used_fert_this_round = False
				# Use this if any onecrop's pc tiling
				# range (3) overlaps with another onecrop
				# directly, where obstruction can occur if 
				# another onecrop's companion needs to be on
				# the current onecrop's tile.
				if ONECROP_TILE_SPACING <= 3:
					till_for_entity(TARGET_CROP)
	
				plant(TARGET_CROP)
				companion, com_pos = get_companion_saferand()
				args = [(companion, com_pos)]	# length 1
				prev_pos = get_pos()
				drone_task(_factory_goto_and_plant, args, local_p_type)
				goto(prev_pos)
			else:
				# Always water before using fert. Water decreases 
				# growth time multiplicatively while fert is additive.
				if SPEEDUP_STRATEGY in ("both", "water"):
					maintain_water(WATER_THRESH_ONECROP)
				if SPEEDUP_STRATEGY in ("both", "fert"):
					if not flag_has_used_fert_this_round:
						# Fertilizer decreases growth time by 2 seconds.
						actual_timing = calculate_actual_growth_time()
						num_ferts_to_use = actual_timing // 2 + 1
						for _ in range(num_ferts_to_use):
							use_item(Items.Fertilizer)
							flag_has_used_fert_this_round = True
						if flag_has_used_fert_this_round:
							use_item(Items.Weird_Substance)
				if SPEEDUP_STRATEGY in ("none"):
					do_a_flip()	# Conserve energy.
		return True
	return _subtask_onecrop



def main():
	# In this problem there are two locations
	# of parallelization. 1: initial drone 
	# to each onecrop tile, and 2: further
	# delegation to save time during 
	# companion planting 
	clear()
	strategy = None
	tile_1d_indices = get_onecrop_indices()
	temp = len(tile_1d_indices)
	# TODO consider recompute_parallelism 
	# manually since subtasks are not defined
	# w.r.t. worldsize?

	if parallelism_type == "none":
		local_p_type = "none"
	else:
		recompute_parallelism()
		local_p_type = "short"

	args = []
	for i in range(max_drones()):
		args.append((deserialize_2d_index(tile_1d_indices[i], ws), local_p_type))
	drone_task(_factory_onecrop, args)
if __name__ == "__main__":
	main()