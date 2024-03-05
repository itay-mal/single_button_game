import random
import time
from bitmaps import bug_bmp, heart_bmp, expand_walls_bmp

class Collectible:
    def __init__(self, screen, bitmap, 
                 init_x: int, init_y: int = 0, 
                 speed_y: int = 3, radius: int = 4) -> None:
        self.pos_x = init_x
        self.pos_y = init_y
        self.speed_y = speed_y
        self.screen = screen
        self.bitmap = bitmap
        self.radius = radius
        
    def show(self):
        self.draw(self.pos_x - 4, self.pos_y - 4)
        
    def update(self):
        self.pos_y += self.speed_y
    
    def draw(self, top_x, top_y):
        for x,y in self.bitmap:
            self.screen.pixel(x + top_x, y + top_y,1)
    
class CollectibleManager:
    def __init__(self, screen, height, bitmap) -> None:
        self.instances = []
        self.screen = screen
        self.height = height
        self.previouse_spawn = time.time()
        self.bitmap = bitmap

    def spawn(self, limit_left: int, limit_right: int):
        self.instances.append(Collectible(self.screen, self.bitmap, 
                                          random.randint(limit_left,limit_right),
                                          -3,3))

    def update(self, limit_left: int, 
               limit_right: int, 
               player_x: int, player_y: int,
               player_w: int, player_h: int):
        # TODO: move spawining to external manager
        

        for inst in self.instances:
            inst.update()
            if (abs(player_x - inst.pos_x) < (player_w/2 + inst.radius) 
                and abs(player_y - inst.pos_y) < (player_h/2 + inst.radius)):
                self.instances.remove(inst)
                return True
        self.instances = [i for i in self.instances if i.pos_y < self.height]
        return False

    def show(self):
        for i in self.instances:
            i.show()

class MultiCollectibleManager:
    def __init__(self, screen, height) -> None:
        self.screen = screen
        self.height = height
        self.previouse_spawn = time.ticks_ms()
        self.spawn_freq = 1000
        self.managers = [
            CollectibleManager(self.screen, self.height, bug_bmp), # bug_manager
            CollectibleManager(self.screen, self.height, heart_bmp), # extra life manager
            CollectibleManager(self.screen, self.height, expand_walls_bmp), # expand walls manager
        ]

    
    def update(self, limit_left: int, 
               limit_right: int, 
               player_x: int, player_y: int,
               player_w: int, player_h: int):
        bug_coll = self.managers[0].update(limit_left,limit_right,player_x,player_y,player_w,player_h)
        extra_life_coll = self.managers[1].update(limit_left,limit_right,player_x,player_y,player_w,player_h)
        expand_walls_coll = self.managers[2].update(limit_left,limit_right,player_x,player_y,player_w,player_h)
        if time.ticks_ms() - self.previouse_spawn > self.spawn_freq:
            random.choice(self.managers).spawn(limit_left, limit_right)
            self.previouse_spawn = time.ticks_ms()
        return bug_coll, extra_life_coll, expand_walls_coll
        
    def show(self):
        for inst in self.managers:
            inst.show()
        
