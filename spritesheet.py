import pygame
import settings
# pylint: disable=E1121

class Spritesheet:

	def __init__(self, sheet_path):
		self.sheet = pygame.image.load(sheet_path).convert_alpha()
		size = self.sheet.get_size()
		self.sheet = pygame.transform.scale(self.sheet, (settings.SCALE * size[0], settings.SCALE * size[1]))
		#self.sheet.set_alpha(128)
		#self.sheet.set_colorkey((0,0,0))

	def get_slice(self, x, y, width, height):
		image = pygame.Surface((width, height), pygame.SRCALPHA)
		image.blit(self.sheet, (0,0), (x,y,width,height))
		return image
