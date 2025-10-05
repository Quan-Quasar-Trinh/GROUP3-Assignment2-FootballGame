import pygame
import sys
from utils.buttons import Button




WIDTH, HEIGHT = 1400, 800

# Create buttons
start_button = Button("Start Game", (600, 400), (200, 60))
quit_button = Button("Quit", (600, 500), (200, 60))

def menu(screen):
    while True:
        screen.fill((0, 100, 0))  # Dark green background

        title = pygame.font.Font(None, 74).render("Main Menu", True, (255, 255, 255))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 200))

        start_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event.pos):
                    return  # Exit menu, go to game
                if quit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()