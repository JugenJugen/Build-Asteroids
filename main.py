from player import Player
import pygame
from constants import *
from logger import log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import *
import sys



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        screen.fill("black")
        updatable.update(dt)

        for aste in asteroids:
            if aste.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for sho in shots:
                if sho.collides_with(aste):
                    log_event("asteroid_shot")
                    sho.kill()
                    aste.split()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()




    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
