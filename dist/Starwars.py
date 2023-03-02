import tarfile

import pygame
import random
import math

# initialise pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('SpaceBG.png')
background2 = pygame.image.load('SpaceBG.png')
bgX1 = 0
bgY1 = 0
bgX2 = 0
bgY2 = -599
# title and icon
pygame.display.set_caption(" Star wars R2D2 rush ")
icon = pygame.image.load('r2.webp')
pygame.display.set_icon(icon)

# R2D2
bb_img = pygame.image.load('R2flying.png')
bbX = 350
bbY = 425
bbX_change = 0
bbY_change = 0

score = 0
font2 = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# deathstar plan
milk_img = pygame.image.load('Plans.png')
milkX = random.randint(0, 735)
milkY = -120

deathstar_img = pygame.image.load('tiefighter.png')
deathstarX = random.randint(0, 735)
deathstarY = -120

laser_img = pygame.image.load('laser.png')
laserX = random.randint(0, 735)
laserY = -300

def writetask():
    f = open("score.txt", "w")
    b = f.write(f"{score}")
    f.close()

def read_highscore():
    f = open("score.txt", "r")
    read_hs = int(f.read())
    if read_hs <= score:
        writetask()
    else:
        f.close()


    # print(read_hs)
    # return read_hs
    # f.close()


def show_highscore(x, y):
    f = open("score.txt", "r")
    read_hs = int(f.read())
    hsc = font2.render("Highscore : " + str(read_hs), True, (255, 255, 255))
    screen.blit(hsc, (x, y))
    f.close()

def bb(x, y):
    screen.blit(bb_img, (x, y))


def milk(x, y):
    screen.blit(milk_img, (milkX, milkY))


def deathstar(x, y):
    screen.blit(deathstar_img, (deathstarX, deathstarY))

def laser(x, y):
    screen.blit(laser_img, (laserX, laserY))


def collision1(bbX, bbY, milkX, milkY):
    if (milkY >= bbY and milkY <= 450) and (milkX >= bbX and milkX <= bbX + 100):
        return True
    else:
        return False


def collision2(bbX, bbY, deathstarX, deathstarY):
    if (bbY <= deathstarY <= 525) and (bbX - 110 <= deathstarX <= bbX + 100):
        return True

    else:
        return False


def collision3(bbX, bbY, laserX, laserY):
    if (bbY <= laserY <= 525) and (bbX - 50 <= laserX <= bbX + 50):
        return True

    else:
        return False


def show_score(x, y):
    sc = font2.render("Your Score : " + str(score), True, (255, 255, 255))
    screen.blit(sc, (x, y))


font1 = pygame.font.Font('freesansbold.ttf', 40)
tX = 10
tY = 10


def prom1(x, y):
    pr = font1.render(str("Game Over :("), True, (255, 255, 255))
    screen.blit(pr, (x + 100, y + 100))

# highscoree = 0

# def high_score(highscoree, score):
#     if score >= highscoree:
#         b = score
#         highscoree = b
#         print(f"this is the highscore : {highscoree}")
#     else:
#         print("not the highscore")


running = True

health = 0
game = 1

t = int

while running:

    screen.fill((0, 0, 0))

    # adding the background in the loop
    screen.blit(background, (0, 0))

    bgY1 += 3
    bgY2 += 3

    milkY += 3.5
    deathstarY += 5
    laserY += 10
    # bgX1 -=0.1
    # adding the background in the loop

    screen.blit(background, (bgX1, bgY1))
    screen.blit(background2, (bgX2, bgY2))

    # for quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --------------------------------

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #

        # -----------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bbX_change = -4.5
            if event.key == pygame.K_RIGHT:
                bbX_change = 4.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                bbX_change = 0

    if bgY1 >= 600:
        bgY1 = -599
        bgX1 = 0
    if bgY2 >= 600:
        bgY2 = -599
        bgX2 = 0

    bbX += bbX_change
    if bbX <= 0:
        bbX = 0
    if bbX >= 700:
        bbX = 700

    if milkY >= 650:
        milkX = random.randint(0, 735)
        milkY = -120

    if deathstarY >= 650:
        deathstarX = random.randint(0, 735)
        deathstarY = -120

    if laserY >= 1500:
        laserX = random.randint(0, 735)
        laserY = -1500

    if collision1(bbX, bbY, milkX, milkY):
        milkX = random.randint(0, 735)
        milkY = -120
        print("true")
        print(f"score : {score}")
        bb_img = pygame.image.load('R2flying.png')
        score += 3

        if 1 <= health <= 3:
            health -= 1
        print(health)

    if collision2(bbX, bbY, deathstarX, deathstarY):
        deathstarX = random.randint(0, 700)
        deathstarY = -120
        print(f"score death : {score}")
        score -= 1
        health += 1
        print(health)

    if collision3(bbX, bbY, laserX, laserY):
        laserX = random.randint(0, 700)
        laserY = -120
        print(f"score death : {score}")
        score -= 1
        health += 3
        print(health)

    if health == 1:
        bb_img = pygame.image.load('R2damaged.png')

    if health == 2:
        bb_img = pygame.image.load('R2damagedd2.png')

    if health >= 3:
        bb_img = pygame.image.load('R2damaged3.png')
        milkY = -200
        deathstarY = -200
        laserY = -250
        game = 0
        (prom1(tX, tY))

    if game == 0:
        if 5 > bgY1 > -5:
            bgY1 = 0
            bgY2 = 0
            # writetask()
            read_highscore()
            show_highscore(textX, textY+50)

    bb(bbX, bbY)
    milk(milkX, milkY)
    deathstar(deathstarX, deathstarY)
    laser(laserX, laserY)
    show_score(textX, textY)
    pygame.display.update()
