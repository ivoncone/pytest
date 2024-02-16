import pygame 

from data.classes.square import Square 
from data.classes.pieces.rook import Rook
from data.classes.pieces.bishop import Bishop
from data.classes.pieces.knight import Knight
from data.classes.pieces.queen import Queen
from data.classes.pieces.king import King 
from data.classes.pieces.pawn import Pawn 

class Board:
	def __init__(self, width, height):
		self.width = width

