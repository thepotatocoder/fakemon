import pygame
from gameobject import GameObject
import settings as stg
from muhmap import berry_colision

START_POS = 8 * stg.SCALE, 24 * stg.SCALE
SIZE_EACH = 16 * stg.SCALE, 32 * stg.SCALE
SPRITESHEET_PATH = 'media/playeroverworld.png'
MOVE_TICKS = stg.TARGET_FPS/15/4
ANIM_TICKS = 30 * stg.TARGET_FPS/15/4

anim_down = 0, 3
anim_up = 4, 7
anim_left = 8, 11
anim_right = 12, 15

class Player(GameObject):

	def __init__(self, spritesheet, pos=(0,0)):
		super().__init__(pos)
		#self.pos = (self.pos[0], self.pos[1]+1) #Sprite workaround
		self.sprite = []
		wheres = [(8,24), (24,24), (40,24), (24,24),
				  (8,56), (24,56), (40,56), (24,56),
				  (8,88), (24,88), (40,88), (24,88)]

		for x in wheres:
			self.sprite.append(spritesheet.get_slice(x[0] * stg.SCALE, x[1] * stg.SCALE, SIZE_EACH[0], SIZE_EACH[1]))

		for i in range(8, 12):
			size = self.sprite[i].get_size()
			self.sprite.append(pygame.transform.flip(self.sprite[i], True, False))
		
		print(len(self.sprite))
		#print(len(self.sprite))
		self.min_frame = anim_down[0]
		self.curr_frame = anim_down[0]
		self.max_frame = anim_down[1]

		self.moving = False
		self.idle = True
		self.colliding = False
		self.target_pos = self.pos

		self.curr_anim = 'down'
		self.move_tick = MOVE_TICKS
		self.anim_tick = ANIM_TICKS

	def input(self, keys):
		if not self.moving:
			self.idle = False
			self.colliding = False
			if keys[pygame.K_a] or keys[pygame.K_LEFT]:
				self.dir = 'left'
				if self.curr_anim != 'left':
					self.curr_anim = 'left'
					self.curr_frame = anim_left[0]
					self.min_frame = anim_left[0]
					self.max_frame = anim_left[1]
				
				self.target_pos = self.pos[0] - stg.GRID_SIZE, self.pos[1]	
				if berry_colision((self.target_pos[0]/stg.GRID_SIZE, self.target_pos[1]/stg.GRID_SIZE)):
					self.target_pos = self.pos
					self.colliding = True
				else:
					self.moving = True
			
			elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
				self.dir = 'right'
				if self.curr_anim != 'right':
					self.curr_anim = 'right'
					self.curr_frame = anim_right[0]
					self.min_frame = anim_right[0]
					self.max_frame = anim_right[1]
				
				self.target_pos = self.pos[0] + stg.GRID_SIZE, self.pos[1]
				if berry_colision((self.target_pos[0]/stg.GRID_SIZE, self.target_pos[1]/stg.GRID_SIZE)):
					self.target_pos = self.pos
					self.colliding = True
				else:
					self.moving = True
					
			
			elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
				self.dir = 'down'
				if self.curr_anim != 'down':
					self.curr_anim = 'down'
					self.curr_frame = anim_down[0]
					self.min_frame = anim_down[0]
					self.max_frame = anim_down[1]
				
				self.target_pos = self.pos[0], self.pos[1] + stg.GRID_SIZE
				if berry_colision((self.target_pos[0]/stg.GRID_SIZE, self.target_pos[1]/stg.GRID_SIZE)):
					self.target_pos = self.pos
					self.colliding = True
				else:
					self.moving = True
					
			
			elif keys[pygame.K_w] or keys[pygame.K_UP]:
				self.dir = 'up'
				
				if self.curr_anim != 'up':
					self.curr_anim = 'up'
					self.curr_frame = anim_up[0]
					self.min_frame = anim_up[0]
					self.max_frame = anim_up[1]
				
				self.target_pos = self.pos[0], self.pos[1] - stg.GRID_SIZE
				if berry_colision((self.target_pos[0]/stg.GRID_SIZE, self.target_pos[1]/stg.GRID_SIZE)):
					self.target_pos = self.pos
					self.colliding = True
				else:
					self.moving = True
			
			else:
				self.idle = True
					

	def tick(self):
		#Movement
		#print('Moving: {}; Move_tick: {}\nPos: {}; Target: {}'.format(self.moving, self.move_tick, self.pos, self.target_pos))
		if self.moving and self.move_tick == MOVE_TICKS:
			if self.dir == 'left':
				self.pos = self.pos[0] - 1, self.pos[1]
			elif self.dir == 'right':
				self.pos = self.pos[0] + 1, self.pos[1]
			elif self.dir == 'down':
				self.pos = self.pos[0], self.pos[1] + 1
			elif self.dir == 'up':
				self.pos = self.pos[0], self.pos[1] - 1
		
		self.move_tick -= 1

		if self.move_tick == 0:
			self.move_tick = MOVE_TICKS
		
		self.anim_tick -= 1
		if self.anim_tick < 0:
			self.anim_tick = ANIM_TICKS
			if not self.idle:
				self.curr_frame += 1
				if self.curr_frame >= self.max_frame+1:
					self.curr_frame = self.min_frame

		if self.pos == self.target_pos:
			self.moving = False
			if self.idle or self.colliding:
				self.curr_frame = self.min_frame + 1
			self.move_tick = MOVE_TICKS

