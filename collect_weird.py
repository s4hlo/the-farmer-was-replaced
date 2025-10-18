clear()
size = get_world_size()
while True:
  for i in range(size):
	for j in range(size):
	  while not can_harvest():
		do_a_flip()
	  if can_harvest():
		use_item(Items.Weird_Substance)
		harvest()
	  move(East)
	move(North)
	