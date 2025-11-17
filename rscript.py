import dino
import pumpking_s
import cactus
import u
import collect_weird
import maze_astar
import sunflower_opt
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
	
# def cost(unlock, item, limit, min):
# 	if get_cost(unlock, limit - 1)[item] < min:
# 	return min
# 	if num_unlocked(unlock) == limit:
# 		return get_cost(unlock, limit - 1)[item]
# 	cost = get_cost(unlock)
# 	if cost[item] < min:
# 		return min
# 	return cost[item]
	


# set_world_size(6)
while(True):
	unlk(Unlocks.Grass, 3)
	unlk(Unlocks.Speed)
	unlk(Unlocks.Hats)
	unlk(Unlocks.Expand, 6)
	unlk(Unlocks.Plant)
	unlk(Unlocks.Carrots)
	unlk(Unlocks.Trees)
	unlk(Unlocks.Pumpkins)
	unlk(Unlocks.Cactus)
	unlk(Unlocks.Watering)
	unlk(Unlocks.Sunflowers)
	unlk(Unlocks.Dinosaurs)
	unlk(Unlocks.Fertilizer, 4)
	unlk(Unlocks.Mazes)
	unlk(Unlocks.Leaderboard)
 
 
 
	# if num_unlocked(Unlocks.Sunflowers) > 0 and num_items(Items.Power) < 100 and num_items(Items.Carrot) == 500:
	# 	sunflower_opt.power(200)
 

	if num_items(Items.Hay) < 100:
		hay()
	elif num_items(Items.Wood) < 1500:
		change_hat(Hats.Brown_Hat)
		plth(Entities.Bush)
		change_hat(Hats.Straw_Hat)
	elif num_items(Items.Carrot) < 500:
		plth(Entities.Carrot)
	elif num_items(Items.Pumpkin) < 8000:
		if num_unlocked(Unlocks.Pumpkins) > 0:
			pumpking_s.get_pumpkins(0.75)
	elif num_items(Items.Weird_Substance) < 1000:
		collect_weird.collect_base()
	elif num_unlocked(Unlocks.Mazes) > 0 and num_items(Items.Gold) < 1000000:
		maze_astar.run()
	elif num_items(Items.Pumpkin) > 4 * 4 * 2 and num_items(Items.Cactus) < 100:
		cactus.cactus_plant()
	elif num_unlocked(Unlocks.Dinosaurs) > 0 and num_items(Items.Bone) < 2000000:
		dino.circular_path()
	
	
