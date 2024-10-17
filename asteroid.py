#asteroid.py
import pygame
from circleshape2 import CircleShape
import random
from constants2 import *

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
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform (20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, velocity1 * 1.2)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, velocity2)