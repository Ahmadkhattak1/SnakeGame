import settings, pygame
from pygame.math import Vector2
import pygame
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_block = False
    
    def draw(self, screen):
        for block in self.body:
            x_pos = int(block.x * settings.cell_size)
            y_pos = int(block.y * settings.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, settings.cell_size, settings.cell_size)
            pygame.draw.rect(screen, settings.snake_color, block_rect, 0,8)
        
    def move(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_block:
            self.add_block = False
        else:
            self.body = self.body[:-1]
        
    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_block = False
