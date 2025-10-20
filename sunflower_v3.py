import u

clear()
set_execution_speed(0)
set_world_size(11)
size = get_world_size()


def plant_sun():
	plant(Entities.Sunflower)
	u.smart_water()
	use_item(Items.Fertilizer)
	use_item(Items.Weird_Substance)

for i in range(size - 1):
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	while measure() > 7:
		if get_ground_type() != Grounds.Soil:
			till()
		harvest()
		plant_sun()
		# u.smart_water()
		# plant(Entities.Sunflower)
	move(East)
 
if get_ground_type() != Grounds.Soil:
	till()
plant_sun()
while True:
	if can_harvest():
		harvest()
		plant_sun()
		
