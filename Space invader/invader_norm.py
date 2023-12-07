import pygame
import random
import math
import sys
import os
import importlib
from menu import two  

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

#caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#defining the screen
screen = pygame.display.set_mode((1000, 600), pygame.FULLSCREEN)

#defining the bacground of the screen
background = pygame.image.load('back.png')

color = (0,0,0)
color_light = (255,255,255)
color_dark = (0,255,0)
width = screen.get_width()
height = screen.get_height()
bigfont = pygame.font.Font('freesansbold.ttf',60)
medium = pygame.font.Font('freesansbold.ttf',40)
smallfont = pygame.font.Font('freesansbold.ttf',35)
xsmallfont = pygame.font.Font('freesansbold.ttf',28)
xxsmallfont = pygame.font.Font('freesansbold.ttf',18)

text = smallfont.render('Next Level!' , True , color)
quit_text = smallfont.render('Quit' , True , color)
menu_text = smallfont.render('Back to Menu' , True , color)

textX = 10
textY = 10

playerIMG = pygame.image.load('ship5.png')
playerX = 370
playerY = 500
playerX_change = 5

#enemy ship
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 26

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('alien.png'))
    enemyX.append(0)
    enemyX.append(50)
    enemyX.append(100)
    enemyX.append(150)
    enemyX.append(200)
    enemyX.append(250)
    enemyX.append(300)
    enemyX.append(350)
    enemyX.append(400)
    enemyX.append(450)
    enemyX.append(500)
    enemyX.append(550)
    enemyX.append(600)
    enemyX.append(650)
    enemyX.append(700)
    enemyX.append(750)
    enemyX.append(800)
    enemyX.append(850)
    enemyX.append(900)
    enemyX.append(950)
    enemyY.append(50)
    enemyY.append(100)
    enemyY.append(150)
    enemyX_change.append(5)
    enemyY_change.append(50)

#bullet
#ready - you cant see the bullet
#fire - the laser is in motion
bulletIMG = pygame.image.load('laser.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y ):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerIMG, (x, y))

def enemy(x, y,  i):
    screen.blit(enemyIMG[i], (x, y))

def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 30, y + 10))

def isCollison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX[i] - bulletX, 2)) + (math.pow(enemyY[i]-bulletY,2 )))
    if distance < 27:
        return True
    else:
        return False

def over_text(x, y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (300, 200))

def Win_text(x, y):
    win_text = over_font.render("YOU WIN!", True, (255, 255, 255))
    screen.blit(win_text, (350, 200))

def pause_text(x, y):
    pause = over_font.render("PAUSED", True, (255, 255, 255))
    screen.blit(pause, (350, 200))

def esc(x, y):
    escape = xxsmallfont.render("Press ESC to Go Back to Menu", True, (255, 255, 255))
    screen.blit(escape, (360, 20))

def hard():
    import invader_hard
    importlib.reload(invader_hard)

