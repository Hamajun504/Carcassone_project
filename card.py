import random
from pygame.draw import *
import pygame
import config
class Card:
    def __init__(self, pos=(0, 0)):
        #self.number = randint(1, 6)
        self.pos = pos
        self.color = random.choice(config.COLORS)
        self.game = False
        #self.right
        #self.left
        #self.top
        #self.bottom

    def draw(self, screen):
        rect(screen, self.color, (self.pos[0] * config.GRID, self.pos[1] * config.GRID, config.GRID, config.GRID))


