"""
Snake.py

Module which contains the "Snake" class. 
This class will contain all data elements needed 
in order to represent the snake

	-Speed
	-Start_Pos 
	-Body
	-Direction
"""
#################################################################
#			Class definition			#
#################################################################
class Snake:

	# Default Settings
	Default_Speed = 30
	Default_Start_Pos = [100, 50]
	Default_Body = [[100, 50], [90, 50], [80, 50], [70, 50]]
	Default_Direction = 'RIGHT'

	def __init__(self, Speed = Default_Speed, 
					   Position = Default_Start_Pos, 
					   Body = Default_Body, 
					   Direction = Default_Direction, 
					   ChangeTo = Default_Direction):
		self.Speed = Speed
		self.Position = Position
		self.Body = Body
		self.Direction = Direction
		self.ChangeTo = Direction
