import pygame

class Tile():
    def __init__(self, width, height, posX, posY):
        self.pos = pygame.Vector2(posX,posY)
        self.vel = pygame.Vector2(0,100)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Pos: {self.pos}\nVel: {self.vel}\nWidth: {self.width}\nHeight: {self.height}"

    def calculateCentreScreenX(self, screenWidth):
        return (screenWidth)/2 - (self.width/2)
    


    # Setters

    def setVelocity(self, x: float, y: float):
        self.vel = pygame.Vector2(x,y)

    def setPosition(self, x: float, y: float):
        self.pos = pygame.Vector2(x,y)

    def setDimensions(self, width: int, height: int):
        self.width = width
        self.height = height

    def setPosXToCentre(self, screenWidth):
        self.pos = pygame.Vector2((screenWidth / 2) - (self.width / 2), self.pos.y)

    '''
    Updates position based on velocity * deltaTime
    '''
    def updatePos(self, deltaTime):
        self.pos += self.vel * deltaTime

    # Getters

    def getVelocity(self):
        return self.vel
    
    def getPosition(self):
        return self.pos
    
    def getDimensions(self):
        return (self.width, self.height)
    
def main():
    print("testing tile")
    tile = Tile(1000,0)
    print(tile)
    tile.setPosition(100,100)
    print(tile.getPosition())
    tile.setVelocity(5,0)
    print()

if __name__ == "__main__":
    main()
