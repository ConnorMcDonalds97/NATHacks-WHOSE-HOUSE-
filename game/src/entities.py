import pygame
import const

class Tile():
    def __init__(self, posX, time, colour, duration = 0.18, velocity=100):
        self.isHit = False
        self.vel = pygame.Vector2(0,velocity)
        self.width = const.TILE_WIDTH
        self.height = const.TILE_HEIGHT * duration

        posY = const.SCREEN_HEIGHT - time * self.vel[1]
        
        self.pos = pygame.Vector2(posX,posY)
        self.originalPos = pygame.Vector2(posX, posY)
        self.colour = colour

        self.duration = duration

    def __str__(self):
        return f"Pos: {self.pos}\nVel: {self.vel}\nWidth: {self.width}\nHeight: {self.height}"

    def calculateCentreScreenX(self, screenWidth):
        return (screenWidth)/2 - (self.width/2)
    
    # Setters
    def setColour(self, colour):
        self.colour = colour

    def setVelocity(self, x: float, y: float):
        self.vel = pygame.Vector2(x,y)

    def setPosition(self, x: float, y: float):
        self.pos = pygame.Vector2(x,y)

    def setDimensions(self, width: int, height: int):
        self.width = width
        self.height = height

    def setPosXToCentre(self, screenWidth):
        self.pos = pygame.Vector2((screenWidth / 2) - (self.width / 2), self.pos.y)

    def setHit(self):
        self.isHit = True
        self.setColour(const.WHITE)

    '''
    Updates position based on velocity * deltaTime
    '''
    def updatePos(self, time):
        self.pos = self.originalPos + self.vel * time

    # Getters
    def getColour(self):
        return self.colour

    def getVelocity(self):
        return self.vel
    
    def getPosition(self):
        return self.pos
    
    def getDimensions(self):
        return (self.width, self.height)
    
    def getRectInfo(self):
        return (self.pos[0], self.pos[1], self.width, self.height)
    
    def checkHit(self):
        return self.isHit
    
