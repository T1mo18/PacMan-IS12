import time
from kaart import kaart_xy

x = 3
y = 2
suund = 'down'

def elukas_print():
	elukas = "\033[" + str(y) + ";" + str(x) + "H$"
	elukas = "\033[91m" + elukas + "\033[0m"

	print elukas

def elukas_move(direction):

	if direction == 'right':

		# Look right
		if kaart_xy(x+1, y) == 1:
			x = x+1
			y = y
			suund = 'right'
		# Look down
		elif kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
			suund = 'down'	
		# Look up
		elif kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
			suund = 'up'
		# Look left
		elif kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
			suund = 'left'	

	if direction == 'left':

		# Look left
		if kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
			suund = 'left'	
		# Look up
		elif kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
			suund = 'up'
		# Look adown
		elif kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
			suund = 'down'	
		# Look right
		elif kaart_xy(x+1, y) == 1:
			x = x+1
			y = y
			suund = 'right'

	if direction == 'up':

		# Look up
		if kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
			suund = 'up'
		# Look left
		elif kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
			suund = 'left'	
		# Look right
		elif kaart_xy(x+1, y) == 1:
			x = x+1
			y = y
			suund = 'right'
		# Look down
		elif kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
			suund = 'down'	

	if direction == 'down':

		# Look down
		if kaart_xy(x, y+1) == 1:
			x = x
			y = y+1
			suund = 'down'
		# Look left
		elif kaart_xy(x-1, y) == 1:
			x = x-1
			y = y
			suund = 'left'	
		# Look right
		elif kaart_xy(x+1, y) == 1:
			x = x+1
			y = y
			suund = 'right'
		# Look up
		elif kaart_xy(x, y-1) == 1:
			x = x
			y = y-1
			suund = 'up'


def elukas_next():
	# Get pacman position
	pacman = player_xy()

	px = pacman[0]
	py = pacman[1]

	# Search pacman from right/bottom
	if px >= x and py >= y:
		elukas_move('right')

	# Search pacman from left/top
	elif px <= x and py <= y:
		elukas_move('left')


def elukas_xy():
	return [x, y]
