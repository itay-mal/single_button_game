import time
from bitmaps import cat_1_l_bmp, cat_2_l_bmp, cat_1_r_bmp, cat_2_r_bmp
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
        self.bmp_type = 0
        self.bmp_last_update = time.ticks_ms()
        self.bmps = [cat_1_l_bmp, cat_2_l_bmp, cat_1_r_bmp, cat_2_r_bmp] 

    def show(self):
        self.draw_cat(self.pos_x - self.width // 2,
                      self.pos_y - self.height//2,
                      self.bmps[((self.speed_x > 0) << 1) | (self.bmp_type)])

    def update(self):
        self.pos_x += self.speed_x
        if time.ticks_ms() - self.bmp_last_update > 700:
            self.bmp_type = 1-self.bmp_type
            self.bmp_last_update = time.ticks_ms()
        
    
    def change_direction(self):
        self.speed_x *=-1
        
    def draw_cat(self, top_x, top_y, bitmap):
        for x,y in bitmap:
            self.screen.pixel(x+top_x,y+top_y,1)
