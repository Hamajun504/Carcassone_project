import pygame
import config
import player
import field


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.players = []
        self.clock = pygame.time.Clock()
        self.finished = False
        self.field = field.Field()

    def draw(self):
        # TODO
        pass

    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if config.FIELD_COORDS[0] <= event.pos[0] < config.FIELD_COORDS[0] + config.FIELD_WIDTH * config.GRID and


    def run(self):
        while not self.finished:
            self.draw()
            self.clock.tick(config.FPS)
            self.event_processing()

            # TODO

