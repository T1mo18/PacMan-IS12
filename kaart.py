import sys
kaart= [
"#######################",
"#**********#**********#",
"#*###*####*#*####*###*#",
"#*********************#",
"#*###*#*#######*#*###*#",
"#*****#*#######*#*****#",
"#####*#****#****#*#####",
"#####*####*#*####*#####",
"#####*#*********#*#####",
"#####*#*###*###*#*#####",
"#*********************#",
"#*###*####*#*####*###*#",
"#***#*************#***#",
"###*#*#*#######*#*#*###",
"#*****#****#****#*****#",
"#*########*#*########*#",
"#*********************#",
"#######################",
]

def kaart_print():
	sys.stdout.write("\033[1;1H")
	for rida in kaart:
		print rida

def kaart_xy(x,y):
	print kaart[y-1] [x-1]

