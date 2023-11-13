import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #it creates the window
pygame.display.set_caption("DINO RUSH")#changes the name of window

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 2 * player_height
player_speed = 5

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Fonts
font = pygame.font.SysFont(None, 55)

# Score
score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
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

    # Move obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # Check for collisions
    for obstacle in obstacles:
        if (
            player_x < obstacle[0] + obstacle_width
            and player_x + player_width > obstacle[0]
            and player_y < obstacle[1] + obstacle_height
            and player_y + player_height > obstacle[1]
        ):
            running = False

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < HEIGHT]

    # Update score
    score += 1

    # Draw everything
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, RED, [player_x, player_y, player_width, player_height])

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(
            screen, RED, [obstacle[0], obstacle[1], obstacle_width, obstacle_height]
        )

    # Draw score
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, [10, 10])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()