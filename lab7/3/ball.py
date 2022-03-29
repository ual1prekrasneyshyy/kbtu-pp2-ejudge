import pygame

number_of_error = 1


def print_error():
    global number_of_error
    print(f'Error {number_of_error}! Ball is going to leave the screen!')
    number_of_error += 1


pygame.init()

#settings
l_x, l_y = 400, 400
FPS = 60
dl = 20
r = 25
x, y = 30, 30

screen = pygame.display.set_mode((l_x, l_y))

running = True

RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
screen.fill(WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_DOWN]:
                if y+dl+r <= l_y:
                    y += dl
                else:
                    print_error()
            elif pressed[pygame.K_UP]:
                if y-dl-r >= 0:
                    y -= dl
                else:
                    print_error()
            elif pressed[pygame.K_LEFT]:
                if x-dl-r >= 0:
                    x -= dl
                else:
                    print_error()
            elif pressed[pygame.K_RIGHT]:
                if x+dl+r <= l_x:
                    x += dl
                else:
                    print_error()

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), r)

    pygame.display.flip()
    clock.tick(FPS)
