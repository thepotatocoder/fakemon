import pygame

class GameObject:

	def __init__(self, pos=(0,0)):
		self.pos = pos
		self.sprite = None
		self.rect = None


