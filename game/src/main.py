import pygame
import entities
import const
import time

from game import Game


def main():
    pygame.init()


    clock = pygame.time.Clock()
    
    running = True

    game = Game(pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT)))

    prevTime = time.time()
    dt = 0
    timer = 0
    while running:
        game.draw()

        now = time.time()
        dt = now - prevTime
        prevTime = now

        timer += dt

        for tile in game.tiles:
            tile.updatePos(dt)
        game.setBack()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                    # game.sensor.setColour("red")
            elif event.type == pygame.KEYUP:
                pass
                    # game.sensor.setColour("white")
        pygame.display.update()

    pygame.quit()

main()