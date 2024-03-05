import pygame
from pygame.player import Player
from pygame.bug import BugManager
from pygame.walls import WallManager
from pygame.scoreboard import ScoreBoard
import time
pygame.init()
pygame.font.init()

# Set up the drawing window
screen = pygame.display.set_mode([128, 64])
player = Player(screen, 64, 54, 3)
bug_mgr = BugManager(screen, 64)
wall_mgr = WallManager(screen, 64, 128, 2, 3)
scoreboard = ScoreBoard(screen, 3, 0, 128)

# hold until user first click
font = pygame.font.SysFont('Comic Sans MS', 15)
text = font.render("Press Space", False, (255,255,255))
textRect = text.get_rect()
textRect.center = (128 // 2, 64 // 2)
screen.blit(text, textRect)
pygame.display.flip()
start_hold = True
game_over_hold = True
while start_hold:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_hold = False

running = True
lives = 3
bug_coll_p = False
# Run until the user asks to quit
while running:
    for event in pygame.event.get():
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            pygame.quit()
        # Did the user click space button?
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.change_direction()

    # Fill the background with black
    screen.fill((0, 0, 0))
    
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


    # Draw all components on screen 
    player.show()
    bug_mgr.show()
    wall_mgr.show()
    scoreboard.show()
    # Flip the display
    pygame.display.flip()
    time.sleep(0.05)

text = font.render("GAME OVER", False, (255,255,255))
textRect = text.get_rect()
textRect.center = (128 // 2, 64 // 2)
screen.blit(text, textRect)
pygame.display.flip()
while game_over_hold:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over_hold = False

# Done! Time to quit.
pygame.quit()
