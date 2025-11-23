def is_even(num):
	return num % 2 == 0

def is_odd(num):
	return not is_even(num)


def clamp(num, left, right):
	# Clamp a number between a given min and max.
	return min(max(num, left), right)

def ring_clamp(num, width):
	return num % width