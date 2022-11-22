import pygame
from pygame.draw import line
import config
class Field:
    def __init__(self):
        self.screen = pygame.Surface((config.FIELD_HEIGHT * config.GRID, config.FIELD_WIDTH * config.GRID))
        self.cards = []

    def place(self, pos):
        pass

    def draw(self):
        pass

    def update(self):
        pass


