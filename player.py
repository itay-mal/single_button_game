import pygame

class Player:
    def __init__(self, screen: pygame.Surface, 
                 init_x: int, init_y: int, 
                 speed_x: int = 3) -> None:
        self.pos_x = init_x
        self.pos_y = init_y
        self.speed_x = speed_x
        self.screen = screen
        self.width = 5
        self.height = 10

    def show(self):
        rect = pygame.Rect(self.pos_x - self.width / 2, 
                           self.pos_y - self.height/2, 
                           self.width, 
                           self.height)
        pygame.draw.rect(self.screen, (255,255,255), rect)

    def update(self):
        self.pos_x += self.speed_x
    
    def change_direction(self):
        self.speed_x *=-1