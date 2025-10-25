import u
clear()
change_hat(Hats.Dinosaur_Hat)

size = get_world_size()
def auto_dino(cut_on=1000):
	count_apples = 0
	while(True):
		x, y = measure()
		u.go_to_pos((x,y))
		count_apples += 1
		if count_apples > cut_on:
			change_hat(Hats.Straw_Hat)
			change_hat(Hats.Dinosaur_Hat)
			
auto_dino()			
# swap = True
# for j in range(size):
# 	for i in range(size):
# 		if swap:
# 			move(East)
# 		else:
# 			move(West)
# 	move(North)
# 	swap = not swap