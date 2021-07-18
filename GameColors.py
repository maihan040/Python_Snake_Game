"""
GameColors.py

Module which contains the "GameColors" class. 
This class contains variables that are accessible 
throughout many objects to indicate which color certain 
fonts/objects should be

"""
#################################################################
#						Import modules							#
#################################################################
import pygame 

#################################################################
#						Class definition						#
#################################################################
class GameColors:

	# This class will hold the color settings that will be used throughout the game 
	Black = pygame.Color(0, 0, 0)
	Red   = pygame.Color(255, 0, 0)
	Green = pygame.Color(0, 255, 0)
	Blue  = pygame.Color(0, 0, 255)
	White = pygame.Color(255, 255, 255)