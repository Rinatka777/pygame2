import pygame
# Import all constants from constants2
# Import specific constants from constants2
from constants2 import *
from player2 import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
def main():
     # Initialize Pygame
    pygame.init()

    # Print statements
    print("Starting asteroids!")
    print("Screen width: {}".format(SCREEN_WIDTH))
    print("Screen height: {}".format(SCREEN_HEIGHT))

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create groups for updatables and drawables
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set Player's containers to the groups
    Player.containers = (updatable, drawable)
    # Set AsteroidField's containers to only the updatable group
    AsteroidField.containers = (updatable)
    # Instantiate a Player object in the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

     # Create an AsteroidField object (without adding initial asteroids)
    asteroid_field = AsteroidField()

    # Add the AsteroidField to the updatable group (it's not drawable)
    updatable.add(asteroid_field)
     # Create a new pygame.time.Clock object
    clock = pygame.time.Clock()

     # Set the dt (delta time) variable to 0
    dt = 0
    # Create a group for asteroids
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # Update all objects in the updatable group
        for obj in updatable:
            # Manually call update with dt since Group.update() doesn't pass parameters
            obj.update(dt)
        # After updating, check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()  # Immediately exit the program

    # Fill the screen with black color
        screen.fill((0, 0, 0))
    # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)
    # Draw the player on the screen
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()