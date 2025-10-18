clear()
size = get_world_size()
while True:
	for i in range(size):
		for j in range(size):
			use_item(Items.Fertilizer)
			harvest()
			move(East)
		move(North)
	