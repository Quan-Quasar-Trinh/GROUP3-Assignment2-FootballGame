import pygame
from Class.player import Hitbox
from utils.botMove import botMove

def update_players(TeamA_Players, TeamB_Players):
    keys = pygame.key.get_pressed()
    for player in TeamA_Players:
        if player.controlled:
            if keys[pygame.K_w]:
                player.position = (player.position[0], player.position[1] - player.speed)
                player.velocity = (0, -player.speed)
            if keys[pygame.K_s]:
                player.position = (player.position[0], player.position[1] + player.speed)
                player.velocity = (0, player.speed)
            if keys[pygame.K_a]:
                player.position = (player.position[0] - player.speed, player.position[1])
                player.velocity = (-player.speed, 0)
            if keys[pygame.K_d]:
                player.position = (player.position[0] + player.speed, player.position[1])
                player.velocity = (player.speed, 0)
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
        
def update_ball(ball):
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
    if ball:
        ball.update()
    