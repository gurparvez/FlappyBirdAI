import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.radius = 15

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y > HEIGHT:
            self.y = HEIGHT
            self.velocity = 0

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, int(self.y)), self.radius)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT))

# Game loop
bird = Bird()
pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
running = True
score = 0

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()

    bird.update()
    bird.draw()

    for pipe in pipes:
        pipe.update()
        pipe.draw()

        # Collision detection
        if (pipe.x < bird.x < pipe.x + PIPE_WIDTH and
                (bird.y < pipe.height or bird.y > pipe.height + PIPE_GAP)):
            running = False

        # Score update
        if pipe.x + PIPE_WIDTH < bird.x and not pipe.passed:
            score += 1
            pipe.passed = True

    # Remove off-screen pipes and add new ones
    if pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)
        pipes.append(Pipe(WIDTH))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
