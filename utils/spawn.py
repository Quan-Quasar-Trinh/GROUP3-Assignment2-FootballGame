from Class.player import Player
from Class.ball import Ball
from Class.player import Hitbox
import pygame


def Spawn_Players(TeamA_Players, TeamB_Players, is_pvp=False):
    # Clear spawn stacks
    TeamA_Players.clear()
    TeamB_Players.clear()
    
    # Spawn players for Team A
    for i in range(1,4):
        if i == 1:
            position = (400, 450)
        else:
            position = (200, 300 + (i-2)*300)  # Example positions
        player = Player("A", i, position, controlled=False, hitbox=Hitbox(position, 45))
        TeamA_Players.append(player)
    TeamA_Players[0].controlled = True  # Make the first player of Team A controlled by user
    # Spawn players for Team B
    for i in range(1,4):
        if i == 1:
            position = (1000, 450)
        else:
            position = (1200, 300 + (i-2)*300)  # Example positions
        player = Player("B", i, position, controlled=False, hitbox=Hitbox(position, 45))
        TeamB_Players.append(player)
    if is_pvp:
        TeamB_Players[0].controlled = True  # Make the first player of Team B controlled by user
        
def Spawn_Ball(ball):
    ball.clear() # Clear spawn stack
    ball.append(Ball((700, 450), (0, 0)))  # Spawn ball at center with no initial velocity