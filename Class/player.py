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
        
    def draw(self, surface):
        color = (0, 0, 255) if self.team == "A" else (255, 0, 0)
        pygame.draw.circle(surface, color, self.position, 45)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.num), True, (255, 255, 255))
        text_rect = text.get_rect(center=self.position)
        surface.blit(text, text_rect)