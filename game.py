import pygame
import config
import player
import field
import card


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.players = []
        self.clock = pygame.time.Clock()
        self.finished = False
        self.field = field.Field()
        self.next_card = card.Card()

    def draw(self):
        self.screen.fill(config.WHITE)
        self.field.draw(self.screen)
        pygame.display.update()

    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if config.FIELD_COORDS[0] <= event.pos[0] < config.FIELD_COORDS[0] + config.FIELD_WIDTH * config.GRID and \
                        config.FIELD_COORDS[1] <= event.pos[1] < config.FIELD_COORDS[1] + config.FIELD_HEIGHT * config.GRID:
                    self.field.place((event.pos[0] - config.FIELD_COORDS[0], event.pos[1] - config.FIELD_COORDS[1]), self.next_card)
                    #self.field.update
                    self.next_card = card.Card()


    def run(self):
        while not self.finished:
            self.draw()
            self.clock.tick(config.FPS)
            self.event_processing()


