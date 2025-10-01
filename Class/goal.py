import pygame

class Goal:
    def __init__(self, x, y, width, height, color, name):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.name = name

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
    def goaled(self, ball):
        ball_x = ball.position[0]
        ball_y = ball.position[1]
        r = 15

        # Clamp circle center to rectangle edges
        closest_x = max(self.rect.left, min(ball_x, self.rect.right))
        closest_y = max(self.rect.top, min(ball_y, self.rect.bottom))

        # Distance circle→closest point
        dx = ball_x - closest_x
        dy = ball_y - closest_y
        return (dx*dx + dy*dy) <= (r * r)
    
class LeftGoal(Goal):
    def __init__(self, field_top, field_height, goal_width, color):
        x = 0
        y = field_top + (field_height - goal_width) // 2
        super().__init__(x, y, 10, goal_width, color, "left")


class RightGoal(Goal):
    def __init__(self, field_top, field_height, field_width, goal_width, color):
        x = field_width - 10
        y = field_top + (field_height - goal_width) // 2
        super().__init__(x, y, 10, goal_width, color, "right")

LEFT_GOAL_COLOR = (0, 0, 255) # Blue
RIGHT_GOAL_COLOR = (255, 0, 0) # Red
GOAL_WIDTH = 200
WIDTH, HEIGHT = 1400, 800
HUD_HEIGHT = 100
FIELD_TOP = HUD_HEIGHT
FIELD_HEIGHT = HEIGHT - HUD_HEIGHT
left_goal = LeftGoal(FIELD_TOP, FIELD_HEIGHT, GOAL_WIDTH, LEFT_GOAL_COLOR)
right_goal = RightGoal(FIELD_TOP, FIELD_HEIGHT, WIDTH, GOAL_WIDTH, RIGHT_GOAL_COLOR)