import pygame, sys
from bsav_button import Button

pygame.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("/Users/lydiahe/Downloads/WT1/BSAV//assets/recharge.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # Draw the title
        VIS_TEXT = get_font(30).render("Binary Search Visualizer", True, (255, 255, 255))
        VIS_RECT = VIS_TEXT.get_rect(center=(WIDTH // 2, 70))
        SCREEN.blit(VIS_TEXT, VIS_RECT)

        BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(30), base_color="White", hovering_color="Purple")

        BACK.changeColor(PLAY_MOUSE_POS)
        BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        # Clear the screen
        SCREEN.fill((0, 0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the title
        TITLE_TEXT = get_font(30).render("Binary Search Visualizer", True, (255, 255, 255))
        TITLE_RECT = TITLE_TEXT.get_rect(center=(WIDTH // 2, 70))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Go!.png"), pos=(640, 650), 
                            text_input="Go!", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

        pygame.display.update()

main_menu()