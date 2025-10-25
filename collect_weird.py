import
clear()
size = get_world_size()

def collect_base():
	while True:
		for i in range(size):
			for j in range(size):
				use_item(Items.Fertilizer)
				harvest()
				move(East)
			move(North)
  
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
  
# collect_multi()



u.all_rows(harvest)

	