import pygame
import sys
from utils.buttons import Button
def choose_mode():
    
    pygame.init()
    
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Choose Mode")
    
    font = pygame.font.Font(None, 50)
    text = font.render("Choose Game Mode:", True, (255, 255, 255))
    
    pvp = Button("PVP", (WIDTH//2 - 100, HEIGHT//2 - 50), (200, 50))
    pve = Button("PVE", (WIDTH//2 - 100, HEIGHT//2 + 10), (200, 50))
    
    
    background = pygame.image.load("media/Images/menu.jpg")  # <-- replace with your file
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    while True:
        screen.blit(background, (0, 0))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 100))
        pvp.draw(screen)
        pve.draw(screen)
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return True  # 1v1 mode
                elif event.key == pygame.K_2:
                    return False  # 1vBot mode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp.is_clicked(event.pos):
                    return True  # 1v1 mode
                elif pve.is_clicked(event.pos):
                    return False   # 1vBot mode