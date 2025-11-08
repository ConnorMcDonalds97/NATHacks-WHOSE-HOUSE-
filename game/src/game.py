import pygame
import const
import entities

SCORE = 0
class Game:
    def __init__(self, surface):
        self.bgRect = (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT) #x,y,width,height
        self.surface = surface
        self.sensor = entities.Tile(const.SCREEN_WIDTH, const.SENSOR_HEIGHT, 0, const.SENSOR_Y, 'white')
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.tiles = initTiles()
        self.tileCount = len(self.tiles)
        self.front = 0
        self.back = 0
        self.setBack()
    
    def setBack(self):
        
        while self.back < self.tileCount:
            if self.tiles[self.back].pos[1] + const.TILE_HEIGHT > -10:
                self.back += 1
            else:
                break

    def showBg(self):
        pygame.draw.rect(self.surface, 'black', self.bgRect)
        
    def showSensor(self):
        pygame.draw.rect(self.surface, self.sensor.colour, self.sensor.getRectInfo())

    def showTiles(self):
        for i in range(self.front, self.back):
            pos = self.tiles[i].getPosition()
            pygame.draw.rect(self.surface, 'white', (pos[0],pos[1],self.tiles[i].width, self.tiles[i].height))

    def showScore(self):
        score = self.font.render(f"Score: {SCORE}", True, "green")
        self.surface.blit(score, ((const.SCREEN_WIDTH / 2) - (score.width / 2), 5))

    def draw(self):
        self.showBg()
        self.showTiles()
        self.showSensor()
        self.showScore()
      
def initTiles():
    return [entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SPAWN_1, 0, "white"),
            entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SPAWN_2, -100, "white"),
            entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SPAWN_1, -200, "white"),
            entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SPAWN_4, -300, "white"),
            entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SPAWN_4, -400, "white"),
            entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SPAWN_3, -500, "white"),
            entities.Tile(const.TILE_WIDTH,const.TILE_HEIGHT, const.SPAWN_1, -600, "white")]

