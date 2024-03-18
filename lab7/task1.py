import sys
import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mickey mouse clock")

mickey_img = pygame.image.load("mickey.png")
right_arm_img = pygame.image.load("rightarm.png")
left_arm_img = pygame.image.load("leftarm.png")

right_angle = 0
left_angle = 0

def draw_hands():
    rotated_right_arm = pygame.transform.rotate(right_arm_img, right_angle)
    window.blit(rotated_right_arm, (WIDTH // 2 - rotated_right_arm.get_width() // 2, HEIGHT // 2 - rotated_right_arm.get_height() // 2))

    rotated_left_arm = pygame.transform.rotate(left_arm_img, left_angle)
    window.blit(rotated_left_arm, (WIDTH // 2 - rotated_left_arm.get_width() // 2, HEIGHT // 2 - rotated_left_arm.get_height() // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.datetime.now()
    minutes = current_time.minute
    seconds = current_time.second

    right_angle = -(minutes / 60) * 360
    left_angle = -(seconds / 60) * 360

    window.fill((255, 255, 255))

    window.blit(mickey_img, (WIDTH // 2 - mickey_img.get_width() // 2, HEIGHT // 2 - mickey_img.get_height() // 2))

    draw_hands()

    pygame.display.update()
    pygame.time.delay(1000)  
