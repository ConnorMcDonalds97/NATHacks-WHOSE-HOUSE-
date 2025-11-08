import pygame

class Tile():
    def __init__(self, width, height):
        self.posX = 0
        self.posY = 0
        self.width = 0
        self.height = 0
        self.vel = [0,0]

    def calculateCentreScreenX(self, screenWidth):
        return (screenWidth)/2 - (self.width/2)

    def teleport(self, x, y):
        pass

    def setVelocity(self, x, y):
        pass

    def getVelocity(self):
        pass

    def updatePos(self, delta_time):
        self.posX = self.vel[0] * delta_time
        self.posY = self.vel[1] * delta_time