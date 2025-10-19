def sort(dir, opps):
	change_hat(Hats.Cactus_Hat)
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
	change_hat(Hats.Brown_Hat)
	 
def plant_line():
	for i in range(size):
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Cactus)
		move(East)
def go_to_southwest():
	# Vai para y=0 (Sul) e x=0 (Oeste)
	while get_pos_y() > 0:
			move(South)
	while get_pos_x() > 0:
			move(West)
	# do_a_flip()
def sort_columns():
		n = get_world_size()
		go_to_southwest()

		for col in range(n):
				change_hat(Hats.Cactus_Hat)

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

		change_hat(Hats.Brown_Hat)
	
	
def plant_and_sort_row(current_y):
		size = get_world_size()
		for i in range(size):
				change_hat(Hats.Brown_Hat)
				if get_ground_type() == Grounds.Grassland:
						till()
				plant(Entities.Cactus)


				# order horizontal
				change_hat(Hats.Cactus_Hat)
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

		change_hat(Hats.Brown_Hat)

clear()
set_world_size(9)
size = get_world_size()

# Garanta que começa no início da linha
change_hat(Hats.Brown_Hat)
# Se não estiver no x=0, volta até o início
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
	go_to_southwest()

while True:
		change_hat(Hats.Dinosaur_Hat)
		do_a_flip()


