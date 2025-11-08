from pickle import TRUE
import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

COLOURS = {
    "WHITE": (255,255,255),
    "RED": (255,0,0)
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # clock.tick returns milliseconds
        deltaTime = clock.tick(60) / 1000.0