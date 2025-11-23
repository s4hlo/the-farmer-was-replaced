def check_has_item(item, num=1):
	# DEPRECATED use can_pay_for()
	# Args:
	#     item: obj under class Items
	#     num: number to check 
	if num_items(item) < num:
		return False
	return True

def can_pay_for(entity, num=1):
	# Checks if I can pay for the
	# desired item(s).
	costs = get_cost(entity)
	if not costs:
		return True
	for k in costs:
		v = costs[k]
		if not check_has_item(k, v * num):
			return False
	return True