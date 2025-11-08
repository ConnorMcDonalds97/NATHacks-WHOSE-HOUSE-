import pygame
import const
import entities

SCORE = 0
class Game:
    def __init__(self, surface):
        self.bgRect = (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT) #x,y,width,height
        self.surface = surface
        self.sensor = entities.Tile(const.SCREEN_WIDTH, 5, 0, 920, 'white')
        self.tiles = initTiles()
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)


    def showBg(self):
        pygame.draw.rect(self.surface, 'black', self.bgRect)
        
    def showSensor(self):
        pygame.draw.rect(self.surface, self.sensor.colour, self.sensor.getRectInfo())

    def showTiles(self):
        for tile in self.tiles:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, 'white', (pos[0],pos[1],tile.width, tile.height))

    def showScore(self):
        score = self.font.render(f"Score: {SCORE}", True, "white")
        self.surface.blit(score, (0, 0))

    def initTiles(self):
        self.tiles = [entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SCREEN_WIDTH/2, 0, "white")]

    def draw(self):
        self.showBg()
        self.showTiles()
        self.showSensor()
        self.showScore()


def initTiles():
    return [entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SCREEN_WIDTH/2, 0, "white")]