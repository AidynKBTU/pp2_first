import pygame
import sys
from datetime import datetime

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mickey Clock")

mickey_head_image = pygame.image.load("head.png")
mickey_right_hand_image = pygame.image.load("right.png")
mickey_left_hand_image = pygame.image.load("left.png")

mickey_head_rect = mickey_head_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

hand_width = mickey_right_hand_image.get_width()
hand_height = mickey_right_hand_image.get_height()
hand_center_x = SCREEN_WIDTH // 2
hand_center_y = SCREEN_HEIGHT // 2
hand_length = 100 

def draw_clock(minute_angle, second_angle):
    screen.fill((255, 255, 255)) 
    screen.blit(mickey_head_image, mickey_head_rect)

    # Вычисление координат конца минутной и секундной стрелок
    minute_hand_end_x = hand_center_x + hand_length * \
        pygame.math.Vector2(1, 0).rotate(-minute_angle)[0]
    minute_hand_end_y = hand_center_y + hand_length * \
        pygame.math.Vector2(1, 0).rotate(-minute_angle)[1]
    second_hand_end_x = hand_center_x + hand_length * \
        pygame.math.Vector2(1, 0).rotate(-second_angle)[0]
    second_hand_end_y = hand_center_y + hand_length * \
        pygame.math.Vector2(1, 0).rotate(-second_angle)[1]

    # Отображение минутной и секундной стрелок
    screen.blit(mickey_right_hand_image, (hand_center_x - hand_width // 2, hand_center_y - hand_height // 2))
    screen.blit(mickey_left_hand_image, (hand_center_x - hand_width // 2, hand_center_y - hand_height // 2))

    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.now()
    minute = current_time.minute
    second = current_time.second


    minute_angle = minute * 6  
    second_angle = second * 6  

    draw_clock(minute_angle, second_angle)

    pygame.time.Clock().tick(1)  

pygame.quit()
sys.exit()
