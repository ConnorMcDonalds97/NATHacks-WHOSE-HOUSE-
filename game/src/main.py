import pygame
import entities
import const
import time

from game import Game

from midi2audio import FluidSynth


def main():
    pygame.init()
    
    running = True

    game = Game(pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT)))
    game.draw()

    clock = pygame.time.Clock()

    dt = 0
    timer = 0
    while running:
        game.draw()

        dt = clock.tick(60)/1000.0

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
                    game.sensor1.setColour(const.WHITE)
                    game.checkSensor(1)
                if event.key == pygame.K_2:
                    game.sensor2.setColour(const.WHITE)
                    game.checkSensor(2)
                if event.key == pygame.K_3:
                    game.sensor3.setColour(const.WHITE)
                    game.checkSensor(3)
                if event.key == pygame.K_4:
                    game.sensor4.setColour(const.WHITE)
                    game.checkSensor(4)
                    # game.sensor.setColour("red")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    game.sensor1.setColour(const.RED)
                if event.key == pygame.K_2:
                    game.sensor2.setColour(const.GREEN)
                if event.key == pygame.K_3:
                    game.sensor3.setColour(const.ORANGE)
                if event.key == pygame.K_4:
                    game.sensor4.setColour(const.BLUE)

                    # game.sensor.setColour("white")
        pygame.display.update()

    pygame.quit()

main()