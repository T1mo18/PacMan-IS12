import time

x = 100
y = 2

def elukas_print():
	elukas = "\033[" + str(y) + ";" + str(x) + "H$"
	elukas = "\033[91m" + elukas

	print elukas

def elukas_next():
	# Get pacman position
	pacman = player_xy()
	
	# Search pacman from right/top
	if pacman[0] > x and pacman[1] <= y:
		# Look right
		if kaart_xy(x+1, y) == 1:
			x = x+1
			y = y
		# Look left
		elif kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
		# Look up
		elif kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
		# Look down
		elif kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
			

	# Search pacman from left/top
	if pacman[0] < x and pacman[1] <= y:
		# Look left
		if kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
		# Look right
		elif kaart_xy(x+1, y) == 1:
			x = x+1
			y = y
		# Look up
		elif kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
		# Look down
		elif kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
			

	# Search pacman from top/right
	if pacman[0] <= x and pacman[1] <= y:
		# Look up
		if kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
		# Look down
		elif kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
		# Look left
		elif kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
		# Look right
		elif kaart_xy(x+1, y) == 1:
			x = x+1
			y = y

	# Search pacman from bottom/left
	if pacman[0] >= x and pacman[1] >= y:
		# Look down
		if kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
		# Look up
		elif kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
		# Look left
		elif kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
		# Look right
		elif kaart_xy(x+1, y) == 1:
			x = x+1
			y = y
				


def elukas_xy():
	print "{};{}".format(x, y)
	return [x, y]


elukas_print()
elukas_xy()

