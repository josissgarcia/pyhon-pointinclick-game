import pygame
from pygame.display import update
from pygame.locals import *
from sys import exit
from random import randint

from pygame.mixer import Sound

pygame.init()

x_tela = 800
y_tela = 600
fonte = pygame.font.SysFont('calibri',40,True,True)

# sound_bg = pygame.mixer.music.load("score.wav")
# pygame.mixer.music.play(-1)

sound_score = pygame.mixer.Sound("score.wav")
sound_score.set_volume(1.2)
sound_shot = pygame.mixer.Sound("shot.wav")
sound_shot.set_volume(0.4)

x_player = int(x_tela/2)
y_player = int(y_tela/2)
speed_player = 10

x_marker = randint(40,x_tela-20)
y_marker = randint(40,y_tela-20)
speed_marker = 1
direct_marker = 1

score = 0
countdown = 60

tela = pygame.display.set_mode((x_tela,y_tela))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

img_bg = pygame.image.load("background.jpg")
img_player = pygame.image.load("mira.png")
img_marker = pygame.image.load("meteoro1.png")
img_marker2 = pygame.image.load("explode.png")

while True:
    relogio.tick(100)
    tela.fill((0,0,0))
    msg = f'Score: {score}'
    msg_formated = fonte.render(msg,True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_e:
                sound_shot.play()
                if objPlayer.colliderect(objMarker):
                    sound_score.play()
                    score = score + 1
                    x_marker = randint(40,x_tela-20)
                    y_marker = randint(40,y_tela-20)
                    speed_marker = randint(1,3)
                    direct_marker = randint(1,2)
        
    tela.blit(img_bg,(0,0))

    if pygame.key.get_pressed()[K_w]:
        y_player = y_player - speed_player
    if pygame.key.get_pressed()[K_s]:
        y_player = y_player + speed_player
    if pygame.key.get_pressed()[K_d]:
        x_player = x_player + speed_player
    if pygame.key.get_pressed()[K_a]:
        x_player = x_player - speed_player
    
    objPlayer = tela.blit(img_player,(x_player,y_player))
    objMarker = tela.blit(img_marker, (x_marker,y_marker))

    if direct_marker == 1:
        x_marker = x_marker + speed_marker
        y_marker = y_marker + speed_marker
    else:
        x_marker = x_marker - speed_marker
        y_marker = y_marker - speed_marker

    # condiçoes para teleport player na tela
    if y_player >= y_tela:
        y_player = 0
    if x_player >= x_tela:
        x_player = 0
    if x_player < 0:
        x_player = x_tela
    if y_player < 0:
        y_player = y_tela
        
    # condiçoes para teleport marker na tela
    if y_marker >= y_tela:
        y_marker = 0
    if x_marker >= x_tela:
        x_marker = 0
    if x_marker < 0:
        x_marker = x_tela
    if y_marker < 0:
        y_marker = y_tela

    tela.blit(msg_formated, (20,20))
    pygame.display.update()
