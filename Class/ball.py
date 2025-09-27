import pygame



class Hitbox:
    def __init__(self, Pos, radius):
        self.Pos = Pos
        self.radius = radius
    def update(self, new_pos):
        self.Pos = new_pos
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), self.Pos, self.radius, 1) 
        
class Ball:
    def __init__(self, position, velocity):
        self.position = position  # position is a tuple (x, y)
        self.velocity = velocity  # velocity is a tuple (vx, vy)
        self.hitbox = Hitbox(position, 15)  # placeholder for hitbox, if needed
         # Draw hitbox as a red circle
        self.last_touch = None  # Track last player who touched the ball
    
        
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.velocity = (self.velocity[0] * 0.975, self.velocity[1] * 0.975)  # Simulate friction
        
    def collision(self, players):
        for player in players:
            dx = self.position[0] - player.position[0]
            dy = self.position[1] - player.position[1]
            distance = (dx**2 + dy**2) ** 0.5
            if distance < 45 + 15:  
                self.velocity = (dx / distance * 20 + player.velocity[0], dy / distance * 20+player.velocity[1])
                self.last_touch = player  # Update last player who touched the ball
                
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), self.position, 15)  # Draw ball as a yellow circle    