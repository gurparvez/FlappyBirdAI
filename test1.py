import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Bird properties
bird_x = 100
bird_y = 200
bird_velocity = 0
GRAVITY = 0.5
JUMP = -10
BIRD_SIZE = 30

# Pipe properties
PIPE_WIDTH = 50
PIPE_GAP = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)
PIPE_SPEED = 3

# Game variables
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def draw_bird(x, y):
    pygame.draw.circle(screen, BLACK, (int(x), int(y)), BIRD_SIZE//2)

def draw_pipe(x, height):
    # Top pipe
    pygame.draw.rect(screen, GREEN, (x, 0, PIPE_WIDTH, height))
    # Bottom pipe
    pygame.draw.rect(screen, GREEN, (x, height + PIPE_GAP, PIPE_WIDTH, HEIGHT - height - PIPE_GAP))

def check_collision(bird_x, bird_y, pipe_x, pipe_height):
    bird_rect = pygame.Rect(bird_x - BIRD_SIZE//2, bird_y - BIRD_SIZE//2, BIRD_SIZE, BIRD_SIZE)
    top_pipe = pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_height)
    bottom_pipe = pygame.Rect(pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT)

    if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
        return True
    if bird_y < 0 or bird_y > HEIGHT:
        return True
    return False

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP

    # Update bird position
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Update pipe position
    pipe_x -= PIPE_SPEED
    if pipe_x < -PIPE_WIDTH:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Check collision
    if check_collision(bird_x, bird_y, pipe_x, pipe_height):
        running = False

    # Draw everything
    screen.fill(WHITE)
    draw_bird(bird_x, bird_y)
    draw_pipe(pipe_x, pipe_height)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Game over
game_over_text = font.render(f"Game Over! Score: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//2))
pygame.display.flip()
pygame.time.wait(2000)

pygame.quit()
sys.exit()