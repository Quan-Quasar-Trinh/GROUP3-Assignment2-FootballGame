import pygame


class Ball:
    def __init__(self, position, velocity):
        self.position = position  # position is a tuple (x, y)
        self.velocity = velocity  # velocity is a tuple (vx, vy)
        
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.velocity = (self.velocity[0] * 0.98, self.velocity[1] * 0.98)  # Simulate friction
        
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), self.position, 15)  # Draw ball as a yellow circle    