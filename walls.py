import pygame
from typing import List

class WallManager:
    def __init__(self, screen:pygame.Surface,
                 screen_height: int, screen_width: int, 
                 wall_height: int = 6, wall_speed: int = 3) -> None:
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.wall_height = wall_height
        self.wall_speed  = wall_speed
        self.walls: List[Wall] = []
    
    def show(self):
        for w in self.walls:
            w.show()
    
    def update(self):
        for w in self.walls:
            w.update()

class Wall:
    def __init__(self, screen:pygame.Surface, x_left: int, x_right: int, 
                 height: int = 6, speed: int = 3) -> None:
        self.screen = screen
        self.y_top = -height
        self.x_left = x_left
        self.x_right = x_right
        self.height = height
        self.speed = speed

    def show(self):
        rect = pygame.Rect(self.x_left,self.y_top,
                           self.x_right-self.x_left,self.height)
        pygame.draw.rect(self.screen, (255,255,255), rect)
    
    def update(self):
        self.y_top += self.speed