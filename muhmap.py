#Because map was taken
from gameobject import GameObject
import settings as stg
import numpy as np

class Tile(GameObject):

	def __init__(self, spritesheet, pos):
		super().__init__()
		self.sprite = spritesheet.get_slice(pos[0], pos[1], stg.GRID_SIZE, stg.GRID_SIZE)
		self.pos = pos


class Map:
	def __init__(self,spritesheet):
		self.tiles = []
		for x in range(0, 640, stg.GRID_SIZE):
			for y in range(0, 480, stg.GRID_SIZE):
				self.tiles.append(Tile(spritesheet, (x, y)))

def berry_colision(pos):
	if pos[0] <= 2:
		return True
	if pos[1] <= 3:
		return True
	if pos[0] <= 5:
		if (pos[1] == 4) or (pos[1] == 5):
			return True
	return False