import pygame
import sys

from Class.goal import *

from utils.spawn import Spawn_Players
from utils.spawn import Spawn_Ball

from utils.draw import draw_field
from utils.draw import drawScore

from utils.update import update_players
from utils.update import update_controlled
from utils.update import update_ball
# from utils.update import update_goaled_A
# from utils.update import update_goaled_B




# GOAL_A_EVENT = pygame.USEREVENT + 1
# GOAL_B_EVENT = pygame.USEREVENT + 1

def show_goal_screen(screen, width, height, team, scorer):
    screen.fill((0, 180, 0))

    font_big = pygame.font.Font(None, 120)
    font_small = pygame.font.Font(None, 60)

    goal_text = font_big.render(f"GOAL for Team {team}!", True, (255, 255, 255))
    if scorer.team == team:
        scorer_text = font_small.render(f"Scorer: {scorer.num if scorer else 'Unknown'}", True, (255, 255, 255))
    else:
        scorer_text = font_small.render(f"Own Goal: {scorer.num if scorer else 'Unknown'}", True, (255, 255, 255))

    # Center text
    screen.blit(goal_text, (width//2 - goal_text.get_width()//2, height//2 - 100))
    screen.blit(scorer_text, (width//2 - scorer_text.get_width()//2, height//2 + 20))

    pygame.display.flip()

def show_winner_screen(screen, width, height, ScoreA, ScoreB):
    screen.fill((0, 180, 0))
    font_big = pygame.font.Font(None, 120)
    font_small = pygame.font.Font(None, 60)
    score_text = font_big.render(f"Team A: {ScoreA}               Team B: {ScoreB}", True, (255, 255, 255))
    if ScoreA > ScoreB:
        winner = font_small.render(f"Team A is the winner!", True, (255, 255, 255))
    elif ScoreA < ScoreB:
        winner = font_small.render(f"Team B is the winner!", True, (255, 255, 255))
    else:
        winner = font_small.render(f"Tie!", True, (255, 255, 255))

    stop_showing_winner_screen = font_small.render(f"(Press any key to return main menu)", True, (255, 255, 255))
    
    screen.blit(score_text, (width//2 - score_text.get_width()//2, height//2 - 100))
    screen.blit(winner, (width//2 - winner.get_width()//2, height//2 + 20))
    screen.blit(stop_showing_winner_screen, (width//2 - stop_showing_winner_screen.get_width()//2, height//2 + 140))
    

def game_loop(screen, WIDTH, HEIGHT, FIELD_COLOR, WHITE, LEFT_GOAL_COLOR, RIGHT_GOAL_COLOR, GOAL_WIDTH, running):
    game_running = True
    TeamA_Players = []
    TeamB_Players = []
    ball = []
    ScoreA = 0
    ScoreB = 0
    
    Spawn_Players(TeamA_Players, TeamB_Players)
    Spawn_Ball(ball)
    
    start_ticks = pygame.time.get_ticks()   # save starting time
    game_time = 90                          # 90 seconds
    font_timer = pygame.font.Font(None, 40) # font
    
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

        # Timer
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        time_left = max(0, game_time - seconds_passed)
        if time_left <= 0:
            show_winner_screen(screen, WIDTH, HEIGHT, ScoreA, ScoreB)
            pygame.display.flip()

            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:   # any key ends the winner screen
                        waiting = False
                        
            game_running = False
            return

        screen.fill(FIELD_COLOR)

        draw_field(screen, WIDTH, HEIGHT, FIELD_COLOR, WHITE, LEFT_GOAL_COLOR, RIGHT_GOAL_COLOR, GOAL_WIDTH)
        # Draw scores
        
        # Draw players
        for player in TeamA_Players + TeamB_Players:
            player.draw(screen)
        
        # Draw ball
        if ball:
            ball[0].draw(screen)
            
        # Goal A - Score for B
        if left_goal.goaled(ball[0]):
            start_time = pygame.time.get_ticks() # save current time stamp
            while pygame.time.get_ticks() - start_time < 1500:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                show_goal_screen(screen, WIDTH, HEIGHT, "B", ball[0].last_touch)
                            
            ScoreB += 1
        
            # respawn
            Spawn_Players(TeamA_Players, TeamB_Players)
            Spawn_Ball(ball)
        
        # Goal B - Score for A
        if right_goal.goaled(ball[0]):
            start_time = pygame.time.get_ticks() # save current time stamp
            while pygame.time.get_ticks() - start_time < 1500:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                show_goal_screen(screen, WIDTH, HEIGHT, "A", ball[0].last_touch)
                            
            ScoreA += 1
        
            # respawn
            Spawn_Players(TeamA_Players, TeamB_Players)
            Spawn_Ball(ball)
        
        drawScore(screen, WIDTH, ScoreA, ScoreB)
        
        # Draw timer at top center
        timer_text = font_timer.render(f"Time: {time_left}", True, (255,255,255))
        screen.blit(timer_text, (WIDTH//2 - timer_text.get_width()//2, 20))
        
        pygame.display.flip()
        pygame.time.delay(30)