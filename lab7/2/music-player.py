import os
import pygame


def stop_play_a_song():
    pygame.mixer.music.stop()


def play_a_song():
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()


def turn_previous_song():
    global _songs

    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()


def turn_next_song():
    global _songs

    _songs = _songs[1:] + [_songs[0]]

    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()


WORKING_DIR = os.getcwd()
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

_songs = []

for item in os.listdir(WORKING_DIR):
    target_path = os.path.join(WORKING_DIR, item)
    if os.path.isfile(target_path):
        if '.wav' in item:
            _songs.append(item)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.37)

screen = pygame.display.set_mode((365, 155))

font1 = pygame.font.SysFont('Verdana', 28)
font2 = pygame.font.SysFont('Verdana', 16)

txt1 = font1.render('My virtual music player.', True, GREEN)
txt2 = font2.render('Press [p] to start play music', True, WHITE)
txt3 = font2.render('Press [s] to stop play music', True, WHITE)
txt4 = font2.render('Press [->] to turn the next song', True, WHITE)
txt5 = font2.render('Press [<-] to turn the previous song', True, WHITE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                turn_next_song()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                turn_previous_song()
            elif event.key == pygame.K_p:
                play_a_song()
            elif event.key == pygame.K_s:
                stop_play_a_song()

    screen.fill(BLUE)
    screen.blit(txt1, (15, 15))
    screen.blit(txt2, (15, 50))
    screen.blit(txt3, (15, 72))
    screen.blit(txt4, (15, 94))
    screen.blit(txt5, (15, 116))

    pygame.display.flip()


