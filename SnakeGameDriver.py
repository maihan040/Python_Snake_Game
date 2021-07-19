#
# SnakeGameDriver.py
#
# Description: Python game implementation of the classic "Snake" game 
# which was a popular game installed on many Nokia phones from the 
# mid 90s to the early 2000s
#
# Objective of the game is to have the Snake move around the window via the  
# up, down, left, and right arrow keys and collect the "snack" objects which 
# will be randomly placed throughout the window. The Snake will grow longer 
# which each snack that it consumes which makes the game more challenging 
# as it goes along 
#
# Additionally, the Snake is not suppose to hit any of the 4 walls, or its
# tail, as those will render the game over. 
#
# This module will only instantiate the game object where all the logic has 
# been implemented in. 
#
# Created on: 05/20/21
#
# Last updated on: 06/11/21

#################################################################################
#				Import Modules					#
#################################################################################
from SnakeGame import SnakeGame

#################################################################################
#			Main Method to play the game				#
#################################################################################
if __name__ == "__main__": 

	#
	# Instantiate main game object 
	#
	GameInstance = SnakeGame(720, 480, "SnakeLegend","pacman_eatfruit.wav", "pacman_death.wav")

	# Play the game 
	GameInstance.Play_Game()
