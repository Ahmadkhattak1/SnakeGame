# food.py
import settings
import pygame
from pygame.math import Vector2
import random

class Food:
    def __init__(self):
        self.position = self.random_position()

    def draw(self, screen, food_surface):
        food_rect = pygame.Rect(self.position.x * settings.cell_size, self.position.y * settings.cell_size, settings.cell_size, settings.cell_size)
        screen.blit(food_surface, food_rect)

    
    def random_position(self):
        x = random.randint(0, settings.number_of_cells-1)
        y = random.randint(0, settings.number_of_cells-1)
        
        position = Vector2(x,y)
        return position