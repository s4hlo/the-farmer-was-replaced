import u

def plant_sun(better=True):
	if num_unlocked(Unlocks.Sunflowers) > 0:
		plant(Entities.Sunflower)
		if (better):
			u.smart_water()
			u.smart_fertilizer()
			use_item(Items.Weird_Substance)
 

 
def power(limit=1000000000):
	if num_unlocked(Unlocks.Sunflowers) > 0:
		clear()
		size = get_world_size()

		for i in range(10):
			if num_items(Items.Carrot) < 1:
				clear()
				return False
			if get_ground_type() != Grounds.Soil:
				till()
			plant_sun(False)
			while measure() > 7 and num_items(Items.Power) < limit:
				if num_items(Items.Carrot) < 1:
					clear()
					return False
				if get_ground_type() != Grounds.Soil:
					till()
				harvest()
				u.smart_water()
				plant_sun(False)
			move(East)
		 
		if get_ground_type() != Grounds.Soil:
			till()
		plant_sun()
		while num_items(Items.Power) < limit:
			if num_items(Items.Carrot) < 1:
				clear()
				return False
			if can_harvest():
				harvest()
				plant_sun()
	clear()
			
power()