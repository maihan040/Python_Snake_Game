"""
Player.py

Module which contains the "player" class. 
This class will contain all the data needed to keep track 
of the players attributes which will be: 

	-Name
	-Score
	-Max Score

"""
#################################################################
#						Import modules							#
#################################################################
import pygame 

#################################################################
#						Class definition						#
#################################################################
class Player: 

	def __init__(self, Name, Score = 0, MaxScore = 0):
		self.Name = Name
		self.Score = Score
		self.MaxScore = MaxScore
	
	#
	# Method to display the player's score
	#
	def Show_Score(self, Color, Font, Size, GameWindow): 
	
		# Create the score font object 
		ScoreFont = pygame.font.SysFont(Font, Size)

		# Create display surface object 
		ScoreSurface = ScoreFont.render("Score : " + str(self.Score), True, Color)

		# Create a rectangular object for the text surface object 
		ScoreRect = ScoreSurface.get_rect()

		# Display the text 
		GameWindow.blit(ScoreSurface, ScoreRect)