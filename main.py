import pygame

from asteroid import Asteroid
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT,
ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MIN_RADIUS)
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(200)/1000

if __name__ == "__main__":
    main()
