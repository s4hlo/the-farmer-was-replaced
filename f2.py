import u 

set_world_size(9)

def plant_c():
	if get_ground_type() != Grounds.Soil:
		till()	
	plant(Entities.Carrot)
def plant_carrot():
	if can_harvest():
		harvest()
		plant_c()
	else:
		plant_c()
while(True):
	u.for_all(plant_carrot)
