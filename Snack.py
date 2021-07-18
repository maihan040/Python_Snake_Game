"""
Snack.py

Module which contains the "Snack" class. 
This class will contain all the data needed to 
represent the snack object

	-Position - list object indicating the corresponding x,y coordinate within the screen where the snack is to be placed
	-Placed   - boolean variables indicating that the snack has already been placed or not 
"""
#################################################################
#						Import modules							#
#################################################################

import random 

class Snack: 
	def __init__(self, WinDim):
		self.get_new_rand_location(WinDim)
	
	#
	# Method to place the snack at a random location within the window 
	#
	def get_new_rand_location(self, WinDim):
		self.Position = [random.randrange(1, (WinDim.x // 10)) * 10, random.randrange(1, (WinDim.y // 10)) * 10]
		self.Placed = True