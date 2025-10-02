import pygame
import random
import sys
import time
import os   # to check if image exists
from Class.player import Player
from Class.ball import Ball
from Class.goal import *
from Loops.Menu import menu
from Loops.Game import game_loop

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1400, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football")

FIELD_COLOR = (34, 139, 34)  # Green
WHITE = (255, 255, 255)

BALL_COLOR = (255, 255, 0)  # Yellow
BALL_RADIUS = 15

LEFT_GOAL_COLOR = (0, 0, 255) # Blue
RIGHT_GOAL_COLOR = (255, 0, 0) # Red
GOAL_WIDTH = 200


running = True
while running:
    menu(screen)
    game_loop(screen, WIDTH, HEIGHT, FIELD_COLOR, WHITE, LEFT_GOAL_COLOR, RIGHT_GOAL_COLOR, GOAL_WIDTH, running)
    

