import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        """64x64 pixels prapreencher todo o espaco"""

        self.image = pygame.image.load('./assets/pedra.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

