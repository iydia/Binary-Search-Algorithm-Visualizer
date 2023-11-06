import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Initialize variables 
running = True
dt = 0

# Load Roboto font or fall back to Arial
try:
    title_font = pygame.font.Font("/Users/lydiahe/Downloads/WT1/BSAV//assets/recharge.ttf", 36)
    subtitle_font = pygame.font.Font("/Users/lydiahe/Downloads/WT1/BSAV/assets/recharge.ttf", 20)
except pygame.error:
    font = pygame.font.SysFont("Arial", 36)

small_font = pygame.font.Font(None, 28)  # Font for displaying entered values
error_font = pygame.font.Font(None, 24)  # Font for displaying error messages
error_color = (255, 0, 0)  # Red color for error message

text_input = ""
key_input = ""
text_pos = array_input_pos = (WIDTH // 2 - 200, 200)  # Centered text boxes
key_pos = key_input_pos = (WIDTH // 2 - 200, 300)  # Centered text boxes
active_input = None
caret_visible = True
caret_timer = 0
array_values = []  # Store entered values
search_key = ""  # Initialize search_key with an empty string
text_error = ""  # Initialize text input error message
key_error = ""  # Initialize key input error message

# Button state
button_color = (255, 255, 255)  # White
button_clicked = False

# Labels
array_label = subtitle_font.render("Array of integers to search from: (separated by spaces)", True, (255, 255, 255))
array_label_rect = array_label.get_rect(center=(WIDTH // 2, array_input_pos[1] - 25))
key_label = subtitle_font.render("Integer to search for:", True, (255, 255, 255))
key_label_rect = key_label.get_rect(center=(WIDTH // 2, key_input_pos[1] - 25))

def draw_text_input_box(text, position):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(position[0], position[1], 400, 40))
    text_surface = subtitle_font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (position[0] + 10, position[1] + 10))

def draw_caret(caret_x, caret_y):
    if caret_visible:
        pygame.draw.line(screen, (0, 0, 0), (caret_x, caret_y), (caret_x, caret_y + 40), 2)

def visualizer(): # Binary Search Visualization
    while True:
        screen.fill("black")

def title_page(): # Main Menu Screen
    while True:
        screen.fill("black")

pygame.quit()
sys.exit()