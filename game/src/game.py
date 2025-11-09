import pygame
import const
import entities
from song_processing import get_beats
import math

class Array:
    def __init__(self):
        self.front = 0
        self.data = []
        self.len = 0
    def append(self, data):
        self.len += 1
        self.data.append(data)
        
class Game:
    def __init__(self, surface, song_title, beat_type, num_sensors, instrument, config):
        self.bgColor = (150, 140, 255) 
        #bg blue = (120, 200, 255) 
        #bg purple = (180, 80, 255)
        
        self.score = 0
        self.multiplier = 1.0

        self.bgRect = (0,0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT) #x,y,width,height
        self.surface = surface

        self.sensor1 = entities.Tile(0,0, const.RED, 0)
        self.sensor2 = entities.Tile(0,0, const.GREEN, 0)
        self.sensor3 = entities.Tile(0,0, const.ORANGE, 0)
        self.sensor4 = entities.Tile(0,0, const.BLUE, 0)


        self.sensor1.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)
        self.sensor2.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)
        self.sensor3.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)
        self.sensor4.setDimensions(const.SENSOR_WIDTH, const.SENSOR_HEIGHT)

        self.sensor1.setPosition(const.SENSOR_OFFSET_LEFT, const.SENSOR_Y)
        self.sensor2.setPosition(const.SENSOR_OFFSET_LEFT + const.SENSOR_WIDTH * 1, const.SENSOR_Y)
        self.sensor3.setPosition(const.SENSOR_OFFSET_LEFT + const.SENSOR_WIDTH * 2, const.SENSOR_Y)
        self.sensor4.setPosition(const.SENSOR_OFFSET_LEFT + const.SENSOR_WIDTH * 3, const.SENSOR_Y)


        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.tiles1 = Array()
        self.tiles2 = Array()
        self.tiles3 = Array()
        self.tiles4 = Array()

        self.difficulty = config["DifficultyIndex"]
        if self.difficulty == 0:    #easy
            self.initTiles(song_title, beat_type, num_sensors, instrument, const.MIN_NOTE_DURATION_MED, const.MAX_SIMULTANEOUS_NOTES_EASY, const.TIME_BETWEEN_NOTES_EASY, const.SPEED_TILES_EASY)
        elif self.difficulty == 1: # medium
            self.initTiles(song_title, beat_type, num_sensors, instrument, const.MIN_NOTE_DURATION_MED, const.MAX_SIMULTANEOUS_NOTES_MED, const.TIME_BETWEEN_NOTES_MED, const.SPEED_TILES_MED)
        elif self.difficulty == 2: # hard
            self.initTiles(song_title, beat_type, num_sensors, instrument, const.MIN_NOTE_DURATION_HARD, const.MAX_SIMULTANEOUS_NOTES_HARD, const.TIME_BETWEEN_NOTES_HARD, const.SPEED_TILES_HARD)

    def getGameState(self):
        if self.tiles1.len > self.tiles1.front:
            return True
        if self.tiles2.len > self.tiles2.front:
            return True
        if self.tiles3.len > self.tiles3.front:
            return True
        if self.tiles4.len > self.tiles4.front:
            return True
        return False

    def checkTile(self, tile, sensorNum):
        if (tile.getPosition()[1] <= const.SENSOR_Y + 10) and ((tile.getPosition()[1] + tile.getDimensions()[1]) >= const.SENSOR_Y):
            if not tile.checkHit():
                tile.setHit()
                print(f"hit {sensorNum}")
                self.score += 100 * self.multiplier
                self.multiplier += 0.1
            return True
        return False


    def checkSensor(self, sensorNum):
        print(f"checking {sensorNum}")
        hit = False
        match sensorNum:
            case 1:
                for tile in self.tiles1.data:
                    if self.checkTile(tile, 1):
                        hit = True
                        break
            case 2:
                for tile in self.tiles2.data:
                    if self.checkTile(tile, 2):
                        hit = True
                        break

            case 3:
                for tile in self.tiles3.data:
                    if self.checkTile(tile, 3):
                        hit = True
                        break
            case 4:
                for tile in self.tiles4.data:
                    if self.checkTile(tile, 4):
                        hit = True
                        break
        if not hit:
            self.multiplier = 1.0
    
    def showBg(self, time):
        scal = math.sin(time/10)
        bgCol = (self.bgColor[0] + scal * -30, self.bgColor[1] + scal * 60, self.bgColor[2])
        print(self.bgColor)
        pygame.draw.rect(self.surface, bgCol, self.bgRect)
        
    def showSensor(self):
        pygame.draw.rect(self.surface, self.sensor1.colour, self.sensor1.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor2.colour, self.sensor2.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor3.colour, self.sensor3.getRectInfo())
        pygame.draw.rect(self.surface, self.sensor4.colour, self.sensor4.getRectInfo())

    def showTiles(self):
        for tile in self.tiles1.data:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))
        for tile in self.tiles2.data:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))
        for tile in self.tiles3.data:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))
        for tile in self.tiles4.data:
            pos = tile.getPosition()
            pygame.draw.rect(self.surface, tile.colour, (pos[0],pos[1], tile.width, tile.height))

    def showScore(self):
        score = self.font.render(f"Score: {int(self.score)}", True, const.GREEN)
        self.surface.blit(score, ((const.SCREEN_WIDTH / 2) - (score.get_width() / 2), 5))

    def draw(self, time):
        self.showBg(time)
        self.showTiles()
        self.showSensor()
        self.showScore()
      
    def updateTiles(self, dt):
        update = 0
        for i in range(self.tiles1.front, self.tiles1.len):
            self.tiles1.data[i].updatePos(dt)
            update += 1
        for i in range(self.tiles2.front, self.tiles2.len):
            self.tiles2.data[i].updatePos(dt)
            update += 1
        for i in range(self.tiles3.front, self.tiles3.len):
            self.tiles3.data[i].updatePos(dt)
            update += 1
        for i in range(self.tiles4.front, self.tiles4.len):
            self.tiles4.data[i].updatePos(dt)
            update += 1
        print("TILES MOVED PER FRAME:", update)
    
    def initTiles(self, midifile, beat_type, num_sensors, instrument, min_note_duration, max_sim_notes, time_bn_notes, speed_tiles):
        data = get_beats.return_keys_assignments_and_populate_json(midifile=midifile, beat_type=beat_type, num_sensors=num_sensors, instrument=instrument, min_note_duration=min_note_duration, max_simultaneous_notes=max_sim_notes, time_between_notes=time_bn_notes)

        for i in range(4):
            for d in data[i]:
                if i == 0:
                    self.tiles1.append(entities.Tile(const.SPAWN_1, d["start_time"] + 0.5 * d["duration"], const.LIGHT_RED, d['duration'], speed_tiles))
                if i == 1:
                    self.tiles2.append(entities.Tile(const.SPAWN_2, d["start_time"] + 0.5 * d["duration"], const.LIGHT_GREEN, d['duration'], speed_tiles))
                if i == 2:
                    self.tiles3.append(entities.Tile(const.SPAWN_3, d["start_time"] + 0.5 * d["duration"], const.LIGHT_ORANGE, d['duration'], speed_tiles))
                if i == 3:
                    self.tiles4.append(entities.Tile(const.SPAWN_4, d["start_time"] + 0.5 * d["duration"], const.LIGHT_BLUE, d['duration'], speed_tiles))
