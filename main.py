# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    updatable = pygame.sprite.Group() # 7)
    drawable = pygame.sprite.Group() # 7)
    Player.containers = (updatable, drawable) # 7)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y) # 1) 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # print(f"Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        # player.update(dt) # 4)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen) 
        # player.draw(screen) # 3)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # 6)
        


if __name__ == "__main__":
    main()

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