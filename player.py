import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
# import math


class Player(CircleShape): # 1)
    def __init__(self, x, y): # 2)
        super().__init__(x, y, PLAYER_RADIUS) # 3)
        self.rotation = 0 # 4)
        self.shoot_timer = 0 # shoot_timer instead of timer, clearer

    def draw(self, screen): # 5)
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # 6) - 8)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt): # 8) 9)
        self.rotation += (PLAYER_TURN_SPEED * dt) # 10)
        
    def move(self, dt, direction = 1):
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED * dt
        # forward is a vector object that allows addition and scalar mult
        
        # theta = math.radians(self.rotation - 90)
        # x = direction * PLAYER_SPEED * dt * math.cos(theta)
        # y = direction * PLAYER_SPEED * dt * math.sin(theta)
        # self.position[0] += x
        # self.position[1] += y
        
    def update(self, dt): # Copy / Paste
        self.shoot_timer -= dt # Put at beginning
        keys = pygame.key.get_pressed() # keyboard input pygame.K_a is the a key

        if keys[pygame.K_a]:
            self.rotate(-dt) # 11)
        if keys[pygame.K_d]:
            self.rotate(dt) # 11)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt, -1)
        if keys[pygame.K_SPACE]:
            # self.shoot(dt)
            self.shoot() # 13)
        
            
    def shoot(self): # 12)
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN # CORRECT WRONG ORDER
        # shot = Shot(self.position)
        shot = Shot(self.position.x, self.position.y)
        # shot.position = pygame.Vector2(0, 1).rotate(self.rotation)
        # shot.position += PLAYER_SHOOT_SPEED * dt
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
        
        

# ENDNOTES
# 1) Create a new file called player.py with a Player class that inherits from CircleShape.
# 2) The Player constructor should take x and y integers as input, then:
# 3) Call the parent class's constructor, also passing in PLAYER_RADIUS
# 4) Create a field called rotation, initialized to 0
# 5) To draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon. It takes:
# The screen object
# 6) A color (use "white")
# 7) A list of points (use self.triangle() that we provided for you)
# A line width (use 2)
# 8) Add a new method to the Player class called rotate. 
# 9) It's going to take one argument: dt (I told you we'd use it!). 
# 10) When it's called, it should add PLAYER_TURN_SPEED * dt to the player's current rotation.
# 11) Update the missing lines to call the rotate method with the dt argument. 
# To go left instead of right when a is pressed, you'll need to reverse dt... how can you do that...?
# Now, about your observation that this vector can be added to self.position directly, you are 
# also on the right track! self.position is also a pygame.Vector2, and Pygame's vector objects 
# allow for direct addition and multiplication like you've shown with 
# self.position += direction * forward * PLAYER_SPEED * dt. It's quite convenient 
# for handling positions and movements in 2D space.
# 12) In your Player class, add a new method called shoot. This method should:
# Create a new shot at the position of the player
# Set the shot's velocity:
# Start with a pygame.Vector2 of (0, 1) - a vector pointing "up"
# .rotate() it in the direction the player is facing by self.rotation
# Scaling it up by PLAYER_SHOOT_SPEED to make it move at the right speed
# 13) Inside your Player class, handle the spacebar (pygame.K_SPACE) 
# and call the shoot method when it is pressed.

