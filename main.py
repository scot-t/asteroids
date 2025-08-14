import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    clock = pygame.time.Clock()
    dt = 0 # seconds
    fps = 60 # int


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()


    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print(f"Game over!")
                return
                # exit()
            for shot in shots:
                if asteroid.colliding(shot):
                    shot.kill()
                    asteroid.split()



    
        screen.fill("pink")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 fps
        dt = clock.tick(fps) / 1000

if __name__ == "__main__":
    main()
