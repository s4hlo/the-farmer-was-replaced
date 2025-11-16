hats = [
	Hats.Brown_Hat,
	Hats.Gold_Hat,
	Hats.The_Farmers_Remains,
	Hats.Traffic_Cone,
	Hats.Wizard_Hat
]


def hat(i):
	change_hat(hats[i])
	while(True):
		move(North)

def hat_0():
	hat(0)
def hat_1():
	hat(1)
def hat_2():
	hat(2)
def hat_3():
	hat(3)
def hat_4():
	hat(4)


funcs = [
	hat_0,
	hat_1,
	hat_2,
	hat_3,
	hat_4,
]

set_execution_speed(1)
clear()
drone_1 = spawn_drone(hat_1)

for i in range(5):
	spawn_drone(funcs[i])
	move(East)

