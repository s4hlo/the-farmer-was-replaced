import u
clear()
size = get_world_size()

def collect_base():
	u.till_to(Grounds.Grassland)
	u.smart_fertilizer()
	if can_harvest():
		change_hat(Hats.Brown_Hat)
		harvest()
		change_hat(Hats.Straw_Hat)
 
def collect_multi():
	while True: 
		def row():
			for _ in range(get_world_size()-1):
				use_item(Items.Fertilizer)
				harvest()
				move(East)
			use_item(Items.Fertilizer)
			harvest()
		for _ in range(get_world_size()):
			if not spawn_drone(row):
				row()
			move(North) 
	
# # collect_multi()


# set_world_size(31)
# u.all_rows(collect_base)

	