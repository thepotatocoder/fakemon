import player
import muhmap
import spritesheet
import settings as stg

SPRITESHEET_PATH = 'media/playeroverworld.png'
SPRITESHEET_PATH2 = 'media/berryforest.png'

class World:

	def __init__(self, loadmap=0):
		self.spritesheet = spritesheet.Spritesheet(SPRITESHEET_PATH)
		self.spritesheet2 = spritesheet.Spritesheet(SPRITESHEET_PATH2)
		self.player = player.Player(self.spritesheet)
		self.player.pos = (6 * stg.GRID_SIZE, 6 * stg.GRID_SIZE)
		self.map = muhmap.Map(self.spritesheet2)

	def tick(self, keys):
		self.player.input(keys)
		self.player.tick()
	
	def render(self, window):
		for tile in self.map.tiles:
			window.blit(tile.sprite, tile.pos)
		window.blit(self.player.sprite[self.player.curr_frame], (self.player.pos[0], self.player.pos[1] - stg.GRID_SIZE))
		print((self.player.pos[0]/stg.GRID_SIZE, self.player.pos[1]/stg.GRID_SIZE))
