import pygame
import time

import entities
import const
from game import Game
import startScreen

from midi2audio import FluidSynth

OPEN_START_SCREEN = True

def main():
    pygame.init()
    
    running = False
    if (OPEN_START_SCREEN):
        gameConfig = startScreen.invokeStartScreen()
        running = gameConfig["StartGameTrue"]
    else:
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
        
        game.updateTiles(dt)
        
        #check if tile is below sensor -> if it is then increment front
        f1 = game.tiles1
        if (f1.front <  f1.len) and f1.data[f1.front].pos[1] > const.SCREEN_HEIGHT:
            f1.front += 1
        f2 = game.tiles2
        if (f2.front <  f2.len) and f2.data[f2.front].pos[1] > const.SCREEN_HEIGHT:
            f2.front += 1
        f3 = game.tiles3
        if (f3.front <  f3.len) and f3.data[f3.front].pos[1] > const.SCREEN_HEIGHT:
            f3.front += 1
        f4 = game.tiles4
        if (f4.front <  f4.len) and f4.data[f4.front].pos[1] > const.SCREEN_HEIGHT:
            f4.front += 1
            
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