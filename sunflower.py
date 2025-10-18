import u

petals_pos = {
		7: set(),
		8: set(),
		9: set(),
		10: set(),
		11: set(),
		12: set(),
		13: set(),
		14: set(),
		15: set(),
}
clear()

print(u.get_pos())

alive = 0
def plant_and_save(alive):
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Sunflower)
	u.smart_water()
	petals_pos[measure()].add(u.get_pos())
	alive = alive + 1
	return alive


def tentar_colher(alive, pos):
	for nivel in range(15, 7, -1):
		lista = petals_pos[nivel]
		if not lista: 
			continue
		if pos in lista and can_harvest():
			harvest()
			lista.remove(pos)
			alive -= 1
			alive = plant_and_save(alive)
		break
	return alive


set_execution_speed(0)
set_world_size(3)
size = get_world_size()
while True:
	for i in range(size):
		for j in range(size):
				alive = plant_and_save(alive)
				if alive >= 9:
					pos = u.get_pos()
					alive = tentar_colher(alive, pos)
				move(East)
		move(North)
