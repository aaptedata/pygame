# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid # 8)
from asteroidfield import AsteroidField # 9)
from shot import Shot # CORRECT
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group() # 7)
    drawable = pygame.sprite.Group() # 7)
    asteroids = pygame.sprite.Group() # 8)
    shots = pygame.sprite.Group() # CORRECT
    
    Asteroid.containers = (asteroids, updatable, drawable) # 8)
    AsteroidField.containers = updatable # 9) no need for () with one
    asteroid_field = AsteroidField() # 9)
    
    Shot.containers = (shots, updatable, drawable) # CORRECT
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updatable, drawable) # 7)
    player = Player(x,y) # 1) 2)
    
    dt = 0
    
    # print(f"Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids: # 10)
            if asteroid.collides_with(player):
                print(f"Game over")
                sys.exit() # 10) window closes, game is over
            for shot in shots:
                if asteroid.collides_with(shot):
                    # asteroid.kill() # 11)
                    shot.kill() # 11)
                    asteroid.split()
        # player.update(dt) # 4)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen) 
        # player.draw(screen) # 3)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # 6)
        


if __name__ == "__main__":
    main()

# ENDNOTES
# 1) In your main function, instantiate a Player object. 
# 2) You can pass these values to the constructor to spawn it in the middle of the screen:
# x = SCREEN_WIDTH / 2
# y = SCREEN_HEIGHT / 2
# 3) Lastly, we need to re-render the player on the screen each frame, meaning inside our 
# game loop. Use the player.draw(screen) method we just added to do so.
# 4) Hook the update method into the game 
# loop by calling it on the player object each frame before rendering.
# 5) Change the game loop to use the new groups instead of the Player object directly.
# Call the .update() method on the "updatables" group.
# Loop over all "drawables" and .draw() them individually.
# 6) Instead of thinking of clock.tick() as stopping a timer, think of it as a function that does two main things in one go:
# It pauses the program until enough time has passed to maintain the desired frame rate (in this case, 60 frames per second).
# It then tells you how long that pause was, plus the time it took for the code to execute since the last time tick() was called.
# 7) Using groups allows you to:
# Update multiple objects with a single line (updatable.update(dt)).
# Draw multiple objects easily by iterating through the drawable group.
# Organize objects based on their behavior or type (e.g., enemies, projectiles, collidable_objects).
# This keeps your game loop much cleaner and makes it easier to manage a growing number of game elements.
# 8) In the initialization code in main (before the game loop starts), 
# create a new pygame.sprite.Group which will contain all of the asteroids. 
# Like we did with the Player class, set the static containers field of the Asteroid 
# class to the new asteroids group, as well as the updatable and drawable groups.
# 9) In the main.py file, set the static containers field of the AsteroidField class to only the updatable 
# group (it's not drawable, and it's not an asteroid itself). 
# Create a new AsteroidField object in the initialization code.
# 10) After the update step in your game loop, iterate over all of the objects in your asteroids group. 
# Check if any of them collide with the player. 
# If a collision is detected, the program should print Game over! and immediately exit the program.
# 11)  kill() is a method that's built into pygame.sprite.Sprite