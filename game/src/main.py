import pygame
import entities
import const
import time

from game import Game


def main():
    pygame.init()


    
    running = True

    game = Game(pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT)))
    game.draw()

    prevTime = time.time()
    dt = 0
    timer = 0
    while running:
        game.draw()

        now = time.time()
        dt = now - prevTime
        prevTime = now

        timer += dt

        for tile in game.tiles1:
            tile.updatePos(dt)
        for tile in game.tiles2:
            tile.updatePos(dt)
        for tile in game.tiles3:
            tile.updatePos(dt)
        for tile in game.tiles4:
            tile.updatePos(dt)
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game.sensor1.setColour('white')
                if event.key == pygame.K_2:
                    game.sensor2.setColour('white')
                if event.key == pygame.K_3:
                    game.sensor3.setColour('white')
                if event.key == pygame.K_4:
                    game.sensor4.setColour('white')
                    # game.sensor.setColour("red")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    game.sensor1.setColour('red')
                if event.key == pygame.K_2:
                    game.sensor2.setColour('green')
                if event.key == pygame.K_3:
                    game.sensor3.setColour('orange')
                if event.key == pygame.K_4:
                    game.sensor4.setColour('blue')

                    # game.sensor.setColour("white")
        pygame.display.update()

    pygame.quit()

main()