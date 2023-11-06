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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if active_input == "text":
                    text_input_values = text_input.split()
                    if len(text_input_values) == 0:
                        text_error = "Input cannot be empty."
                    else:
                        try:
                            array_values = list(map(int, text_input.split()))
                            text_error = ""  # Reset text input error message
                            array_text = small_font.render("Array: [" + ", ".join(map(str, array_values)) + "]", True, (255, 255, 255))
                            array_rect = array_text.get_rect(center=(WIDTH // 2, 400))
                            screen.blit(array_text, array_rect)
                        except ValueError:
                            text_error = "Invalid Input. Integer values only"

                if active_input == "key":
                    key_input_values = key_input.split()
                    if len(key_input_values) == 1:
                        try:
                            search_key = int(key_input)
                            key_error = ""  # Reset key input error message
                        except ValueError:
                            key_error = "Invalid Input. Integer values only"
                    elif len(key_input_values) == 0:
                        key_error = "Input cannot be empty."
                    else:
                        key_error = "Invalid input. One search value only"
            elif event.key == pygame.K_BACKSPACE:
                if active_input == "text":
                    text_input = text_input[:-1]
                elif active_input == "key":
                    key_input = key_input[:-1]
            else:
                if active_input == "text":
                    text_input += event.unicode
                elif active_input == "key":
                    key_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if array_input_pos[0] < event.pos[0] < array_input_pos[0] + 400 and array_input_pos[1] < event.pos[1] < array_input_pos[1] + 40:
                active_input = "text"
                text_error = ""  # Clear text input error message
            elif key_input_pos[0] < event.pos[0] < key_input_pos[0] + 400 and key_input_pos[1] < event.pos[1] < key_input_pos[1] + 40:
                active_input = "key"
                key_error = ""  # Clear key input error message
            else:
                active_input = None

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the title
    title_text = title_font.render("Binary Search Visualizer", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(WIDTH // 2, 70))
    screen.blit(title_text, title_rect)

    # Draw labels
    screen.blit(array_label, array_label_rect)
    screen.blit(key_label, key_label_rect)

    # Draw text input boxes
    draw_text_input_box(text_input, array_input_pos)
    draw_text_input_box(key_input, key_input_pos)

    # Draw caret
    if active_input == "text":
        draw_caret(text_pos[0] + subtitle_font.size(text_input)[0] + 10, text_pos[1])
    elif active_input == "key":
        draw_caret(key_pos[0] + subtitle_font.size(key_input)[0] + 10, key_pos[1])

    # Display entered array values
    array_text = small_font.render("Array: " + " ".join(map(str, array_values)), True, (255, 255, 255))
    array_rect = array_text.get_rect(center=(WIDTH // 2, 400))
    screen.blit(array_text, array_rect)

    # Display search key
    key_text = small_font.render("Search Key: " + str(search_key), True, (255, 255, 255))
    key_rect = key_text.get_rect(center=(WIDTH // 2, 450))
    screen.blit(key_text, key_rect)

    # Display text input error message
    text_error_text = error_font.render(text_error, True, error_color)
    text_error_rect = text_error_text.get_rect(left=WIDTH // 2 + 210, top=array_input_pos[1])
    screen.blit(text_error_text, text_error_rect)

    # Display key input error message
    key_error_text = error_font.render(key_error, True, error_color)
    key_error_rect = key_error_text.get_rect(left=WIDTH // 2 + 210, top=key_input_pos[1])
    screen.blit(key_error_text, key_error_rect)

    # Draw the "Go!" button
    button_rect = pygame.Rect(WIDTH // 2 - 50, 500, 100, 40)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = small_font.render("Go!", True, (0, 0, 0))
    screen.blit(button_text, button_rect.move(35, 10))

    # Check if the button is clicked
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            button_color = (200, 200, 200)  # Light grey
        elif button_clicked:
            # Add code here to go to the next page of the game
            # For now, it will just go to a black screen
            screen.fill((0, 0, 0))
        else:
            button_color = (255, 255, 255)  # White
    else:
        button_color = (255, 255, 255)  # White

    # Update caret visibility
    caret_timer += dt
    if caret_timer >= 0.5:
        caret_timer = 0
        caret_visible = not caret_visible

    # Update the display
    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()
sys.exit()