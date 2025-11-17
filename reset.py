unlocks = {}
items = {}
globals = {}
i_unlocks = Unlocks
sim_items = {
			 Items.Hay : 100,
			 Items.Wood : 1501,
			 Items.Carrot : 100000,
			 Items.Pumpkin : 7000,
			 Items.Hay : 50,
			 Items.Pumpkin : 5000,
			 Items.Wood : 500,
			 Items.Carrot : 10000,
			 Items.Hay : 50,
			 }
#um valor de semente negativo significa uma semente aleatória
seed = -1
speedup = 10000
simulate("rscript", unlocks, items, globals, seed, speedup)

