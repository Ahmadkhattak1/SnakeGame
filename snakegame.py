# main.py
import pygame
import sys
import settings
from food import Food

# Initializing Pygame
pygame.init()

# Creating a screen (Size is set in the settings.py file)
screen = pygame.display.set_mode(settings.screen_size)

# Initializing Food Object
food_instance = Food()
food_surface = pygame.image.load("Game_graphics\\food.png")

# Screen Title
pygame.display.set_caption("Snake Game")

# clock object that controls the speed
clock = pygame.time.Clock()

# Game loop starts here
while True:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Drawing on the screen
    screen.fill(settings.background_color)
    food_instance.draw(screen, food_surface)
    
    pygame.display.update()
    
    # FPS
    clock.tick(settings.fps)
