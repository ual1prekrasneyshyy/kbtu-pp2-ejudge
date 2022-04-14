import pygame

pygame.init()
running = True

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (500, 500)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)


clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption('uPaint')
screen.fill(WHITE)

prev, cur = None, None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
            if prev:
                pygame.draw.line(screen, RED, prev, cur, width=2)
                prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
