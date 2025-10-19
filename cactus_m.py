import u



def sort(dir, size):
	opps = u.opposite(dir)
	change_hat(Hats.Cactus_Hat)
	for i in range(1,size):
		move(dir)
		j = i
		steps_back = 0
		while j > 0 and measure() > measure(opps):
			swap(opps)
			move(opps)
			steps_back = steps_back + 1
			j = j -1
	
		for _ in range(steps_back):
			move(dir)
	change_hat(Hats.Straw_Hat)
	 
def plant_line():
	for i in range(size):
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Cactus)
		if i < size - 1:
			move(East)

def sort_columns():
		n = get_world_size()
		u.go_to_pos((0,0))
		for col in range(n):
	
				# sort 
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
				change_hat(Hats.Straw_Hat)
	
				while get_pos_y() > 0:
						move(South)

				# Avança para a próxima coluna à direita (exceto após a última)
				if col < n - 1:
						move(East)

	
	
def plant_and_sort():
		current_y = get_pos_y()
		size = get_world_size()
		for i in range(size):
				change_hat(Hats.Straw_Hat)
				if get_ground_type() == Grounds.Grassland:
						till()
				plant(Entities.Cactus)


				# sort
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

		change_hat(Hats.Straw_Hat)
		print("cabei aqui fi")

clear()
set_world_size(9)
size = get_world_size()
def plant_the_sort():
	plant_line()
	do_a_flip()
	sort(West, size)
 
for i in range(size):
	spawn_drone(plant_and_sort)
	move(North)
# single_sort(East, West, size)

while True:
		do_a_flip()


# # Garanta que começa no início da linha
# change_hat(Hats.Straw_Hat)
# # Se não estiver no x=0, volta até o início
# while get_pos_x() > 0:
# 		move(West)

# # Planta e ordena simultaneamente da esquerda para a direita
# for o in range(size):
# 	spawn_drone(plant_and_sort_row)
# 	move(North)
# while num_drones() > 1:
#   do_a_flip()
# sort_columns()
# if can_harvest():
# 	harvest()
# u.go_to_pos((0,0))


# u.go_to_pos((3,3))

# # Extra (como no seu código)
# while True:
# 		change_hat(Hats.Dinosaur_Hat)
# 		do_a_flip()



