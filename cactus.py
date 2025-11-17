import u
def sort(dir, opps):
	size = get_world_size()
	for i in range(1,size):
		move(dir)
		j = i
		steps_back = 0
		while j > 0 and measure() < measure(opps):
			swap(opps)
			move(opps)
			steps_back = steps_back + 1
			j = j -1
	
		for k in range(steps_back):
			move(dir)
	 
def plant_line():
	for i in range(size):
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Cactus)
		move(East)
  
def sort_columns():
		n = get_world_size()
		u.go_to_pos((0,0))

		for col in range(n):

				for y in range(1, n):
						move(North)
						steps_down = 0

						while steps_down < y and measure() < measure(South):
								swap(South)
								move(South)
								steps_down += 1

						for _ in range(steps_down):
								move(North)

				# Coluna finalizada: volta ao chão
				while get_pos_y() > 0:
						move(South)

				# Avança para a próxima coluna à direita (exceto após a última)
				if col < n - 1:
						move(East)

	
	
def plant_and_sort_row(current_y):
		size = get_world_size()
		for i in range(size):
				if get_ground_type() == Grounds.Grassland:
						till()
				plant(Entities.Cactus)


				# order horizontal
				j = i
				steps_back = 0
				while j > 0 and measure() < measure(West):
						swap(West)     # troca com o vizinho anterior
						move(West)     # anda 1 para trás junto com o item
						steps_back += 1
						j -= 1

				# Volta para a posição original (à frente), para seguir ao próximo i
				for _ in range(steps_back):
						move(East)

				# Avança para a próxima célula, exceto após a última
				if i < size - 1:
						move(East)



def cactus_plant():
	harvest()
	u.go_to_pos((0,0))
	
	size = get_world_size()
	while get_pos_x() > 0:
			move(West)

	while True:
		for o in range(size):
			plant_and_sort_row(get_pos_y())
			move(East)
			move(North)
		sort_columns()
		if can_harvest():
			harvest()
			u.go_to_pos((0,0))
			break
		u.go_to_pos((0,0))
 
	
