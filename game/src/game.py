import pygame
import const
import entities

SCORE = 0
class Game:
    def __init__(self, surface):
        self.bgRect = (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT) #x,y,width,height
        self.surface = surface

        self.sensor = entities.Tile(0, 0, 'white')
        self.sensor.setDimensions(const.SCREEN_WIDTH, const.SENSOR_HEIGHT)
        self.sensor.setPosition(0, const.SENSOR_Y)
        
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.tiles1 = []
        self.tiles2 = []
        self.tiles3 = []
        self.tiles4 = []
        self.initTiles()
    
    def showBg(self):
        pygame.draw.rect(self.surface, 'black', self.bgRect)
        
    def showSensor(self):
        pygame.draw.rect(self.surface, self.sensor.colour, self.sensor.getRectInfo())

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

