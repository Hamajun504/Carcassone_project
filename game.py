import pygame
import config
import player


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.players = []
        self.clock = pygame.time.Clock()

    def draw(self):
        # TODO
        pass

    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
        # TODO

    def run(self):
        self.draw()
        self.clock.tick(config.FPS)
        self.event_processing()
        # TODO

