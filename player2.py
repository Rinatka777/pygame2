# player2.py
import pygame
# Import the CircleShape class from CircleShape.py
from circleshape2 import CircleShape
from constants2 import *
from shot import Shot

class Player(CircleShape):
    containers = None  # This will be set from main2.py
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Create a field called rotation, initialized to 0
        self.rotation = 0
    def rotate (self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self, dt):
        # Implement movement logic here
        # Example: Move in the direction the player is facing
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = direction * PLAYER_SPEED * dt  # SPEED should be defined in your constants
        self.position += velocity

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left by inverting dt
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right normally
        if keys[pygame.K_w]:
            self.move (dt)
        if keys[pygame.K_s]:
            self.move (-dt)
        if keys[pygame.K_SPACE]:
            return self.shoot()
        
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
    def shoot(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)  # Direction the player is facing
        # Create a new shot at the player's current position
        shot_position = self.position + forward * (self.radius + SHOT_RADIUS)  # Adjust to the tip of the triangle

        # Set the shot's velocity
        shot_velocity = pygame.Vector2(0, -1)  # Start with vector pointing up
        shot_velocity = shot_velocity.rotate(self.rotation)  # Rotate it based on player rotation
        shot_velocity *= PLAYER_SHOOT_SPEED  # Scale up by the player's shooting speed

        # Create the shot
        new_shot = Shot(shot_position.x, shot_position.y, shot_velocity)

        return new_shot 


