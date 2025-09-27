import pygame
import sys
from utils.spawn import Spawn_Players
from utils.spawn import Spawn_Ball
from utils.draw import draw_field
from utils.draw import drawScore
from utils.update import update_players
from utils.update import update_controlled
from utils.update import update_ball






def game_loop(screen, WIDTH, HEIGHT, FIELD_COLOR, WHITE, GOAL_COLOR, GOAL_WIDTH, running):
    game_running = True
    TeamA_Players = []
    TeamB_Players = []
    ball = []
    ScoreA = 0
    ScoreB = 0
    
    Spawn_Players(TeamA_Players, TeamB_Players)
    Spawn_Ball(ball)
    
    
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False  # Exit to menu
                    return  # Return to menu
                if event.key == pygame.K_q:
                    update_controlled(TeamA_Players)
                if event.key == pygame.K_KP0:
                    update_controlled(TeamB_Players)
                
        update_players(TeamA_Players, TeamB_Players)
        update_ball(ball[0], TeamA_Players, TeamB_Players)

        
                
                
                

        screen.fill(FIELD_COLOR)

        draw_field(screen, WIDTH, HEIGHT, FIELD_COLOR, WHITE, GOAL_COLOR, GOAL_WIDTH)
        # Draw scores
        
        # Draw players
        for player in TeamA_Players + TeamB_Players:
            player.draw(screen)
        
        # Draw ball
        if ball:
            ball[0].draw(screen)


        drawScore(screen, WIDTH, ScoreA, ScoreB)
        pygame.display.flip()
        pygame.time.delay(30)