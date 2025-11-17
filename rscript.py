import pumpking_s
import cactus
import u
def base(a, g, h):
	if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
		harvest() 
		if get_ground_type() != g:
			till()
		if not h:
			u.smart_water()
			plant(a)

def plth(a):
	base(a, Grounds.Soil, False)


def hay():
	base(Entities.Hedge, Grounds.Grassland, True)

def unlk(e, i = 1):
	if (num_unlocked(e) < i):
		unlock(e)



set_world_size(4)
while(True):
	unlk(Unlocks.Speed)
	unlk(Unlocks.Hats)
	unlk(Unlocks.Expand, 3)
	unlk(Unlocks.Plant)
	unlk(Unlocks.Carrots)
	unlk(Unlocks.Trees)
	unlk(Unlocks.Pumpkins)
	unlk(Unlocks.Cactus)
	unlk(Unlocks.Watering)

	if num_items(Items.Hay) < 100:
		hay()
	elif num_items(Items.Wood) < 500:
		change_hat(Hats.Brown_Hat)
		plth(Entities.Bush)
		change_hat(Hats.Straw_Hat)
	elif num_items(Items.Carrot) < 200:
		plth(Entities.Carrot)
	elif num_items(Items.Pumpkin) < 6000:
		if num_unlocked(Unlocks.Pumpkins) > 0:
			pumpking_s.get_pumpkins(0.75)
	elif num_items(Items.Pumpkin) > 4 * 4 * 2:
		cactus.cactus_plant()
