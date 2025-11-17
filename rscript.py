import dino
import pumpking_s
import cactus
import u
import collect_weird
def base(a, g, h):
	u.smart_fertilizer()
	if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
		harvest() 
		u.till_to(g)
		if not h:
			plant(a)
			u.smart_fertilizer()
			u.smart_water()

def plth(a):
	base(a, Grounds.Soil, False)


def hay():
	base(Entities.Hedge, Grounds.Grassland, True)

def unlk(e, i = 1):
	if (num_unlocked(e) < i):
		unlock(e)


set_world_size(6)
while(True):
	unlk(Unlocks.Speed)
	unlk(Unlocks.Hats)
	unlk(Unlocks.Expand, 4)
	unlk(Unlocks.Plant)
	unlk(Unlocks.Carrots)
	unlk(Unlocks.Trees)
	unlk(Unlocks.Pumpkins)
	unlk(Unlocks.Cactus)
	unlk(Unlocks.Watering)
	unlk(Unlocks.Dinosaurs)
	unlk(Unlocks.Fertilizer, 4)
 
 

	if num_items(Items.Hay) < 100:
		hay()
	elif num_items(Items.Wood) < 1500:
		change_hat(Hats.Brown_Hat)
		plth(Entities.Bush)
		change_hat(Hats.Straw_Hat)
	elif num_items(Items.Carrot) < 200:
		plth(Entities.Carrot)
	elif num_items(Items.Pumpkin) < 6000:
		if num_unlocked(Unlocks.Pumpkins) > 0:
			pumpking_s.get_pumpkins(0.75)
	elif num_unlocked(Unlocks.Dinosaurs) > 0 and num_items(Items.Cactus) > 100:
		dino.circular_path()
	# elif num_items(Items.Weird_Substance) < 500:
	# 	collect_weird.collect_base()
	elif num_items(Items.Pumpkin) > 4 * 4 * 2:
		cactus.cactus_plant()
  
	
