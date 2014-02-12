#!/usr/bin/env python 
#-*- coding utf-8 -*-
from kaart import kaart_print
from elukad import elukas_print
from elukad import elukas_next
from elukad import elukas_xy
from player import player_print
from player import player_xy
from player import player_next
import time



def main():                
	while True:
		kaart_print()
		elukas_print()
		player_print()
		elukas_next()
		player_next()
		time.sleep(0.3)
		if elukas_xy()== player_xy():
			print "G4M3 0V3R"	
main()
