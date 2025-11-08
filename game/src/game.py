import pygame
import const
import entities
class Game:
    def __init__(self, surface):
        self.bgRect = (0,0, const.WIDTH, const.HEIGHT)
        self.surface = surface
        
        self.sensor = (0,920, const.WIDTH, 5)

        self.tiles = []
        self.initTiles()
    def showBg(self):
        pygame.draw.rect(self.surface, 'black', self.bgRect)

    def showSensor(self):
        pygame.draw.rect(self.surface, 'red', self.sensor)

    def showTiles(self):
        for tile in self.tiles:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, 'white', (tile.width, tile.height, pos[0], pos[1]))

    def initTiles(self):
        self.tiles = [entities.Tile(1000,50,100,20), entities.Tile(100,20,100,20)]