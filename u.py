def get_pos():
	return (get_pos_x(), get_pos_y())

def smart_water():
	while get_water() < 0.75:
		use_item(Items.Water)
		if num_items(Items.Water) < 1:
			break