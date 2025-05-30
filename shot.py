import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    
    # def __init__(self, x, y, radius):
        # super().__init__(x, y, radius=SHOT_RADIUS) # 1)
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS) # 1)
        # Don't need radius = SHOT_RADIUS
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 
        
    def update(self, dt):
        self.position += (self.velocity * dt) 
        # if not screen.get_rect().collidepoint(self.rect.center):
        #     self.kill()
        
# CORRECT

# 1) Create a new Shot class to represent a bullet. It should also inherit from 
# CircleShape so that it can use our collision detection code. It should look 
# very similar to our Asteroid class in that it will be drawn and have its 
# position updated. Use a new SHOT_RADIUS constant and set it to 5.