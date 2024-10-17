# player2.py
import pygame
# Import the CircleShape class from CircleShape.py
from circleshape2 import CircleShape
from constants2 import *
from shot import Shot
import math

class Player(CircleShape):
    
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Create a field called rotation, initialized to 0
        self.radius = 20
        self.rotation = 0
        self.shoot_timer = 0  # Timer starts at 0, meaning player can shoot immediately
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
        
        # Decrease the shoot timer by dt to gradually count down
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

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
        # Only allow shooting if the shoot timer is <= 0
        if self.shoot_timer <= 0:
            # Reset the shoot timer to the cooldown value
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

            # Set the shot's initial position to the player's current position
            shot_position = self.position

            # Set the shot's velocity to move forward in the direction the player is facing
            shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

            # Debugging: Output shot creation details
            print(f"Shot fired! Position: {shot_position}, Velocity: {shot_velocity}, Rotation: {self.rotation}")

            # Create and return the shot
            new_shot = Shot(shot_position.x, shot_position.y, shot_velocity)
            return new_shot

        # If the timer hasn't reached 0 yet, no shot is fired
        return None








