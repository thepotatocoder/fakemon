import player
import muhmap
import spritesheet
import settings as stg
import pygame

SPRITESHEET_PATH = 'media/playeroverworld.png'
SPRITESHEET_PATH2 = 'media/berryforest.png'

class World:

	def __init__(self, loadmap=0):
		self.spritesheet = spritesheet.Spritesheet(SPRITESHEET_PATH)
		self.spritesheet2 = spritesheet.Spritesheet(SPRITESHEET_PATH2)
		self.player = player.Player(self.spritesheet)
		self.player.pos = (6 * stg.GRID_SIZE, 6 * stg.GRID_SIZE)
		self.map = muhmap.Map(self.spritesheet2)
		self.sprites = [self.player]
		
		self.tile_rects = pygame.sprite.LayeredDirty()
		for tile in self.map.tiles:
			#print(type(tile))
			self.tile_rects.add(tile)
		self.tile_rects.add(self.player)
			
	def tick(self, keys):
		if pygame.mouse.get_pressed()[0]:
			m = pygame.mouse.get_pos()
			self.map.matrix[int(m[0]/stg.GRID_SIZE), int(m[1]/stg.GRID_SIZE)] = 1

		self.player.input(keys, self.map)
		self.player.tick()
	
	def render(self, window):
		rects = self.tile_rects.draw(window)
		pygame.display.update(rects)

