#!/usr/bin/env python 
#-*- coding utf-8 -*-

from kaart import kaart_print
from elukad import elukas_print
from player import player_print
import time





def main():                
	while True:
		kaart_print()
		elukas_print()
		player_print()
		#elukas_next()
		#player_next()
      		time.sleep(1)
main()
