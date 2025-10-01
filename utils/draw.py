import pygame

from Class.goal import *

def draw_field(screen, WIDTH, HEIGHT, FIELD_COLOR, WHITE, LEFT_GOAL_COLOR, RIGHT_GOAL_COLOR, GOAL_WIDTH):
    HUD_HEIGHT = 100
    # Field dimensions (everything below HUD)
    FIELD_TOP = HUD_HEIGHT
    FIELD_HEIGHT = HEIGHT - HUD_HEIGHT

    # Draw field boundary (start from HUD_HEIGHT instead of 0)
    pygame.draw.rect(screen, WHITE, (0, FIELD_TOP, WIDTH, FIELD_HEIGHT), 10)

    # Halfway line
    pygame.draw.line(screen, WHITE,
                    (WIDTH // 2, FIELD_TOP),
                    (WIDTH // 2, HEIGHT), 5)

    # Center circle (shifted down by HUD_HEIGHT)
    pygame.draw.circle(screen, WHITE,
                    (WIDTH // 2, FIELD_TOP + FIELD_HEIGHT // 2),
                    75, 5)

    # # Goals (also shifted down)
    # pygame.draw.rect(screen, GOAL_COLOR,
    #                 (0, FIELD_TOP + (FIELD_HEIGHT - GOAL_WIDTH) // 2, 10, GOAL_WIDTH))  # Left goal

    # pygame.draw.rect(screen, GOAL_COLOR,
    #                 (WIDTH - 10, FIELD_TOP + (FIELD_HEIGHT - GOAL_WIDTH) // 2, 10, GOAL_WIDTH))  # `Right goal
    
    left_goal = LeftGoal(FIELD_TOP, FIELD_HEIGHT, GOAL_WIDTH, LEFT_GOAL_COLOR)
    right_goal = RightGoal(FIELD_TOP, FIELD_HEIGHT, WIDTH, GOAL_WIDTH, RIGHT_GOAL_COLOR)
    
    left_goal.draw(screen)
    right_goal.draw(screen)


def drawScore(screen, WIDTH, ScoreA, ScoreB):
    
    HUD_HEIGHT = 100  # space reserved for HUD at the top
    #Draw HUD background
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, WIDTH, HUD_HEIGHT)) 
    font = pygame.font.Font(None, 74)
    score_text = font.render(f"Team A: {ScoreA}               Team B: {ScoreB}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    
