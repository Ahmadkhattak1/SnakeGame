# main.py
import pygame
import sys
import settings
from food import Food
from snake import Snake
from pygame.math import Vector2
import game

# Initializing Pygame
pygame.init()

# Creating a screen (Size is set in the settings.py file)
screen = pygame.display.set_mode(settings.screen_size)

# Initializing Food and Snake Objects
game = game.Game()
food_surface = pygame.image.load("Game_graphics\\food.png")
snake_update = pygame.USEREVENT
pygame.time.set_timer(snake_update, settings.snake_speed)

# Screen Title
pygame.display.set_caption("Snake Game")

# clock object that controls the speed
clock = pygame.time.Clock()

# Game loop starts here
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == snake_update:
            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)
                
    
    
    # Drawing on the screen
    screen.fill(settings.background_color)
    game.draw_elements(screen, food_surface)
    pygame.display.update()
    
    # FPS
    clock.tick(settings.fps)
