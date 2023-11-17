import pygame, sys
from settings import *
"""
token para o github
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
"""

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.screen.fill('black')
                pygame.display.update()
                self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

