import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # CORRECT 1)
        # self.x = x
        # self.y = y
        # self.radius = radius
        
        
    def draw(self, screen):
        # pygame.draw.polygon(screen, "white", self.triangle(), 2)
        # pygame.draw.circle(screen, "white", (self.x, self.y), 2)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt) # CORRECT 3)
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20.0, 50.0) # Random angle
        a = self.velocity.rotate(random_angle) # New angle a
        b = self.velocity.rotate(-random_angle) # New angle b
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # asteroid1 = pygame.Vector2(0, 1).rotate(self.random_angle)
        # asteroid2 = pygame.Vector2(0, 1).rotate(-self.random_angle)
        
        # New Asteroid a
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        # New Asteroid b
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
            
            
        
        
# ENDNOTES        
# 1) Add a constructor with this signature:
# def __init__(self, x, y, radius):
# 2) Override the draw() method to draw the asteroid as a pygame.draw.circle. 
# Use its position, radius, and a width of 2
# 3) Override the update() method so that it moves in a straight line at constant speed. 
# On each frame, it should add (self.velocity * dt) to its position 
# (get self.velocity from its parent class, CircleShape).