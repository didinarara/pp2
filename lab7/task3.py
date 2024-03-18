import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2

def draw_ball():
    pygame.draw.circle(window, RED, (ball_x, ball_y), ball_radius)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - 20, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + 20, WINDOW_HEIGHT - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - 20, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + 20, WINDOW_WIDTH - ball_radius)

    window.fill(WHITE)

    draw_ball()

    pygame.display.update()

pygame.quit()
sys.exit()