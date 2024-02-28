import pygame
import random
from typing import List
import time

class Bug:
    def __init__(self, screen: pygame.Surface, 
                 init_x: int, init_y: int = 0, 
                 speed_y: int = 3) -> None:
        self.pos_x = init_x
        self.pos_y = init_y
        self.speed_y = speed_y
        self.screen = screen
        self.radius = 3.0 # TODO: might replace this when real bug draw is ready

    def show(self):
        pygame.draw.circle(self.screen, (255,255,255), (self.pos_x, self.pos_y), self.radius)

    def update(self):
        self.pos_y += self.speed_y

class BugManager:
    def __init__(self, screen: pygame.surface, height) -> None:
        self.bugs: List[Bug] = []
        self.screen = screen
        self.height = height
        self.previouse_spawn = time.time()

    def spawn_bug(self, limit_left: int, limit_right: int):
        self.bugs.append(Bug(self.screen, random.randint(limit_left,limit_right),-3,3))

    def update(self, limit_left: int, 
               limit_right: int, 
               player_x: int, player_y: int,
               player_w: int, player_h: int):
        if time.time() - self.previouse_spawn > 0.5:
            self.spawn_bug(limit_left, limit_right)
            self.previouse_spawn = time.time()

        for b in self.bugs:
            b.update()
            print(len(self.bugs))
            if (abs(player_x - b.pos_x) < (player_w/2 + b.radius) 
                and abs(player_y - b.pos_y) < (player_h/2 + b.radius)):
                return True
        self.bugs = [b for b in self.bugs if b.pos_y < self.height]
        return False

    def show(self):
        for b in self.bugs:
            b.show()