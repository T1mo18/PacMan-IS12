from elukad import *
from kaart import *

x = 10 
y = 10

def player_print():
	player = "\033["+str(y)+";"+str(x)+"H" + "G"
	player = "\033[93m" + player + "\033[0m"

	print player

def player_next():
	# 'j' = left
	# 'l' = right
	# 'i' = up
	# 'k' = down
	global x
	global y
	
	while True:
		mov = raw_input("Sisesta liikumissuund (j,l,i,k) -> ")
		if mov == "i":
			y = y + 1
			print player_next
		elif mov == "j":
			x = x - 1
			print player
		elif mov == "l":
			x = x + 1
			print player
		elif mov == "k":
			y = y - 1
			print player
		
def player_xy():
    global x
    global y
