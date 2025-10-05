import pygame
class Hitbox:
    def __init__(self, Pos, radius):
        self.Pos = Pos
        self.radius = radius
    def update(self, new_pos):
        self.Pos = new_pos
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), self.Pos, self.radius, 1) 
class Player:
    def __init__(self,team, num, position, hitbox=None, controlled=False):
        self.team = team  # team is a string, e.g., "A" or "B"
        self.num = num
        self.position = position  # position is a tuple (x, y)
        self.velocity = (0, 0)  # velocity is a tuple (vx, vy)
        self.speed = 8  # default speed
        self.controlled = controlled  # whether the player is controlled by user
        self.hitbox = Hitbox(hitbox.Pos, hitbox.radius)  # placeholder for hitbox, if needed
         # Draw hitbox as a red circle   
        self.ball_cooldown = 0  # Cooldown timer for ball interaction 
        self.last_touch_time = None  # Track last time player touched the ball
    def draw(self, surface):
        color = (0, 0, 255) if self.team == "A" else (255, 0, 0)
        
        pygame.draw.circle(surface, color, self.position, 45)
        if self.controlled:
            x, y = self.position
            radius = 45
            triangle_height = 30
            triangle_width = 20
            # 3 đỉnh của tam giác (chỉ xuống)
            point1 = (x, y - radius)        # đỉnh dưới
            point2 = (x - triangle_width // 2, y - radius- triangle_height)    # góc trái
            point3 = (x + triangle_width // 2, y - radius- triangle_height)    # góc phải
            pygame.draw.polygon(surface, (255, 255, 0), [point1, point2, point3])
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.num), True, (255, 255, 255))
        text_rect = text.get_rect(center=self.position)
        surface.blit(text, text_rect)
        pos = (int(self.position[0]), int(self.position[1]))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            cd_value = self.ball_cooldown
            last_touch = self.last_touch_time
            info_text = font.render(f"CD: {cd_value}  LTT: {last_touch} Pos: {pos}", True, (255, 255, 0))
            info_rect = info_text.get_rect(midleft=(pos[0] + 55, pos[1]))
            surface.blit(info_text, info_rect)