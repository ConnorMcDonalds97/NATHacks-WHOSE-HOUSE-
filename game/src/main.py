from pickle import TRUE
import pygame
import tile

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

COLOURS = {
    "WHITE": (255,255,255),
    "RED": (255,0,0)
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# noteSensor = tile.Sensor(1000,10)


sensorPosX = (SCREEN_WIDTH/2) - (1000/2)
noteSensor = pygame.Rect((sensorPosX,600, 1000, 10))

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # clock.tick returns milliseconds
        deltaTime = clock.tick(60) / 1000.0

        pygame.draw.rect(screen, COLOURS["WHITE"], noteSensor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

main()