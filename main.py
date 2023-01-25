
# Import pygame
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Number Guessing Game")

# Create color variables
bg_color = pygame.Color('#ADD8E6')
color_inactive = pygame.Color('White')
color_active = pygame.Color("#808080")
color = color_inactive

# Generate a random number for the user to guess
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
answer = (num1 + num2) // random.randint(1, 10)

# Create a text input box
textbox_x, textbox_y = 100, 150
textbox_width, textbox_height = 140, 32
active = False

# Define the font for the text input box
FONT = pygame.font.Font(None, 32)

# Define the input_box variable
input_box = ""

# Set the number of guesses
guesses = 5

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if (event.pos[0] > textbox_x
                    and event.pos[0] < textbox_x + textbox_width) and (
                        event.pos[1] > textbox_y
                        and event.pos[1] < textbox_y + textbox_height):
                active = not active
            else:
                active = False

            color = color_active if active else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    guess = input_box
                    input_box = ""
                    # Check if the guess is correct
                    if int(guess) == answer:
                        myfont = pygame.font.SysFont('Arial', 15)
                        textsurface = myfont.render('You guessed correctly!',
                                                    False, (0, 0, 0))
                        screen.fill(bg_color)
                        screen.blit(textsurface, (50, 50))
                        running = False
                    elif int(guess) > answer:
                        guesses -= 1
                        myfont = pygame.font.SysFont('Arial', 15)
                        textsurface = myfont.render(
                            'Too high! Guess again. You have ' + str(guesses) +
                            ' guesses left.', False, (0, 0, 0))
                        screen.fill(bg_color)
                        screen.blit(textsurface, (50, 50))
                        if guesses == 0:
                            myfont = pygame.font.SysFont('Arial', 15)
                            textsurface = myfont.render(
                                'You ran out of guesses. Better luck next time!',
                                False, (0, 0, 0))
                            screen.fill(bg_color)
                            screen.blit(textsurface, (50, 50))
                            pygame.time.wait(5000)
                            running = False
                    else:
                        guesses -= 1
                        myfont = pygame.font.SysFont('Arial', 15)
                        textsurface = myfont.render(
                            'Too low! Guess again. You have ' + str(guesses) +
                            ' guesses left.', False, (0, 0, 0))
                        screen.fill(bg_color)
                        screen.blit(textsurface, (50, 50))
                        if guesses == 0:
                            myfont = pygame.font.SysFont('Arial', 15)
                            textsurface = myfont.render(
                                'You ran out of guesses. Better luck next time!',
                                False, (0, 0, 0))
                            screen.fill(bg_color)
                            screen.blit(textsurface, (50, 50))
                            pygame.time.wait(5000)
                            running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_box = input_box[:-1]
                else:
                    input_box += event.unicode

    # Draw the text input box
    pygame.draw.rect(screen, color,
                     (textbox_x, textbox_y, textbox_width, textbox_height))
    txt_surface = FONT.render(input_box, True, (0, 0, 0))
    screen.blit(txt_surface, (textbox_x + 5, textbox_y + 5))

    pygame.display.update()

# Quit pygame
pygame.quit()
