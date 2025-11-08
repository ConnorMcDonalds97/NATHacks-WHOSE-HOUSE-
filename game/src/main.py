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
        
        game.showBg()
        game.showSensor(game.sensorSmall, 'red')
        game.showTiles()

        for tile in game.tiles:
            print(tile)
            tile.updatePos(deltaTime)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.showSensor(game.sensorBig, 'white')
            elif event.type == pygame.KEYUP:
                pass

        pygame.display.update()

    pygame.quit()

main()