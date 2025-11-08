import pygame

class Tile():
    def __init__(self, width, height):
        self.pos = pygame.Vector2(0,0)
        self.vel = pygame.Vector2(0,0)
        self.width = 0
        self.height = 0

    def calculateCentreScreenX(self, screenWidth):
        return (screenWidth)/2 - (self.width/2)

    def setPosition(self, x, y):
        self.pos = pygame.Vector2(x,y)

    def setVelocity(self, x, y):
        self.vel = pygame.Vector2(x,y)

    '''
    Updates position based on velocity * deltaTime
    '''
    def updatePos(self, deltaTime):
        self.pox += self.vel * deltaTime

    def getVelocity(self):
        return self.vel
    
    def getPosition(self):
        return self.pos