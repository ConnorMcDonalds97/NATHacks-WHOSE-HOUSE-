import pygame
import entities
import const

from game import Game


def main():
    pygame.init()


    clock = pygame.time.Clock()
    running = True

    game = Game(pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT)))

    while running:
        # clock.tick returns milliseconds
        deltaTime = clock.tick(60) / 1000.0

        for tile in game.tiles:
            # print(tile)
            tile.updatePos(deltaTime)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.sensor.setColour("red")
            elif event.type == pygame.KEYUP:
                    game.sensor.setColour("white")
        game.draw()

        pygame.display.update()

    pygame.quit()

main()