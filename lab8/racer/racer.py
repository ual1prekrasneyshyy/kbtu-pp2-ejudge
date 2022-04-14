import random
import time

import pygame

clock = pygame.time.Clock()
fps = 60

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SPEED = 6
SCORE = 0

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 393, 600
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

font = pygame.font.SysFont('Verdana', 65)
font_small = pygame.font.SysFont('Verdana', 25)
game_over_text_label = font.render('Game over!', True, WHITE)

background = pygame.image.load('street.png')
pygame.mixer.init()
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play()

pygame.display.set_caption('GAME')

game_over = False


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, WINDOW_WIDTH-20), random.randint(20, WINDOW_HEIGHT-20))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_random_position(self):
        self.rect.center = (random.randint(20, WINDOW_WIDTH-20), random.randint(20, WINDOW_HEIGHT-20))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WINDOW_WIDTH-40), 0)

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)

        if self.rect.bottom > WINDOW_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, WINDOW_WIDTH-30), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT-80)

    def move(self):
        global SPEED

        # self.rect.move_ip(0, -1*SPEED)
        #
        # if self.rect.top < 0:
        #     self.rect.bottom = WINDOW_HEIGHT

        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WINDOW_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < WINDOW_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


player = Player()
enemy = Enemy()

enemies = pygame.sprite.Group()
enemies.add(enemy)

all_sprites = pygame.sprite.Group()
all_sprites.add(enemy)
all_sprites.add(player)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1500)

coin = Coin()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == INC_SPEED:
            SPEED += 1

    # screen.fill(WHITE)
    screen.blit(background, (0, 0))
    scores_label = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores_label, (10, 10))

    for sprite in all_sprites:
        sprite.move()
        sprite.draw(screen)
    coin.draw(screen)
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over_text_label, (11, 240))

        pygame.display.update()
        for sprite in all_sprites:
            sprite.kill()

        time.sleep(3)

        game_over = True

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
