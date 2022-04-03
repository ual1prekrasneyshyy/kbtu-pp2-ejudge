import math
import os

import pygame

size = width, height = 480,360
center = (width/2, height/2)
pygame.init()
screen = pygame.display.set_mode(size)
done = False

_image_lib = {}
def get_image(path):
    global _image_lib
    image = _image_lib.get(path)
    if image is None:
        can_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(can_path)
        _image_lib[path] = image
    return image


clock = pygame.time.Clock()

im_min = get_image('images/minutes_arrow.png')
im_sec = get_image('images/seconds_arrow.png')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    im_min = pygame.transform.rotate(im_min, -0.1) #360 degree / 60 minutes (3600 seconds)
    dm = im_min.get_rect(center=im_min.get_rect(center=center).center)
    im_sec = pygame.transform.rotate(im_sec, -6) # 360 degree / 60 seconds
    ds = im_sec.get_rect(center=im_sec.get_rect(center=center).center)

    screen.blit(get_image('images/clock.jpg'), (0, 0))
    screen.blit(im_min, dm)
    screen.blit(im_sec, ds)

    pygame.display.flip()
    clock.tick(1)