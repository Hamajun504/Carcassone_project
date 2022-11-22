from random import randint
from pygame.draw import *
import pygame
class Card:
    def __init__(self):
        #self.number = randint(1, 6)
        self.x = 0
        self.y = 0
        self.color = (0, 0, 0)
        self.game = False
        #self.right
        #self.left
        #self.top
        #self.bottom

    def draw(self, screen):
        rect(screen, self.color, (30, 30, self.x, self.y))

    def place(self):
