change_hat(Hats.Traffic_Cone)
clear()
size = get_world_size()
swap = True
while True:
  for i in range(size):
	for j in range(size/2):
	  if can_harvest():
		harvest()
		if swap:
		  if num_items(Items.Wood) < 400 or num_items(Items.Hay) < 100:
			if get_ground_type() == Grounds.Soil:
			  till()
			move(East)
			if can_harvest():
			  harvest()
			  if get_ground_type() == Grounds.Soil:
				till()
			  plant(Entities.Tree)
		  else:
			if get_ground_type() == Grounds.Grassland:
			  till()
			plant(Entities.Carrot)
			move(East) 
			if can_harvest():
			  harvest()
			  if get_ground_type() == Grounds.Grassland:
				till()
			  plant(Entities.Carrot)
		else: 
		  if num_items(Items.Wood) < 200 or num_items(Items.Hay) < 100:
			if can_harvest():
			  harvest()
			  if get_ground_type() == Grounds.Soil:
				till()
			  plant(Entities.Tree)
			move(East)
			if get_ground_type() == Grounds.Soil:
			  till()
		  else:
			if can_harvest():
			  harvest()
			  if get_ground_type() == Grounds.Grassland:
				till()
			  plant(Entities.Carrot)
			move(East) 
			if get_ground_type() == Grounds.Grassland:
			  till()
			plant(Entities.Carrot)
	  move(East)
	  # if swap:
	  # till()
	  # if can_harvest():
	  #   harvest()
	  # till()
	  # plant(Entities.carrot)
		# swap = not swap
	move(North)
	swap = not swap
	
	