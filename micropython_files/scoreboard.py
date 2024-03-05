import time
from font import Font
from beeper import extra_life_buzz, life_lost_buzz
from bitmaps import heart_bmp
import array

class ScoreBoard:
    def __init__(self, screen,
                 initial_lives: int = 3, 
                 initial_score: int = 0,
                 screen_width: int = 128) -> None:
        self.screen = screen
        self.lives = initial_lives
        self.score = initial_score
        self.box_width = 30
        self.box_height = 10
        self.last_score_add = time.time()
        self.screen_width = screen_width
        self.f = Font(screen)
        self.bug_coll_p = False
        self.extra_life_coll_p = False

    def show(self) -> None:
        # lives
        self.screen.fill_rect(0, 0, self.box_width, self.box_height, 0)
        for i in range(self.lives):
            self.draw_heart((i*self.box_width)//3, 0)

        # score
        self.screen.fill_rect(self.screen_width - self.box_width, 0, self.box_width, self.box_height,0)
        self.f.text(f"{self.score:05}", 128-self.box_width-10,0, 10)
        
    def update(self, wall_coll:bool, bug_coll:bool, extra_life_coll) -> bool:
        if bug_coll and not self.bug_coll_p:
            self.lives -= 1
            life_lost_buzz()
        if extra_life_coll and not self.extra_life_coll_p:
            self.lives += self.lives < 3
            extra_life_buzz()
        
        self.bug_coll_p = bug_coll
        if time.time() - self.last_score_add > 1:
            self.score += 1
            self.last_score_add = time.time()
        return not self.lives or wall_coll

    def draw_heart(self, top_x, top_y):
        for x,y in heart_bmp:
            self.screen.pixel(top_x + x, top_y + y,1)