#Because map was taken
from gameobject import GameObject
import settings as stg
import numpy as np
import pygame

class Tile(pygame.sprite.DirtySprite):

	def __init__(self, spritesheet, pos):
		super().__init__()
		self.image = spritesheet.get_slice(pos[0], pos[1], stg.GRID_SIZE, stg.GRID_SIZE)
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		self.dirty = 1


class Map:
	def __init__(self,spritesheet):
		self.tiles = []
		for x in range(0, stg.WINDOW_W, stg.GRID_SIZE):
			for y in range(0, stg.WINDOW_H, stg.GRID_SIZE):
				self.tiles.append(Tile(spritesheet, (x,y)))
		
		self.matrix = np.zeros((int(stg.WINDOW_W/stg.GRID_SIZE), int(stg.WINDOW_H/stg.GRID_SIZE)))	
		for i in range(int(stg.WINDOW_W/stg.GRID_SIZE)):
			for j in range(int(stg.WINDOW_H/stg.GRID_SIZE)):
				#print(i,j)
				self.matrix[i,j] = berry_colision((i,j))

	def collision_map(self, pos):
		try:
			return self.matrix[int(pos[0]), int(pos[1])]
		except IndexError:
			return 0


def berry_colision(pos):
	x = int(pos[0])
	y = int(pos[1])

	if x <= 2:
		return 1
	if y <= 3:
		return 1
	if x <= 5:
		if (y == 4) or (y == 5):
			return 1
	return 0
