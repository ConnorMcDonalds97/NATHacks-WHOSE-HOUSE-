import pygame
import const
import entities
class Game:
    def __init__(self, surface):
        self.bgRect = (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT) #x,y,width,height
        self.surface = surface

        self.sensor = (0,920, const.SCREEN_WIDTH, 5)

        self.tiles = []
        self.initTiles()
    def showBg(self):
        pygame.draw.rect(self.surface, 'black', self.bgRect)
        
    def showSensor(self):
        pygame.draw.rect(self.surface, 'red', self.sensor)

    def showTiles(self):
        for tile in self.tiles:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, 'white', (pos[0],pos[1],tile.width, tile.height))

    def initTiles(self):
        self.tiles = [entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SCREEN_WIDTH/2, 0)]