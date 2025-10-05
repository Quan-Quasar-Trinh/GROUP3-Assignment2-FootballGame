import pygame
import sys
from utils.buttons import Button




WIDTH, HEIGHT = 1400, 800

# Create buttons
start_button = Button("Start Game", (600, 250), (200, 60))
quit_button = Button("Quit", (600, 350), (200, 60))

background = pygame.image.load("media/Images/menu.jpg")  # <-- replace with your file
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def menu(screen):
    pygame.mixer.init()

# Load background music (looped)
    pygame.mixer.music.load("media/Audios/menu.wav")  # <-- replace with your file
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    while True:
        screen.blit(background, (0, 0))

        title = pygame.font.Font(None, 74).render("Main Menu", True, (255, 255, 255))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))

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