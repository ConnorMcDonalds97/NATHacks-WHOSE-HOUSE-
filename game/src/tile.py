import pygame

class Tile:
    def __init__(self):
        self.image = pygame.surface((50,50))
        self.image.fill((255, 0, 0))