from kaart import *
from player import *
from random import randint	
x = 2
y = 2
suund = 'down'

def elukas_print():
	global x
	global y
	
	elukas = "\033[" + str(y) + ";" + str(x) + "H$"
	elukas = "\033[91m" + elukas + "\033[0m"

	print elukas

def elukas_move(direction):
	global x
	global y

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
		# Look down
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
	global x
	global y

	directions = ['left','right','up','down']
	direction = randint(0,3)	
	direction = directions[direction]

	elukas_move(direction)


def elukas_xy():
	global x
	global y

	return [x, y]
