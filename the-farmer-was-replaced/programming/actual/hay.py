while True:
	for x in range(get_world_size()):
		move(North)
		for y in range(get_world_size()):
			move(East)
			if can_harvest():
				harvest()
