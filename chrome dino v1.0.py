import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1400, 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Runner v1.0")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 2 * player_height
player_speed = 8

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Fonts
font = pygame.font.SysFont(None, 55)

# Score and Power-up settings
score = 0
powerup_width = 40
powerup_height = 40
powerup_speed = 5
powerup_frequency = 150
powerups = []
powerup_counter = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Generate obstacles
    if random.randrange(0, obstacle_frequency) == 0:
        obstacle_x = random.randrange(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append([obstacle_x, obstacle_y])

    # Generate power-ups
    if random.randrange(0, powerup_frequency) == 0:
        powerup_x = random.randrange(0, WIDTH - powerup_width)
        powerup_y = -powerup_height
        powerups.append([powerup_x, powerup_y, random.choice([RED, GREEN, BLUE])])

    # Move obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # Move power-ups
    for powerup in powerups:
        powerup[1] += powerup_speed

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if (
            player_x < obstacle[0] + obstacle_width
            and player_x + player_width > obstacle[0]
            and player_y < obstacle[1] + obstacle_height
            and player_y + player_height > obstacle[1]
        ):
            running = False

    # Check for collisions with power-ups
    for powerup in powerups:
        if (
            player_x < powerup[0] + powerup_width
            and player_x + player_width > powerup[0]
            and player_y < powerup[1] + powerup_height
            and player_y + player_height > powerup[1]
        ):
            powerups.remove(powerup)
            powerup_counter += 1

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < HEIGHT]

    # Remove off-screen power-ups
    powerups = [powerup for powerup in powerups if powerup[1] < HEIGHT]

    # Draw everything
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, RED, [player_x, player_y, player_width, player_height])

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(
            screen, RED, [obstacle[0], obstacle[1], obstacle_width, obstacle_height]
        )

    # Draw power-ups
    for powerup in powerups:
        pygame.draw.rect(
            screen,
            powerup[2],  # Use the color stored in the power-up list
            [powerup[0], powerup[1], powerup_width, powerup_height],
        )

    # Draw score
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, [10, 10])

    # Draw power-up counter
    counter_text = font.render(f"Power-ups: {powerup_counter}", True, RED)
    screen.blit(counter_text, [WIDTH - 200, 10])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()