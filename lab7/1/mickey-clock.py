import pygame
import datetime
import math


def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)


pygame.init()
screen = pygame.display.set_mode((480, 360))


base_of_clock = pygame.image.load('clock.jpg')
minutes_arrow = pygame.image.load('minutes_arrow.jpg')
seconds_arrow = pygame.image.load('seconds_arrow.jpg')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                blit_rotate_center(screen, minutes_arrow, (200, 200), 1)

        screen.blit(base_of_clock, (0, 0))
        # screen.blit(minutes_arrow, (0, 0))
        screen.blit(minutes_arrow, (224, 229))
        # screen.blit(seconds_arrow, (224, 229))

        pygame.display.flip()
