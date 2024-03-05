import pygame
import time

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
        self.bug_coll_p = False
        self.extra_life_coll_p = False

    def show(self) -> None:
        # lives
        rect = pygame.Rect(0, 0, self.box_width, self.box_height)
        pygame.draw.rect(self.screen, (0,0,0), rect)
        for i in range(self.lives):
            self.draw_heart((1+2*i)*self.box_width/6,
                            self.box_height/2,
                            self.box_height-2,
                            (self.box_width/3) - 2)

        # score
        textRect = pygame.Rect(self.screen_width - self.box_width, 0, self.box_width, self.box_height)
        font = pygame.font.SysFont('Comic Sans MS', 10)
        text = font.render(f"{self.score:05}", False, (255,255,255), (0,0,0))
        self.screen.blit(text, textRect)

    def update(self, wall_coll:bool, bug_coll:bool, extra_life_coll: bool) -> bool:
        self.lives -= bug_coll and not self.bug_coll_p
        self.lives += extra_life_coll and not self.extra_life_coll_p and self.lives < 3
        self.bug_coll_p = bug_coll
        if time.time() - self.last_score_add > 1:
            self.score += 1
            self.last_score_add = time.time()
        return not self.lives or wall_coll


    def draw_heart(self, 
                   center_x, center_y, 
                   height, width):
        # TODO: DRAW ACTUAL HEART
        pygame.draw.circle(self.screen, (255,255,255), (center_x, center_y), height/2)
