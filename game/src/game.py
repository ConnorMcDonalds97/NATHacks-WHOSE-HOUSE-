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

        self.tiles1 = []
        self.tiles2 = []
        self.tiles3 = []
        self.tiles4 = []
        self.initTiles()
    
    def showBg(self):
        pygame.draw.rect(self.surface, 'grey', self.bgRect)
        
    def showSensor(self):
        pygame.draw.rect(self.surface, self.sensor1.colour, self.sensor1.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor2.colour, self.sensor2.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor3.colour, self.sensor3.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor4.colour, self.sensor4.getRectInfo())


    def showTiles(self):
        for tile in self.tiles1:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))
        for tile in self.tiles2:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))
        for tile in self.tiles3:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))
        for tile in self.tiles4:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))

    def showScore(self):
        score = self.font.render(f"Score: {SCORE}", True, "green")
        self.surface.blit(score, ((const.SCREEN_WIDTH / 2) - (score.get_width() / 2), 5))

    def draw(self):
        self.showBg()
        self.showTiles()
        self.showSensor()
        self.showScore()
      
    def initTiles(self):
        data1 = [5,7,8,10,12]
        data2 = [4,6,8,9,11]
        data3 = [6,7,8,9]
        data4 = [3,5,6,8,10,12]
        for d in data1:
            self.tiles1.append(entities.Tile(const.SPAWN_1, d, const.LIGHT_RED))
        for d in data2:
            self.tiles2.append(entities.Tile(const.SPAWN_2, d, const.LIGHT_GREEN))
        for d in data3:
            self.tiles3.append(entities.Tile(const.SPAWN_3, d, const.LIGHT_YELLOW))
        for d in data4:
            self.tiles4.append(entities.Tile(const.SPAWN_4, d, const.LIGHT_BLUE))

