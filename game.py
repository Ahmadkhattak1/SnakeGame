import pygame, sys
import settings
from food import Food
from snake import Snake

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        
    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self, screen, food_surface):
        self.food.draw(screen, food_surface)
        self.snake.draw(screen)
    
    def check_collision(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.random_position(self.snake.body)
            self.snake.add_block = True
        
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < settings.number_of_cells or not 0 <= self.snake.body[0].y < settings.number_of_cells:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    def game_over(self):
        self.snake.reset()
        