#!/usr/bin/env python 
#-*- coding utf-8 -*-

import pygame, sys
from pygame.locals import *

x,y=1,1
movex,movey=1,1
#	pygame.key.set_repeat(50, 50)

def player_print():
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type==KEYDOWN:
			if event.key==K_LEFT:
				print "Left"
			elif event.key==K_RIGHT:
				print "Right"
			elif event.key==K_UP:
				print "Up"
			elif event.key==K_DOWN:
				print "Down"
	x=movex
	y=movey

player_print()			
