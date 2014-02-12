from kaart import *
from player import *

x = 2
y = 2
pattern = []
force_dir = 0
force_start = 0

def elukas_print():
	global x
	global y
	
	elukas = "\033[" + str(y) + ";" + str(x) + "H$"
	elukas = "\033[91m" + elukas + "\033[0m"

	print elukas

def set_direction():
	global x
	global y
	global direction
	global pattern
	global force_dir
	
	player = player_xy()
	px = player[0]
	py = player[1]
	
	if not force_dir:
		if px > x and py > y:
			direction = 'right/down'
		elif px < x and py < y:
			direction = 'left/up'
		elif px == x and py < y:
			direction = 'up'
		elif px == x and py > y:
			direction = 'down'
		elif px > x and py == y:
			direction = 'right'
		elif px < x and py == y:
			direction = 'left'
	else:
		direction = force_dir
		
	return direction

def elukas_move(move):
	global x
	global y
	global force_dir
	global force_start

	player = player_xy()
	px = player[0]
	py = player[1]
		
	if len(pattern) > 4:
		if pattern[len(pattern)-1] == pattern[len(pattern)-3] and pattern[len(pattern)-2] == pattern[len(pattern)-4] and pattern[len(pattern)-2] != pattern[len(pattern)-1] and pattern[len(pattern)-2] == pattern[len(pattern)-4]:
			if direction == 'right':
				force_dir = 'left'
			if direction == 'down':
				force_dir = 'up'
			if direction == 'left':
				force_dir == 'right'
			if direction == 'right/down':
				force_dir == 'left/up'
			if direction == 'left/up':
				force_dir == 'right/down'

	if len(pattern) < force_start+7:
		force_dir = 0
	
	if force_dir:
		force_start = len(pattern)
		move = force_dir
				
	if move == 'right/down':
		if kaart_xy(x+1, y):
			x += 1		
			moved = 'right'
		elif kaart_xy(x, y+1):
			y += 1
			moved = 'down'
		elif kaart_xy(x-1, y):
			x -= 1
			moved = 'left'
		elif kaart_xy(x, y-1):
			y -= 1
			moved = 'up'

	if move == 'left/up':
		if kaart_xy(x-1, y):
			x -= 1
			moved = 'left'
		elif kaart_xy(x, y-1):
			y -= 1
			moved = 'up'
		elif kaart_xy(x, y+1):
			y += 1
			moved = 'down'
		elif kaart_xy(x+1, y):
			x += 1
			moved = 'right'

	if move == 'down':	
		
		if kaart_xy(x, y+1):
			y += 1
			moved = 'down'
		elif kaart_xy(x+1, y):
			x += 1
			moved = 'right'
		elif kaart_xy(x-1, y):
			x -= 1
			moved = 'left'
		elif kaart_xy(x, y-1):
			y -= 1
			moved = 'down'

	if move == 'up':	
		if kaart_xy(x, y-1):
			y -= 1			
			moved = 'up'
		elif kaart_xy(x-1, y):
			x -= 1
			moved = 'left'
		elif kaart_xy(x, y+1):
			y += 1
			moved = 'down'
		elif kaart_xy(x+1, y):
			x += 1		
			moved = 'right'

	if move == 'left':	
		if kaart_xy(x-1, y):
			x -= 1
			moved = 'left'	
		elif kaart_xy(x, y-1):
			y -= 1			
			moved = 'up'
		elif kaart_xy(x, y+1):
			y += 1
			moved = 'down'
		elif kaart_xy(x+1, y):
			x += 1		
			moved = 'right'

	if move == 'right':	
		if kaart_xy(x+1, y):
			x += 1		
			moved = 'right'	
		elif kaart_xy(x-1, y):
			x -= 1
			moved = 'left'	
		elif kaart_xy(x, y-1):
			y -= 1			
			moved = 'up'
		elif kaart_xy(x, y+1):
			y += 1
			moved = 'down'
		elif kaart_xy(x-1, y):
			x -= 1
			moved = 'left'				
		elif kaart_xy(x+1, y):
			x += 1		
			moved = 'right'
			
	pattern.append(moved)	

def elukas_next():
	global x
	global y

	# Get pacman position
	pacman = player_xy()

	px = pacman[0]
	py = pacman[1]
	
	# MOVE 
	movement = set_direction()
	elukas_move(movement)
	

def elukas_xy():
	global x
	global y

	return [x, y]
