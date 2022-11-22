import pygame
from pygame.draw import line
import config
import card
from math import floor
import config
class Field:
    def __init__(self):
        self.screen = pygame.Surface((config.FIELD_HEIGHT * config.GRID, config.FIELD_WIDTH * config.GRID))
        self.screen.fill(config.WHITE)
        self.cards = []

    def place(self, pos, card: card.Card):
        pos = (floor(pos[0] / config.GRID), floor(pos[1] / config.GRID))
        card.pos = pos
        self.cards.append(card)

    def draw(self, screen):
        screen.blit(self.screen, config.FIELD_COORDS)

    def update(self, card):
        card.draw(self.screen)


