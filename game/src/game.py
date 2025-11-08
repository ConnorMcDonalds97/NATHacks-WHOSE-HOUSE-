import pygame
import const
import entities
from song_processing import get_beats
class Game:
    def __init__(self, surface):
        self.score = 0

        self.bgRect = (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT) #x,y,width,height
        self.surface = surface

        self.sensor1 = entities.Tile(0,0, const.RED)
        self.sensor2 = entities.Tile(0,0, const.GREEN)
        self.sensor3 = entities.Tile(0,0, const.ORANGE)
        self.sensor4 = entities.Tile(0,0, const.BLUE)


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

    def checkTile(self, tile, sensorNum):
        if (tile.getPosition()[1] <= const.SENSOR_Y + 10) and ((tile.getPosition()[1] + tile.getDimensions()[1]) >= const.SENSOR_Y):
            if not tile.checkHit():
                tile.setHit()
                print(f"hit {sensorNum}")
                self.score += 1
            return True
        return False


    def checkSensor(self, sensorNum):
        print(f"checking {sensorNum}")
        match sensorNum:
            case 1:
                for tile in self.tiles1:
                    if self.checkTile(tile, 1):
                        break
            case 2:
                for tile in self.tiles2:
                    if self.checkTile(tile, 2):
                        break
            case 3:
                for tile in self.tiles3:
                    if self.checkTile(tile, 3):
                        break
            case 4:
                for tile in self.tiles4:
                    if self.checkTile(tile, 4):
                        break
    
    def showBg(self):
        pygame.draw.rect(self.surface, const.GREY, self.bgRect)
        
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
        score = self.font.render(f"Score: {self.score}", True, const.GREEN)
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
            self.tiles3.append(entities.Tile(const.SPAWN_3, d, const.LIGHT_ORANGE))
        for d in data4:
            self.tiles4.append(entities.Tile(const.SPAWN_4, d, const.LIGHT_BLUE))
