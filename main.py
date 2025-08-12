import pygame
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT,
ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MIN_RADIUS)

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
