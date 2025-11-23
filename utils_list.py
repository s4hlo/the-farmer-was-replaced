def all(ls):
	for x in ls:
		if not x:
			return False
	return True
	
def any(ls):
	for x in ls:
		if x:
			return True
	return False

def index(ls, item):
	for i in range(len(ls)):
		if ls[i] == item:
			return i
	return None # TODO raise exception

def max_with_index(ls):
	# Args:
	#     ls: list
	# Returns:
	#     value: maximum item
	#     index: maximum index
		
	if not ls:
		return None, -1
	
	max_val = ls[0]
	max_idx = 0
	
	for i in range(1, len(ls)):
		cur_val = ls[i]
		if cur_val > max_val:
			max_val = cur_val
			max_idx = i
	
	return max_val, max_idx

def extend(ls1, ls2):
	# Extend ls1 with ls2's values.
	for x in ls2:
		ls1.append(x)

def reversed(ls):
	# Reverse the list.
	res = []
	for i in range(len(ls) -1, -1, -1):
		res.append(ls[i])
	return res

def enumerate_list(ls):
	# Returns a list of (idx, val) pairs
	i = 0
	result = []
	for item in ls:
		result.append((i, item))
		i = i + 1
	return result

def serialize_2d_index(idx, dim_len):
	# Args:
	#     idx: 2-tuple  
	#     dim_len: int length of 0th dimension
	# Returns:
	#     int: serialized index
	
	return idx[1] * dim_len + idx[0]

def deserialize_2d_index(idx, dim_len):
	# Args:
	#     idx: int
	#     dim_len: int length of 0th dimension
	# Returns: 
	#     2-tuple: 2d matrix index
	
	return idx % dim_len, idx // dim_len

def serialize_2d_matrix(m):
	# Flattens a 2d matrix into a list.
	# Args:
	#     m: List[List]
	# Returns:
	#     list: flattened 1d matrix
	res = []
	for i in range(len(m)):
		extend(res, m[i])
	return res

def deserialize_2d_matrix_CC(m, dim_len):
	# Rebuilds 2d matrix from 1d.
	# Uses the Contiguous Chunks strategy.
	# Args:
	#     m: List
	#     dim_len: int 0th dim target length (number of rows)
	# Returns:
	#     list[list]: 2d matrix or None if invalid
	if dim_len <= 0:
		return None
	n = len(m)
	if n % dim_len != 0:
		return None  # must divide evenly for strict reshape

	# build dim_len rows
	cols = n // dim_len
	res = []
	i = 0
	while i < dim_len:
		res.append([])
		i = i + 1

	# fill row-major (contiguous chunks)
	i = 0
	while i < n:
		row_idx = i // cols
		res[row_idx].append(m[i])
		i = i + 1

	return res

def deserialize_2d_matrix_unsafe_CC(m, dim_len):
	# Rebuilds a 2D matrix from a 1D list, 
	# distributing items as evenly as possible.
	# Uses the Contiguous Chunks strategy.
	# Args:
	#     m: list
	#     dim_len: int 0th dim target length (number of rows)
	# Returns:
	#     list[list]: 2D "best-effort" matrix distributed CC
	if dim_len <= 0:
		return [m]

	n = len(m)
	if n == 0:
		temp = []
		for _ in range(dim_len):
			temp.append([])
		return temp

	# Compute base size and remainder 
	# (extra elements to distribute)
	rows = dim_len
	base = n // rows
	remainder = n % rows

	res = []
	idx = 0
	i = 0
	while i < rows:
		# Give one extra element to 
		# the first `remainder` rows
		if i < remainder:
			extra = 1
		else:
			extra = 0
		row_len = base + extra
		row = m[idx:idx + row_len]
		res.append(row)
		idx += row_len
		i += 1

	# If some elements remain (shouldn't 
	# happen), append them all to 
	# the last row
	if idx < n:
		res[-1].extend(m[index:])

	return res

def deserialize_2d_matrix_RR(m, dim_len):
	# Rebuilds 2d matrix from 1d.
	# Uses the Round Robin strategy.
	# Args:
	#     m: List
	#     dim_len: int 0th dim target length (number of rows)
	# Returns:
	#     list[list]: 2d matrix or None if invalid
	if dim_len <= 0:
		return None
	
	# NOTE update when list comps
	res = []
	i = 0
	while i < dim_len:
		res.append([])
		i = i + 1
		
	n = len(m)
	if n == 0:
		return res
	if n % dim_len != 0:
		return None  # must divide evenly for strict reshape

	# build exactly dim_len rows
	res = []
	i = 0
	while i < dim_len:
		res.append([])
		i = i + 1

	# round robin placement
	for idx, item in enumerate_list(m):
		res[idx % dim_len].append(item)

	return res

def deserialize_2d_matrix_unsafe_RR(m, dim_len):
	# Rebuilds a 2D matrix from a 1D list,
	# distributing items as evenly as possible.
	# Uses the Round Robin strategy.
	#
	# Args:
	#     m: list
	#     dim_len: int 0th dim target length (number of rows)
	# Returns:
	#     list[list]: 2D "best-effort" matrix distributed RR 

	if dim_len <= 0:
		return [m]

	n = len(m)
	# NOTE update when list comps [[] for _ in range(dim_len)]
	res = []
	for _ in range(dim_len):
		res.append([])
	if n == 0:
		return res
	
	# round robin placement
	for idx, item in enumerate_list(m):
		res[idx % dim_len].append(item)

	return res