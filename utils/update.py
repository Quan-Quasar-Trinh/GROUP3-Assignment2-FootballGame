import pygame
from Class.player import Hitbox
from Class.ball import *
from utils.botMove import botMove
from utils.draw import draw_field
from utils.spawn import *

def update_players(TeamA_Players, TeamB_Players):
    keys = pygame.key.get_pressed()
    for player in TeamA_Players:
        if player.controlled:
            player.velocity = (0, 0)  # Reset velocity each frame
            if keys[pygame.K_w]:
                player.position = (player.position[0], player.position[1] - player.speed)
                player.velocity = (player.velocity[0], player.velocity[1] -player.speed)
            if keys[pygame.K_s]:
                player.position = (player.position[0], player.position[1] + player.speed)
                player.velocity = (player.velocity[0], player.velocity[1] + player.speed)
            if keys[pygame.K_a]:
                player.position = (player.position[0] - player.speed, player.position[1])
                player.velocity = (player.velocity[0] - player.speed, player.velocity[1])
            if keys[pygame.K_d]:
                player.position = (player.position[0] + player.speed, player.position[1])
                player.velocity = (player.velocity[0] + player.speed, player.velocity[1])
            if player.position[0] < 0:
                player.position = (0, player.position[1])
            if player.position[0] > 1400:
                player.position = (1400, player.position[1])
            if player.position[1] < 100:
                player.position = (player.position[0], 100)
            if player.position[1] > 800:
                player.position = (player.position[0], 800)
        else:
            botMove()
                
    for player in TeamB_Players:
        if player.controlled:
            if keys[pygame.K_UP]:
                player.position = (player.position[0], player.position[1] - player.speed)
                player.velocity = (0, -player.speed)
            if keys[pygame.K_DOWN]:
                player.position = (player.position[0], player.position[1] + player.speed)
                player.velocity = (0, player.speed)
            if keys[pygame.K_LEFT]:
                player.position = (player.position[0] - player.speed, player.position[1])
                player.velocity = (-player.speed, 0)
            if keys[pygame.K_RIGHT]:
                player.position = (player.position[0] + player.speed, player.position[1])
                player.velocity = (player.speed, 0)
    for player in TeamA_Players + TeamB_Players:
        if player.hitbox:
            player.hitbox.update(player.position)
    
    
def update_controlled(Team_Players):
    for player in Team_Players:
        if player.controlled:
            player.controlled = False
            next_index = (Team_Players.index(player) + 1) % len(Team_Players)
            Team_Players[next_index].controlled = True
            break
        
def update_ball(ball, TeamA_Players, TeamB_Players):
    if ball.position[0] < 10:
        ball.position = (10, ball.position[1])
        ball.velocity = (-ball.velocity[0], ball.velocity[1])
    if ball.position[0] > 1390:
        ball.position = (1390, ball.position[1])
        ball.velocity = (-ball.velocity[0], ball.velocity[1])
    if ball.position[1] < 100:
        ball.position = (ball.position[0], 100)
        ball.velocity = (ball.velocity[0], -ball.velocity[1])
    if ball.position[1] > 790:
        ball.position = (ball.position[0], 790)
        ball.velocity = (ball.velocity[0], -ball.velocity[1])
    
    if ball.velocity[0]**2 + ball.velocity[1]**2 < 0.1:
        ball.velocity = (0, 0)
        
    ball.collision(TeamA_Players + TeamB_Players)
        
    if ball:
        ball.update()
        
def show_goal_screen(screen, width, height, team, scorer):
    screen.fill((0, 180, 0))

    font_big = pygame.font.Font(None, 120)
    font_small = pygame.font.Font(None, 60)

    goal_text = font_big.render(f"GOAL for Team {team}!", True, (255, 255, 255))
    scorer_text = font_small.render(f"Scorer: {scorer.name if scorer else 'Unknown'}", True, (255, 255, 255))

    # Center text
    screen.blit(goal_text, (width//2 - goal_text.get_width()//2, height//2 - 100))
    screen.blit(scorer_text, (width//2 - scorer_text.get_width()//2, height//2 + 20))

    pygame.display.flip()

        
    