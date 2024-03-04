import random
import time
from bitmaps import bug_bmp

class Bug:
    def __init__(self, screen: pygame.Surface, 
                 init_x: int, init_y: int = 0, 
                 speed_y: int = 3) -> None:
        self.pos_x = init_x
        self.pos_y = init_y
        self.speed_y = speed_y
        self.screen = screen
        self.radius = 3 # TODO: might replace this when real bug draw is ready

    def show(self):
        self.draw_bug(self.pos_x - 4, self.pos_y - 4)
        
    def update(self):
        self.pos_y += self.speed_y
    
    def draw_bug(self, top_x, top_y):
        for x,y in bug_bmp:
            self.screen.pixel(x + top_x, y + top_y,1)

    
    
class BugManager:
    def __init__(self, screen: pygame.surface, height) -> None:
        self.bugs = []
        self.screen = screen
        self.height = height
        self.previouse_spawn = time.time()
        self.spawn_freq = 1

    def spawn_bug(self, limit_left: int, limit_right: int):
        self.bugs.append(Bug(self.screen, random.randint(limit_left,limit_right),-3,3))

    def update(self, limit_left: int, 
               limit_right: int, 
               player_x: int, player_y: int,
               player_w: int, player_h: int):
        if time.time() - self.previouse_spawn > self.spawn_freq:
            self.spawn_bug(limit_left, limit_right)
            self.previouse_spawn = time.time()

        for b in self.bugs:
            b.update()
            if (abs(player_x - b.pos_x) < (player_w/2 + b.radius) 
                and abs(player_y - b.pos_y) < (player_h/2 + b.radius)):
                return True
        self.bugs = [b for b in self.bugs if b.pos_y < self.height]
        return False

    def show(self):
        for b in self.bugs:
            b.show()
            
