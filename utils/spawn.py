from Class.player import Player
from Class.ball import Ball
from Class.player import Hitbox
import pygame


def Spawn_Players(TeamA_Players, TeamB_Players):
    TeamA_Players.clear()
    TeamB_Players.clear()
    
    # Spawn players for Team A
    for i in range(1,4):
        position = (100, i * 150)  # Example positions
        player = Player("A", i, position, controlled=False, hitbox=Hitbox(position, 45))
        TeamA_Players.append(player)
    TeamA_Players[0].controlled = True  # Make the first player of Team A controlled by user
    # Spawn players for Team B
    for i in range(1,4):
        position = (1300, i * 150)  # Example positions
        player = Player("B", i, position,controlled=False, hitbox=Hitbox(position, 45))
        TeamB_Players.append(player)
    TeamB_Players[0].controlled = True  # Make the first player of Team B controlled by user
        
def Spawn_Ball(ball):
    ball.clear()
    ball.append(Ball((700, 450), (0, 0)))  # Spawn ball at center with no initial velocity