#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():		
	kaart_print()
	elukas_print()
	player_print()
	elukas_next()
	player_next()



x=0
while True:
		kaart_print(x)
		elukas_print(x)
		player_print(x)
		elukas_next()
		player_next()
		
		x=x+1
	
	return x
