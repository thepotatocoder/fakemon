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
		self.font = pygame.font.Font('media/DejaVuSansMono.ttf', 18)
		self.last_fps = TARGET_FPS
		
		self.last_cycle = 1/TARGET_FPS * 1000
		self.num_cycle = 1
		self.sum_cycle = self.last_cycle
		self.min_cycle = self.last_cycle
		self.max_cycle = self.last_cycle

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
		fps_text = self.font.render('fps: {:3.1f}'.format(self.last_fps), True, (0,0,0))
		stats_text = self.font.render(
				'cycle_ms: {:4.1f}; min: {:4.1f}; max: {:4.1f}; avg: {:4.1f}'.format(
				self.last_cycle, self.min_cycle, self.max_cycle, self.sum_cycle/self.num_cycle),
				True,
				(0, 0, 0)
			)
		self.window.blit(fps_text, (0, 0))
		self.window.blit(stats_text, (0, 20))
		pygame.display.flip()

		curr_time = time.time()
		diff = curr_time - self.prev_time
		print(diff)
		self.last_cycle = diff*1000
		delay = max(1.0/TARGET_FPS - diff, 0)
		time.sleep(delay)
		self.last_fps = 1.0/(delay + diff)
		self.prev_time = curr_time

		self.num_cycle += 1
		if self.last_cycle < self.min_cycle:
			self.min_cycle = self.last_cycle
		elif self.last_cycle > self.max_cycle:
			self.max_cycle = self.last_cycle
		
		self.sum_cycle += self.last_cycle


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
	
