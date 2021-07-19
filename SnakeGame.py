"""
SnakeGame.py

Module which contains the "SnakeGame" class. 
This class will contain all the indiviudal objects 
needed to play the game

"""
#################################################################
#			Import modules				#
#################################################################
import time 
import pygame 
from Snake import Snake
from Snack import Snack
from pygame import mixer 
from Player import Player
from GameColors import GameColors
from SoundFiles import SoundFiles
from WindowDimensions import WindowDimensions

#################################################################
#			Class definition			#
#################################################################
class SnakeGame:
    
    def __init__(self, win_x, win_y, player_name, sound_file_eat, sound_file_death):
        
	    # Initializing pygame 
        pygame.init()

	    # Initializing the mixer 
        mixer.init()

	    # Initialize the game window 
        pygame.display.set_caption('Snake Game')

        # Member variables 
        self.Snake      = Snake()
        self.Colors     = GameColors()
        self.WinDim     = WindowDimensions(win_x, win_y)
        self.Snack      = Snack(self.WinDim)
        self.FPS        = pygame.time.Clock() # Frame rate controller 
        self.Player     = Player(player_name)
        self.Sounds     = SoundFiles(mixer, sound_file_eat, sound_file_death)
        self.GameWindow = pygame.display.set_mode((self.WinDim.x, self.WinDim.y))
    
	# 
	# Method to play the game 
	#
    def Play_Game(self): 

	    while True:
	    	# handling key events
	    	for event in pygame.event.get():
	    		if event.type == pygame.KEYDOWN:
	    			if event.key == pygame.K_UP:
	    				self.Snake.ChangeTo = 'UP'
	    			if event.key == pygame.K_DOWN:
	    				self.Snake.ChangeTo = 'DOWN'
	    			if event.key == pygame.K_LEFT:
	    				self.Snake.ChangeTo = 'LEFT'
	    			if event.key == pygame.K_RIGHT:
	    				self.Snake.ChangeTo = 'RIGHT'

	    	# Logic to ensure the Snake doesn't simultaneously move in two opposing directions 
	    	if self.Snake.ChangeTo == 'UP' and self.Snake.Direction != 'DOWN':
	    		self.Snake.Direction = 'UP'
	    	if self.Snake.ChangeTo == 'DOWN' and self.Snake.Direction != 'UP':
	    		self.Snake.Direction = 'DOWN'
	    	if self.Snake.ChangeTo == 'LEFT' and self.Snake.Direction != 'RIGHT':
	    		self.Snake.Direction = 'LEFT'
	    	if self.Snake.ChangeTo == 'RIGHT' and self.Snake.Direction != 'LEFT':
	    		self.Snake.Direction = 'RIGHT'

	    	# Logic of the Snake movement. Only the first element of the list (the head) is being moved 
	    	if self.Snake.Direction == 'UP':
	    		self.Snake.Position[1] -= 10
	    	if self.Snake.Direction == 'DOWN':
	    		self.Snake.Position[1] += 10
	    	if self.Snake.Direction == 'LEFT':
	    		self.Snake.Position[0] -= 10
	    	if self.Snake.Direction == 'RIGHT':
	    		self.Snake.Position[0] += 10

	    	# Snake body growth mechanism, body will grow by 10 once Snake and Snack collide
	    	self.Snake.Body.insert(0, list(self.Snake.Position))
	    	if self.Snake.Position[0] == self.Snack.Position[0] and self.Snake.Position[1] == self.Snack.Position[1]:
	    		self.Sounds.eating_sound.play()
	    		self.Player.Score += 10
	    		self.Snack.Placed = False
	    	else:
	    		self.Snake.Body.pop()

	    	if not self.Snack.Placed:
	    		self.Snack.get_new_rand_location(self.WinDim)
    
			# Note that the snack has been placed 
	    	self.Snack.Placed = True

			# Fill the background color of the surface object 
	    	self.GameWindow.fill(self.Colors.Black)

	    	# Draw the Snake body on screen 
	    	for pos in self.Snake.Body:
	    		pygame.draw.rect(self.GameWindow, self.Colors.Green, pygame.Rect(pos[0], pos[1], 10, 10))

	    	# Draw the Snack on screen
	    	pygame.draw.rect(self.GameWindow, self.Colors.White, pygame.Rect(self.Snack.Position[0], self.Snack.Position[1], 10, 10))

	    	#############################################################
	    	#           Conditions when game will be over               #
	    	#############################################################

	    	# Touching any of the four walls
	    	if self.Snake.Position[0] < 0 or self.Snake.Position[0] > self.WinDim.x -10:
	    		self.Game_Over()
	    	if self.Snake.Position[1] < 0 or self.Snake.Position[1] > self.WinDim.y-10:
	    		self.Game_Over()

	    	# Touching its body
	    	for block in self.Snake.Body[1:]:
	    		if self.Snake.Position[0] == block[0] and self.Snake.Position[1] == block[1]:
	    			self.Game_Over()

	    	# Display score countinuously
	    	self.Player.Show_Score(self.Colors.White, 'times new roman', 20, self.GameWindow)

	    	# Refresh game screen
	    	pygame.display.update()

	    	# Frame Per Second /Refres Rate
	    	self.FPS.tick(self.Snake.Speed)
        
	#
	# Method to indicate the game is over 
	#
    def Game_Over(self):

	    # Play the game over music
	    self.Sounds.game_over_sound.play()

	    # Create the font object 
	    MyFont = pygame.font.SysFont('times new roman', 30)
    
	    # Create a text surface on which the text can be drwan 
	    GameOverSurface = MyFont.render("Game Over !!! Your Score is : " + str(self.Player.Score), True, self.Colors.Red)
    
	    # Box the text surface to have it later positioned in the center of the window 
	    GameOverRect = GameOverSurface.get_rect()
    
	    # Set the position of the text 
	    GameOverRect.midtop = (self.WinDim.x / 2, self.WinDim.y / 4)
    
	    # Use "blit" to draw the text on the screen 
	    self.GameWindow.blit(GameOverSurface, GameOverRect)

		# "Update the full display Surface to the screen"
	    pygame.display.flip()
    
	    # Sleep for a couple seconds before quitting the game 
	    time.sleep(2)
    
	    # Quit the pygame library  
	    pygame.quit()
    
	    # Quit the program 
	    quit()
