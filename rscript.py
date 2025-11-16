import pumpking_s
def base(a, g, h):
	if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
		harvest() 
		if get_ground_type() != g:
			till()
		if not h:
			plant(a)

def plth(a):
	base(a, Grounds.Soil, False)


def hay():
	base(Entities.Hedge, Grounds.Grassland, True)

def unlk(e, i = 1):
	if (num_unlocked(e) < i):
		unlock(e)




while(True):
	unlk(Unlocks.Speed)
	unlk(Unlocks.Expand, 3)
	unlk(Unlocks.Plant)
	unlk(Unlocks.Carrots)
	unlk(Unlocks.Trees)
	unlk(Unlocks.Pumpkins)
	unlk(Unlocks.Cactus)

	if num_items(Items.Hay) < 100:
		hay()
	elif num_items(Items.Wood) < 500:
		plth(Entities.Bush)
	elif num_items(Items.Carrot) < 200:
		plth(Entities.Carrot)
	elif num_items(Items.Pumpkin) < 5000:
			if num_unlocked(Unlocks.Pumpkins) > 0:
				pumpking_s.get_pumpkins(0.75, 5000)
	else:
		plant(Entities.Cactus)

