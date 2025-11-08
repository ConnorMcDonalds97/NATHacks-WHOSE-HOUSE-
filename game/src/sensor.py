import pygame

class Tile():
    def __init__(self, width, height):
        self.posX = 0
        self.posY = 0
        self.width = 0
        self.height = 0

    def calculateCentreScreenX(self, screenWidth):
        return (screenWidth)/2 - (self.width/2)
    
    def updatePos(self, x, y):