running = True
while running:
    screen.blit(background, (0, 0))
    esc(textX, textY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.pygame.exit()
            runnning = False

#keyboard events and movements
        if event.type == pygame.KEYDOWN: # pressing any key down
            if event.key == ord('a'):
                playerX_change = -9
            if event.key == ord('d'):
                playerX_change = 9
            if event.key == pygame.K_ESCAPE:
                two()
        if event.type == pygame.KEYUP: # releaseing any pressed down key
            if event.key == ord('a') or event.key == ord('d'):
                playerX_change = 0
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bulletX = playerX
                    fire(playerX, bulletY)
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playerX_change = 0

        #if event.type == pygame.KEYDOWN: # pressing any key down
            #if event.key == ord('a'):
            #    playerX_change = -9
            #if event.key == ord('d'):
            #    playerX_change = 9
            #if event.key == pygame.K_ESCAPE:
            #    two()
        #if event.type == pygame.KEYUP: # releaseing any pressed down key
            #if event.key == ord('a') or event.key == ord('d'):
            #    playerX_change = 0

            #if event.type == pygame.MOUSEBUTTONUP:
            #    if event.button == 1:
            #        bulletX = playerX
            #        fire(playerX, bulletY)

            #if event.type == pygame.MOUSEBUTTONDOWN:
            #    if event.button == 1:
            #        playerX_change = 0


        for i in range(num_of_enemies):
            if event.type == pygame.KEYDOWN:
                if event.key == ord('p'):
                    for j in range(num_of_enemies):
                        enemyY[j]= -2000
                        playerY= -2000
                    pause_text(textX,textY)
            if event.type == pygame.KEYUP:
                if event.key == ord('p'):
                    for j in range(num_of_enemies):
                        enemyY[j]= -2000
                        playerY= -2000
                    pause_text(textX,textY)


#boundaries for main character
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
    if enemyY[i] >= 460:
        playerY = -2000
        playerX = 2000


#boundaries and movement of enemy
    for i in range(num_of_enemies):

        if enemyY[i] >= 460 and score_value != 60:
            for j in range(num_of_enemies):
                enemyY[j]= 2000
            over_text(textX, textY)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2-40 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40:
                    pygame.quit()
                if width/2-115 <= mouse[0] <= width/2+90 and height/1.65 <= mouse[1] <= height/1.65+40:
                    two()

                mouse = pygame.mouse.get_pos()
            if width/2-40 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,color_light,[width/2-40,height/2,80,40])
                screen.blit(quit_text ,(width/2-40,height/2+3))
            else:
                pygame.draw.rect(screen,color_dark,[width/2-40,height/2,80,40])
                screen.blit(quit_text ,(width/2-40,height/2+3))

            if width/2-115 <= mouse[0] <= width/2+90 and height/1.65 <= mouse[1] <= height/1.65+40:
                pygame.draw.rect(screen,color_light,[width/2-115,height/1.65,233,40])
                screen.blit(menu_text ,(width/2-115,height/1.65+3))
            else:
                pygame.draw.rect(screen,color_dark,[width/2-115,height/1.65,233,40])
                screen.blit(menu_text ,(width/2-115,height/1.65+3))


        elif score_value == 60:
            for j in range(num_of_enemies):
                enemyY[j]= 2000
            Win_text(textX, textY)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2-40 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40:
                    pygame.quit()
                if width/2-115 <= mouse[0] <= width/2+90 and height/1.65 <= mouse[1] <= height/1.65+40:
                    two()
                if width/2-115 <= mouse[0] <= width/2+90 and height/1.4 <= mouse[1] <= height/1.4+40:
                    hard()

                mouse = pygame.mouse.get_pos()
            if width/2-40 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,color_light,[width/2-40,height/2,80,40])
                screen.blit(quit_text ,(width/2-40,height/2+3))
            else:
                pygame.draw.rect(screen,color_dark,[width/2-40,height/2,80,40])
                screen.blit(quit_text ,(width/2-40,height/2+3))

            if width/2-115 <= mouse[0] <= width/2+90 and height/1.65 <= mouse[1] <= height/1.65+40:
                pygame.draw.rect(screen,color_light,[width/2-115,height/1.65,233,40])
                screen.blit(menu_text ,(width/2-115,height/1.65+3))
            else:
                pygame.draw.rect(screen,color_dark,[width/2-115,height/1.65,233,40])
                screen.blit(menu_text ,(width/2-115,height/1.65+3))

            if width/2-91 <= mouse[0] <= width/2+90 and height/1.4 <= mouse[1] <= height/1.4+40:
                pygame.draw.rect(screen,color_light,[width/2-91,height/1.4,190,40])
                screen.blit(text ,(width/2-91,height/1.4+3))
            else:
                pygame.draw.rect(screen,color_dark,[width/2-91,height/1.4,190,40])
                screen.blit(text ,(width/2-91,height/1.4+3))

        elif enemyY[i] < 460 and score_value < 70:
            pygame.mouse.set_pos(width/2, 550)
        else:
            pass


    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 936:
            enemyX_change[i] = -5.5
            enemyY[i] += enemyY_change[i]

        #collison
        collision = isCollison(enemyX, enemyY, bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)


#bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
