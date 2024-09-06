# player2.py
import pygame
# Import the CircleShape class from CircleShape.py
from circleshape2 import CircleShape
from constants2 import PLAYER_RADIUS
class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Create a field called rotation, initialized to 0
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Add the draw method here
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)