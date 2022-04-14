import pygame
import random


pygame.init()
CLOCK = pygame.time.Clock()
FPS = 6
RADIUS = 10
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def get_coordinates(self) -> tuple:
        return self.x, self.y


class Food:
    def __init__(self):
        self.location = Point()
        self.radius = RADIUS
        self.set_random_position()

    @staticmethod
    def own_round(value, base=RADIUS):
        return base*round(value/RADIUS)

    def set_random_position(self):
        self.location.x = self.own_round(random.randint(0 , WINDOW_WIDTH))
        self.location.y = self.own_round(random.randint(0, WINDOW_HEIGHT))

    def draw(self):
        pygame.draw.circle(SCREEN, BLUE, self.location.get_coordinates(), self.radius)


class Snake:
    def __init__(self, *args, **kwargs):
        self.radius = RADIUS
        self.body = [Point(100, 100), Point(), Point()]
        self.block = 15
        self.dx = self.block
        self.dy = 0

    def head(self):
        return self.body[0]

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            # self.body[i].set_coordinates(self.body[i].get_coordinates())
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.head().x += self.dx
        self.head().y += self.dy

        if self.head().x > WINDOW_WIDTH:
            self.head().x = 0
        if self.head().x < 0:
            self.head().x = WINDOW_WIDTH
        if self.head().y > WINDOW_HEIGHT:
            self.head().y = 0
        if self.head().y < 0:
            self.head().y = WINDOW_HEIGHT

    def draw(self):
        for i, point in enumerate(self.body):
            color = RED if i == 0 else BLUE
            pygame.draw.circle(SCREEN, color, point.get_coordinates(), RADIUS)

    def add_tail(self):
        self.body.append(Point())


game_over = False
snake = Snake()
snake.draw()

while not game_over:
    # print("iii")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                snake.dy = -1 * snake.block
                snake.dx = 0
            if pressed[pygame.K_DOWN]:
                snake.dy = snake.block
                snake.dx = 0
            if pressed[pygame.K_LEFT]:
                snake.dy = 0
                snake.dx = -1 * snake.block
            if pressed[pygame.K_RIGHT]:
                snake.dy = 0
                snake.dx = snake.block

    pygame.display.flip()
    SCREEN.fill(WHITE)
    snake.move()
    snake.draw()
    CLOCK.tick(FPS)

pygame.quit()

