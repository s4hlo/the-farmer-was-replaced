import u

petals_pos = {
		7: [],
		8: [],
		9: [],
		10: [],
		11: [],
		12: [],
		13: [],
		14: [],
		15: [],
}
clear()

alive = 0
def plant_and_save(alive):
	if get_ground_type() == Grounds.Grassland:
		till()
	if plant(Entities.Sunflower):
		u.smart_water()
		petals_pos[measure()].append(u.get_pos())
		alive = alive + 1
	return alive

def harvest_alive(alive, pos):
	value = measure()
	lista = petals_pos[value]
	lista.remove(pos)
	harvest()
	alive -= 1
	return alive

def tentar_colher(alive, pos):
	# TODO improve this
	# sete = petals_pos[7]
	# if len(sete) > 2 and can_harvest():
	# 	harvest_alive(alive, pos)
	
	
	for nivel in range(15, 7, -1):
		lista = petals_pos[nivel]
		if not lista: 
			continue
		if pos in lista and can_harvest():
			alive = harvest_alive(alive, pos)
			alive = plant_and_save(alive)
		break
	return alive


set_execution_speed(0)
set_world_size(11)
size = get_world_size()
while True:
	if len(petals_pos[7]) == size:
		while True:
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
			if can_harvest():
				harvest()
				plant(Entities.Sunflower)
	for i in range(size):
			alive = plant_and_save(alive)
			if alive >= 10:
				pos = u.get_pos()
				alive = tentar_colher(alive, pos)
			move(East)

