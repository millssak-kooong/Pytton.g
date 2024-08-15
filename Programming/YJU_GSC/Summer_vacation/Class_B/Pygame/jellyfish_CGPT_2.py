import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("지렁이 게임")

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)

# Define clock for controlling the frame rate
clock = pygame.time.Clock()

# Define initial position and speed
x, y = width // 2, height // 2
speed = 20

# Define initial direction
direction = 'RIGHT'

# Function to handle movement
def handle_movement(direction, x, y, speed):
    if direction == 'RIGHT':
        x += speed
    elif direction == 'LEFT':
        x -= speed
    elif direction == 'UP':
        y -= speed
    elif direction == 'DOWN':
        y += speed
    return x, y

# Function to wait for the initial direction
def wait_for_initial_direction():
    direction = None
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                    waiting = False
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
                    waiting = False
                elif event.key == pygame.K_UP:
                    direction = 'UP'
                    waiting = False
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                    waiting = False
        # Display instruction
        screen.fill(black)
        font = pygame.font.SysFont(None, 50)
        message = font.render("Press an arrow key to start", True, green)
        screen.blit(message, (width // 2 - 200, height // 2 - 25))
        pygame.display.update()
    return direction

# Get the initial direction from the player
direction = wait_for_initial_direction()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change direction based on key press
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    # Update position based on direction
    x, y = handle_movement(direction, x, y, speed)

    # Ensure the snake stays within the window boundaries
    x = max(0, min(x, width - 20))
    y = max(0, min(y, height - 20))

    # Fill the screen with black to clear previous position
    screen.fill(black)

    # Draw the snake (a simple rectangle)
    pygame.draw.rect(screen, green, (x, y, 20, 20))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(15)

# Quit Pygame
pygame.quit()
