import pygame
from player import Player
from bug import BugManager
import time
pygame.init()
pygame.font.init()

# Set up the drawing window
screen = pygame.display.set_mode([128, 64])
player = Player(screen, 64, 54, 3)
bug_mgr = BugManager(screen, 64)

# hold until user first click
font = pygame.font.SysFont('Comic Sans MS', 15)
text = font.render("Press Space", False, (255,255,255))
textRect = text.get_rect()
textRect.center = (128 // 2, 64 // 2)
screen.blit(text, textRect)
pygame.display.flip()
start_hold = True
game_over_hold = False
while start_hold:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_hold = False
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_hold = False

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.change_direction()

    # Fill the background with black
    screen.fill((0, 0, 0))
    
    # Update all components
    player.update()
    bug_coll = bug_mgr.update(0, 128, player.pos_x, player.pos_y, player.width, player.height)

    if bug_coll:
        game_over_hold = True
        break

    # Draw all components on screen 
    player.show()
    bug_mgr.show()
    # Flip the display
    pygame.display.flip()
    time.sleep(0.05)

text = font.render("GAME OVER", False, (255,255,255))
textRect = text.get_rect()
textRect.center = (128 // 2, 64 // 2)
screen.blit(text, textRect)
pygame.display.flip()
while running and game_over_hold:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_hold = False
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over_hold = False


# Done! Time to quit.
pygame.quit()