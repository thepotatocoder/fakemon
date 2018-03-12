import time
import pygame
from pygame import display

import world

TITLE = 'Fakemon'
VERSION = '1.0'
TARGET_FPS = 60

class GameStates:
	_none, Initializing, Running, Paused, Quitting = range(5)


class Game:
	
	def __init__(self, size):
		pygame.init()
		self.state = GameStates.Initializing
		self.size = size
		self.window = pygame.display.set_mode(size, pygame.HWACCEL)
		pygame.display.set_caption(TITLE)
		self.prev_time = time.time()
		self.world = world.World()
		self.run_count = 3600*3
		self.font = pygame.font.Font('media/DejaVuSans.ttf', 24)
		self.last_fps = TARGET_FPS

		self.state = GameStates.Running

	def run(self):
		keys = pygame.key.get_pressed()
		
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				print("we out!")
				self.state = GameStates.Quitting
				return
		
		self.window.fill((0,0,0))
		self.world.tick(keys)
		self.world.render(self.window)
		text = self.font.render("{}".format(int(self.last_fps)), True, (255,255,255))
		self.window.blit(text, (0, 0))
		pygame.display.flip()

		curr_time = time.time()
		diff = curr_time - self.prev_time
		delay = max(1.0/TARGET_FPS - diff, 0)
		time.sleep(delay)
		self.last_fps = 1.0/(delay + diff)
		self.prev_time = curr_time


		#DEADLY CODE x.x
		#pygame.display.set_caption('{} - {} [{}]'.format(TITLE, VERSION, int(fps)))

		#self.run_count -= 1

		if self.run_count == 0:
			self.state = GameStates.Quitting


	def loop(self):
		while 1:
			if self.state == GameStates.Initializing:
				#init?
				pass
			elif self.state == GameStates.Running:
				#GameLoop
				self.run()
				pass
			elif self.state == GameStates.Paused:
				#Maybe Paused and Running have their similarities
				pass
			elif self.state == GameStates.Quitting:
				#Pack things up
				break
				pass
			elif self.state == GameStates._none:
				#Uh oh maybe throw out an error?
				pass
	
