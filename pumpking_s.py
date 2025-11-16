import u

def smart_harvest(fertilize):  # Waits for plant to grow before harvesting. Fertilising can be enabled.
		if get_entity_type() != None:
				while fertilize and not can_harvest():
						use_item(Items.Fertilizer)
				harvest()

def smart_till(req_ground):  # Switch ground type
		if get_ground_type() != req_ground:
				till()
				
def move_self(tx, ty):
		ws = get_world_size()
		dx, dy = get_pos_x() - tx, get_pos_y() - ty

		ns = (None, South, North)
		we = (None, West, East)

		def inner_move(delta, move_dir):
				if abs(delta) > ws // 2:
						delta -= (delta / abs(delta)) * ws
				if delta == 0:
						return
				for i in range(0, delta, delta / abs(delta)):
						move(move_dir[delta / abs(delta)])
		
		inner_move(dx, we)
		inner_move(dy, ns)

		return get_pos_x(), get_pos_y()

def pos_to_xy(pos):
		world_size = get_world_size()
		return pos % world_size, pos // world_size
		
def xy_to_pos(x, y):
		world_size = get_world_size()
		return x + y * world_size
		
def generate_blank_pumpkin_patch():
		world_size = get_world_size()
		blank_pumpkins = []
		for i in range(0, world_size ** 2):
				blank_pumpkins.append(False)
		return blank_pumpkins
		
def check_pumpkin():
		return can_harvest() and get_entity_type() == Entities.Pumpkin
		
def check_pumpkin_patch(patch): # Use is to restart pumpkin patch w/o replanting whole field
		pumpkins = patch
		for i_ in range(get_world_size() ** 2):
				if True != pumpkins[i_]:
						x, y = pos_to_xy(i_)
						move_self(x, y)
						pumpkins[i_] = check_pumpkin()
		return pumpkins
		
def can_harvest_pumpkin_patch(patch):
		return patch[0] == True and len(set(patch)) == 1
		
def maintain_pumpkin_patch(req_water_level=0.75, req_fertilize=False):
		pumpkin_patch = check_pumpkin_patch(generate_blank_pumpkin_patch())
		pos = get_pos_x() + get_pos_y() * get_world_size()
		dir = 1
		while not can_harvest_pumpkin_patch(pumpkin_patch):
						
				if get_entity_type() != Entities.Pumpkin:
						smart_till(Grounds.Soil)
						if num_unlocked(Unlocks.Plant) > 0:
							plant(Entities.Pumpkin)
				elif not can_harvest():
						u.smart_water(req_water_level)
						
				pumpkin_patch[pos] = check_pumpkin()
				
				pos += dir
				if pos >= get_world_size() ** 2 or pos < 0:
						dir *= -1
						pos += dir
				if pumpkin_patch[pos] == True:
						continue
				x, y = pos_to_xy(pos)
				move_self(x, y)

def get_pumpkins(req_water_level=0.75, req_fertilize=False):
		maintain_pumpkin_patch(req_water_level, req_fertilize)
		harvest()  # harvest megapumpkin

# clear()

# set_world_size(4)
# while num_items(Items.Pumpkin) < 100000 or True:
# 		get_pumpkins(0.75)