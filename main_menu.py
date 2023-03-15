import pygame

from Game import main
from constans import  HEIGHT, WIDTH, WHITE, BLACK, FONT_SIZE
# Define constants
FPS = 60


# Initialize Pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# Set up the font
font = pygame.font.Font(None, FONT_SIZE)


# Define the main menu function
def main_menu():
    # Set up the menu options
    options = ["Easy", "Medium", "Hard", "Quit"]
    selected = 0

    # Set up the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    print("K_RETURN: ")
                    print(selected)
                    # Start the game with the selected difficulty level
                    if selected == 0:
                        start_game("easy")
                    elif selected == 1:
                        start_game("medium")
                    elif selected == 2:
                        start_game("hard")
                    elif options[selected] == "Quit":
                        # Quit the game
                        running = False

        # Clear the screen
        WIN.fill(BLACK)

        # Draw the title
        title_text = font.render("Arkanoid", True, WHITE)
        title_rect = title_text.get_rect()
        title_rect.center = (WIDTH / 2, HEIGHT / 4)
        WIN.blit(title_text, title_rect)

        # Draw the menu options
        for i, option in enumerate(options):
            option_text = font.render(option, True, WHITE)
            option_rect = option_text.get_rect()
            option_rect.center = (WIDTH / 2, HEIGHT / 2 + i * FONT_SIZE * 1.5)
            if i == selected:
                # Highlight the selected option
                pygame.draw.rect(WIN, WHITE, (
                    option_rect.left - FONT_SIZE / 2, option_rect.top - FONT_SIZE / 2, option_rect.width + FONT_SIZE,
                    option_rect.height + FONT_SIZE), 4)
            WIN.blit(option_text, option_rect)

        # Update the screen
        pygame.display.update()

    # Quit Pygame
    pygame.quit()


# Define the start game function
def start_game(difficulty):
    speed = 0.1
    if difficulty == "easy":
        speed = 0.15
    elif difficulty == "medium":
        speed = 0.25
    elif difficulty == "hard":
        speed = 0.3

    main(speed)

# Call the main menu function
