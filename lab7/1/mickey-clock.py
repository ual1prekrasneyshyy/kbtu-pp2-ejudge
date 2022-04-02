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



immin = get_image('images/minutes_arrow.png')
imsec = get_image('images/seconds_arrow.png')


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    immin = pygame.transform.rotate(immin, -0.1) #360 degree / 60 minutes (3600 seconds)
    dm = immin.get_rect(center=immin.get_rect(center=center).center)
    imsec = pygame.transform.rotate(imsec, -6) # 360 degree / 60 seconds
    ds = imsec.get_rect(center=imsec.get_rect(center=center).center)

    screen.blit(get_image('images/clock.jpg'), (0, 0))
    screen.blit(immin, dm)
    screen.blit(imsec, ds)

    pygame.display.flip()
    clock.tick(1)