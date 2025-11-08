import pygame
import const
import entities

SCORE = 0
class Game:
    def __init__(self, surface):
        self.bgRect = (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT) #x,y,width,height
        self.surface = surface

        self.sensor1 = entities.Tile(0,0,'red')
        self.sensor2 = entities.Tile(0,0,'green')
        self.sensor3 = entities.Tile(0,0,'orange')
        self.sensor4 = entities.Tile(0,0,'blue')


        self.sensor1.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)
        self.sensor2.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)
        self.sensor3.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)
        self.sensor4.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)

        self.sensor1.setPosition(const.SENSOR_OFFSET_LEFT, const.SENSOR_Y)
        self.sensor2.setPosition(const.SENSOR_OFFSET_LEFT + const.SENSOR_WIDTH * 1, const.SENSOR_Y)
        self.sensor3.setPosition(const.SENSOR_OFFSET_LEFT + const.SENSOR_WIDTH * 2, const.SENSOR_Y)
        self.sensor4.setPosition(const.SENSOR_OFFSET_LEFT + const.SENSOR_WIDTH * 3, const.SENSOR_Y)


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
        pygame.draw.rect(self.surface, self.sensor1.colour, self.sensor1.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor2.colour, self.sensor2.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor3.colour, self.sensor3.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor4.colour, self.sensor4.getRectInfo())


    def showTiles(self):
        for i in range(self.front, self.back):
            tile = self.tiles[i]
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1],self.tiles[i].width, self.tiles[i].height))

    def showScore(self):
        score = self.font.render(f"Score: {SCORE}", True, "green")
        self.surface.blit(score, ((const.SCREEN_WIDTH / 2) - (score.get_width() / 2), 5))

    def draw(self):
        self.showBg()
        self.showTiles()
        self.showSensor()
        self.showScore()
      
def initTiles():
    return [entities.Tile(const.SPAWN_1, 1, "green"),
            entities.Tile(const.SPAWN_2, 10, "white"),
            entities.Tile(const.SPAWN_1, 11, "white"),
            entities.Tile(const.SPAWN_4, 12, "white"),
            entities.Tile(const.SPAWN_4, 13, "green"),
            entities.Tile(const.SPAWN_3, 14, "white"),
            entities.Tile(const.SPAWN_1, 15, "white")]

