import pygame
from circleshape2 import CircleShape
from constants2 import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        # Initialize the shot with position and radius
        super().__init__(x, y, SHOT_RADIUS)
        
        # Set the velocity for the shot
        self.velocity = velocity

    def update(self, dt):
        # Move the shot according to its velocity and delta time
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw the shot as a small circle
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius)

