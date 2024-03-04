import random

class WallManager:
    def __init__(self, screen:pygame.Surface,
                 screen_height: int, screen_width: int, 
                 wall_height: int = 6, wall_speed: int = 3) -> None:
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.wall_height = wall_height
        self.wall_speed  = wall_speed
        self.walls = []
        self.left_edge = 0
        self.right_edge = screen_width
        self.wall_pace = 3
    
    def show(self) -> None:
        for left_wall, right_wall in self.walls:
            left_wall.show()
            right_wall.show()
    
    def update(self, player_x: int, player_y: int,
               player_w: int, player_h: int) -> bool:
        for left_wall, right_wall in self.walls:
            left_wall.update()
            right_wall.update()
        
        diff = random.randint(-self.wall_pace,self.wall_pace)
        self.left_edge = max(0,self.left_edge + diff)
        self.right_edge = min(self.screen_width,self.right_edge + diff)
        self.walls.insert(0,(Wall(self.screen, 0, self.left_edge, self.wall_height, self.wall_speed),
                             Wall(self.screen, self.right_edge, self.screen_width, self.wall_height, self.wall_speed)))
        
        # check wall collision
        wall_collision = False
        for w_l,w_r in filter(lambda x: (x[0].y_top + x[0].height) >= player_y-(player_h/2) ,self.walls):
            wall_collision = ((player_x - player_w/2) < w_l.x_right) or ((player_x + player_w/2) > w_r.x_left)
        
        # disccard off-screen walls
        self.walls = [ws for ws in self.walls if ws[0].y_top < self.screen_height]

        return wall_collision

class Wall:
    def __init__(self, screen:pygame.Surface, x_left: int, x_right: int, 
                 height: int = 6, speed: int = 3) -> None:
        self.screen = screen
        self.y_top = -height
        self.x_left = x_left
        self.x_right = x_right
        self.height = height
        self.speed = speed

    def show(self) -> None:
        self.screen.fill_rect(self.x_left,self.y_top,self.x_right-self.x_left,self.height,1)
    
    def update(self) -> None:
        self.y_top += self.speed
