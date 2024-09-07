#asteroid.py
import pygame
from circleshape2 import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        # Call the parent class's constructor to initialize position and radius
        super().__init__(x, y, radius)

        self.velocity = pygame.Vector2(velocity)

    def update(self, dt):
        # Update the position by adding (velocity * dt) to the current position
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw the asteroid on the screen using a circle shape
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, 2)