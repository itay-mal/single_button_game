import time
from font import Font
from beeper import buzz
import array

class ScoreBoard:
    def __init__(self, screen: pygame.Surface,
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

    def show(self) -> None:
        # lives
        self.screen.fill_rect(0, 0, self.box_width, self.box_height, 0)
        for i in range(self.lives):
            self.draw_heart((1+2*i)*self.box_width/6,
                            self.box_height/2,
                            self.box_height-2,
                            (self.box_width/3) - 2)

        # score
        self.screen.fill_rect(self.screen_width - self.box_width, 0, self.box_width, self.box_height,0)
        self.f.text(f"{self.score:05}", 128-self.box_width-10,0, 10)
        
    def update(self, wall_coll:bool, bug_coll:bool) -> bool:
        if bug_coll and not self.bug_coll_p:
            self.lives -= 1
            buzz(20,400,0)
        self.bug_coll_p = bug_coll
        if time.time() - self.last_score_add > 1:
            self.score += 1
            self.last_score_add = time.time()
        return not self.lives or wall_coll

    def draw_heart(self, center_x, center_y, 
                       height, width):
        myData = array.array('h', [int(center_x)          , int(center_y + height/2),
                                   int(center_x - width/2), int(center_y - height/4),
                                   int(center_x - width/4), int(center_y - height/2),
                                   int(center_x)          , int(center_y - height/4),
                                   int(center_x + width/4), int(center_y - height/2),
                                   int(center_x + width/2), int(center_y - height/4),
                                   int(center_x)          , int(center_y + height/2)
                                  ])
        self.screen.poly(0,0, myData, 1, True)