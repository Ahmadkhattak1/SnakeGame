# food.py
import settings
import pygame
from pygame.math import Vector2
import random

class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)

    def draw(self, screen, food_surface):
        food_rect = pygame.Rect(self.position.x * settings.cell_size, self.position.y * settings.cell_size, settings.cell_size, settings.cell_size)
        screen.blit(food_surface, food_rect)

    def generate_random_position(self):
        x = random.randint(0, settings.number_of_cells-1)
        y = random.randint(0, settings.number_of_cells-1)
        return Vector2(x, y)
    
    def random_position(self, snake_body):
        position = self.generate_random_position()
        
        while position in snake_body:
            position = self.generate_random_position()
            return position
        
        return position