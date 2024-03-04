from machine import Pin, I2C
import ssd1306

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) 
screen = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
button = Pin(4, Pin.IN, Pin.PULL_UP)

from font import Font
from player import Player
from bug import BugManager
from walls import WallManager
from scoreboard import ScoreBoard
from beeper import game_over_tune, buzz
import time
f = Font(screen)

while True:
    player = Player(screen, 64, 54, 3)
    bug_mgr = BugManager(screen, 64)
    wall_mgr = WallManager(screen, 64, 128, 3, 3)
    scoreboard = ScoreBoard(screen, 3, 0, 128)

    # hold until user first click
    screen.fill(0)
    f.text("Press",32,5, 24)
    f.text("Button",25,35, 24)
    screen.show()
    
    while True:
        if button.value() == 1:
            break
    while True:
        if button.value() == 0:
            break
    
    running = True
    lives = 3
    bug_coll_p = False
    # Run until the user asks to quit
    latch = True
    while running:
        if button.value() == 0 and latch:
            latch = False
            player.change_direction()
        elif (button.value() == 1 and (not latch)):
            latch = True
        # Fill the background black
        screen.fill(0)
        
        # Update all components
        player.update()
        wall_coll = wall_mgr.update(player_h=player.height,
                                    player_w=player.width,
                                    player_x=player.pos_x,
                                    player_y=player.pos_y)
        bug_coll = bug_mgr.update(wall_mgr.left_edge, wall_mgr.right_edge, 
                                  player.pos_x, player.pos_y, 
                                  player.width, player.height)
        if(scoreboard.update(wall_coll, bug_coll)):
            break

        player.show()
        bug_mgr.show()
        wall_mgr.show()
        scoreboard.show()
        screen.show()
        
    f.text("GAME OVER",25,0, 16)
    with open("high_score.txt","rt") as fp:
        high_score = int(fp.readlines()[0])
    if scoreboard.score > high_score:
        with open("high_score.txt","wt") as fp:
            fp.write(f"{scoreboard.score}")
        f.text("New Highscore!",5,17,10)
    f.text(f"score: {scoreboard.score}",5,34,10)
    f.text(f"highscore: {high_score}",5,50,10)
    screen.show()
    game_over_tune()
    while True:
        if button.value() == 0:
            break
