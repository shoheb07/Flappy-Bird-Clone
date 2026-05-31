import pygame
import random

pygame.init()

# Screen Settings
WIDTH, HEIGHT = 500, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)

# Bird
bird_x = 100
bird_y = 300
bird_radius = 20

gravity = 0.5
velocity = 0

# Pipes
pipes = []

pipe_width = 70
pipe_gap = 180

score = 0

font = pygame.font.SysFont(None, 50)

running = True

while running:

    screen.fill(BLUE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                velocity = -8

    # Bird Physics
    velocity += gravity
    bird_y += velocity

    bird_rect = pygame.Rect(
        bird_x - bird_radius,
        bird_y - bird_radius,
        bird_radius * 2,
        bird_radius * 2
    )

    # Generate Pipes
    if random.randint(1, 90) == 1:

        height = random.randint(150, 450)

        pipes.append(
            [
                WIDTH,
                height
            ]
        )

    # Draw Pipes
    for pipe in pipes:

        pipe[0] -= 4

        top_pipe = pygame.Rect(
            pipe[0],
            0,
            pipe_width,
            pipe[1]
        )

        bottom_pipe = pygame.Rect(
            pipe[0],
            pipe[1] + pipe_gap,
            pipe_width,
            HEIGHT
        )

        pygame.draw.rect(
            screen,
            GREEN,
            top_pipe
        )

        pygame.draw.rect(
            screen,
            GREEN,
            bottom_pipe
        )

        # Collision Detection
        if (
            bird_rect.colliderect(top_pipe)
            or
            bird_rect.colliderect(bottom_pipe)
        ):
            running = False

        if pipe[0] == bird_x:

            score += 1

    # Draw Bird
    pygame.draw.circle(
        screen,
        (255, 255, 0),
        (bird_x, int(bird_y)),
        bird_radius
    )

    # Ground/Top Collision
    if bird_y <= 0 or bird_y >= HEIGHT:

        running = False

    # Score
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(score_text, (20, 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
