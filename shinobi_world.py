import pygame
import random
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Shinobi world")

# icon
icon = pygame.image.load("ninja.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("itachi.jpg")
mixer.music.load("sound.mp3")
mixer.music.play(-1)

# weapon
weapon = pygame.image.load("kunai.png")
xcor = 350
ycor = 500
pchange = 0

# enemy
enemy =[]
ex = []
ey = []
exchange = []
eychange = []
no_of_enemies=4
for i in range(no_of_enemies):
    enemy.append(pygame.image.load("enemy.png"))
    ex.append(random.randint(0, 760))
    ey.append(random.randint(50, 150))
    exchange.append(0.5)
    eychange.append(20)

# kunai
kunai = pygame.image.load("kunai2.png")
kx = 0
ky = 480
kx_change = 0
ky_change = 1
kunai_state = "ready"

score_val=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

over_font=pygame.font.Font("freesansbold.ttf",64)

def gameover():
    o=over_font.render("GAME OVER!",True,(255,0,0))
    screen.blit(o,(200,250))


def show_score():
    score=over_font.render("score:"+str(score_val),True,(255,0,0))
    screen.blit(score,(textX,textY))

def player():
    screen.blit(weapon, (xcor, ycor))


def monster(x,y):
    screen.blit(enemy[i], (x, y))


def background():
    screen.blit(bg, (0, 0))


def throw(x, y):
    global kunai_state
    kunai_state = "fire"
    screen.blit(kunai, (x + 16, y))


def isCollision(ex, ey, kx, ky):
    distance = math.sqrt(pow((ex - kx), 2) + (pow((ey - ky), 2)))
    if distance < 20:
        return True
    else:
        return False

running = True
while running:
    background()
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            running = False
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_LEFT:
                pchange = -0.5
            if eve.key == pygame.K_RIGHT:
                pchange = 0.5
            if eve.key == pygame.K_SPACE:
                if kunai_state == "ready":
                    # ksound=mixer.Sound("eyes.m4a")
                    # ksound.play()
                    kx = xcor
                    throw(kx, ky)
        if eve.type == pygame.KEYUP:
            if eve.key == pygame.K_LEFT or eve.key == pygame.K_RIGHT:
                pchange = 0
    xcor += pchange
    player()
    if xcor >= 746:
        xcor = 746
    elif xcor <= 0:
        xcor = 0

    for i in range(no_of_enemies):
        if ey[i]>440:
            for j in range(no_of_enemies):
                ey[j]=2000
            gameover()
            break

        ex[i] += exchange[i]
        if ex[i] >= 730:
            exchange[i] = -0.5
            ey[i] += eychange[i]
        elif ex[i]<= 0:
            exchange[i] = 0.5
            ey[i] += eychange[i]

    #collision
        collision = isCollision(ex[i], ey[i], kx, ky)
        if collision:
            ky = 480
            kunai_state = "ready"
            score_val+=1
            ex[i] = random.randint(0, 760)
            ey[i] = random.randint(50, 150)
        monster(ex[i],ey[i])

    if ky <= 0:
        kunai_state = "ready"
        ky = 480

    if kunai_state == "fire":
        throw(kx, ky)
        ky -= ky_change

    show_score()

    pygame.display.update()
