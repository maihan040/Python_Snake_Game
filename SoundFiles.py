"""
SoundFiles.py

Module which contains the "SoundFiles" class. 
This class contains variables which are used to load various
sounds files which will be played when certain game conditions 
are met

"""
#################################################################
#						Import modules							#
#################################################################
import pygame 

#################################################################
#						Class definition						#
#################################################################
class SoundFiles: 

	# This class contains the sound files that will be used throughout the game 
	def __init__(self, mixer, eating_sound_file, game_over_sound_file):
		self.eating_sound = mixer.Sound(eating_sound_file)
		self.game_over_sound = mixer.Sound(game_over_sound_file)