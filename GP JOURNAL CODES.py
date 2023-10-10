#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##practical 1
#Write A Python Program to Draw different Shapes to Perform Translation ,Transformation of that object


# In[2]:


from tkinter import *

root=Tk()


C=Canvas(root,bg="red",height=700,width=700)


Square=C.create_rectangle(50,50,200,200,fill="green")
oval=C.create_oval(50,50,200,200,fill="yellow")
eyes1=C.create_oval(85,90,105,110,fill="blue")
eyes2=C.create_oval(145,90,165,110,fill="blue")
nose=C.create_polygon(110,120,140,120,125,155,fill="black")
oval=C.create_oval(106,170,144,180,fill="blue")

C.create_text(150,30,text="Oval before Translation",fill="black",font=('Helvatica 15 bold'))

tx=300
ty=300

Square=C.create_rectangle(50+tx,50+ty,200+tx,200+ty,fill="green")
oval=C.create_oval(50+tx,50+ty,200+tx,200+ty,fill="yellow")
eyes1=C.create_oval(85+tx,90+ty,105+tx,110+ty,fill="blue")
eyes2=C.create_oval(145+tx,90+ty,165+tx,110+ty,fill="blue")
nose=C.create_polygon(110+tx,120+ty,140+tx,120+ty,125+tx,155+ty,fill="black")
oval=C.create_oval(106+tx,170+ty,144+tx,180+ty,fill="blue")

C.create_text(310,310,text="Oval after Translation",fill="black",font=('Helvatica 15 bold'))

C.pack()
mainloop()


# In[ ]:


##practical 2 Scaling


# In[30]:


from tkinter import*
root=Tk()
C=Canvas(root,bg="gray",height=819,width=662)
triangle=C.create_polygon(195,90,195,273,352,270,fill="dark green")
C.create_text(300,50,text="triangle before scaling",fill="black",font=('Arial'))
x=195
y=90
x1=195
x2=273
x2=352
y2=270
C.create_text(300,300,text="triangle after scaling",fill="black",font=('Arial'))
Sx=2
Sy=1
triangle=C.create_polygon(x*Sx,y*Sy,x1*Sx,y1*Sy,x2*Sx,y2*Sy,fill="blue")
C.pack()
mainloop()                   


# In[ ]:


##practical 3 Rotation


# In[31]:


from tkinter import*
import math
root=Tk()
C=Canvas(root,bg="yellow",height=1340,width=690)
x0=165
y0=158
x1=164
y1=259
x2=227
y2=257
b=90
C.create_polygon(x0,y0,x1,y1,x2,y2,fill="blue")
C.create_text(130,250,text="triangle before rotation",font=('helvetica'))
x01=abs(x0*math.cos(math.radians(b))-y0*math.sin(math.radians(b)))
y01=abs(x0*math.sin(math.radians(b))+y0*math.cos(math.radians(b)))
x11=abs(x1*math.cos(math.radians(b))-y1*math.sin(math.radians(b)))
y11=abs(x1*math.sin(math.radians(b))+y1*math.cos(math.radians(b)))
x21=abs(x2*math.cos(math.radians(b))-y2*math.sin(math.radians(b)))
y21=abs(x2*math.sin(math.radians(b))+y2*math.cos(math.radians(b)))
C.create_polygon(x01,y01,x11,y11,x21,y21,fill="black")
C.create_text(130,600,text="triangle after rotation",font=('helvetica'))
C.pack()
mainloop()


# In[ ]:


##practical 4 shearing


# In[ ]:


from tkinter import*
import math
root=Tk()
C=Canvas(root,bg="white",height=1340,width=690)
x0=int(input("enter x0 "))
y0=int(input("enter y0 "))
x1=int(input("enter x1 "))
y1=int(input("enter y1 "))
x2=int(input("enter x2 "))
y2=int(input("enter y2 "))
x3=int(input("enter x3 "))
y3=int(input("enter y3 "))
b=int(input("enter angle of shearing"))
polygon=C.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,fill="yellow")
xsh0=x0+y0*math.tan(math.radians(b))
xsh1=x1+y1*math.tan(math.radians(b))
xsh2=x2+y2*math.tan(math.radians(b))
xsh3=x3+y3*math.tan(math.radians(b))
polygon=C.create_polygon(xsh0,y0,xsh1,y1,xsh2,y2,xsh3,y3,fill="orange")
C.pack()
mainloop()


# In[ ]:


##practical 5 reflection 


# In[ ]:


from tkinter import*
import math
root = Tk()
C = Canvas(root,bg="yellow",height=1000,width=1200)
x0 = int(input("Enter x0"))
y0 = int(input("Enter y0"))
x1 = int(input("Enter x1"))
y1 = int(input("Enter y1"))
x2 = int(input("Enter x2"))
y2 = int(input("Enter y2"))
triangle=C.create_polygon(x0,y0,x1,y1,x2,y2,fill="black")
a=200
x10=-x0+(2*a)
x11=-x1+(2*a)
x12=-x2+(2*a)
triangle=C.create_polygon(x10,y0,x11,y1,x12,y2,fill="green")
C.pack()
mainloop()


# In[ ]:


##practical 6 space invader


# In[ ]:


---practical6----
----spaceinvader---
##ACTUAL CODE##
import math
import pygame
import random
from pygame import mixer

# initialization
pygame.init()
# display size
screen = pygame.display.set_mode((800, 600))
# Title
pygame.display.set_caption("Space Invader")
# Icon
icon = pygame.image.load("spaceship.png")
# Background sound
#mixer.music.load("background.wav")
#mixer.music.play(-1)
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(60, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Background
bgImg = pygame.image.load("background (1).png")
# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
score_value = 0
# Text for score display
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
# Game over text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


# Gameover Function
def game_over_text():
    gameover = game_over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(gameover, (200, 250))


# Score Function
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Collision function
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


running = True
# game window stays on until close
while running:
    screen.fill((0, 0, 0))  # Background Color
    screen.blit(bgImg, (0, 0))  # background Img
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()

                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    playerX += playerX_change
    # player boundary
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736  # size of player is 64, so we subtract 64 from 800

    # player boundary
    for i in range(no_of_enemies):
        # gameover code
        if enemyY[i] > 400:
            for j in range(no_of_enemies):
                enemyY[i] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 735:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        # Checking collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    show_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update()


# In[ ]:


##practical 7 snake game


# In[ ]:


# importing libraries 
import pygame 
import time 
import random 
 
snake_speed = 15 
 
# Window size 
window_x = 720 
window_y = 480 
 
# defining colors 
black = pygame.Color(0, 0, 0) 
white = pygame.Color(255, 255, 255) 
red = pygame.Color(255, 0, 0) 
green = pygame.Color(0, 255, 0) 
blue = pygame.Color(0, 0, 255) 
 
# Initialising pygame 
pygame.init() 
 
# Initialise game window 
pygame.display.set_caption('GeeksforGeeks Snakes') 
game_window = pygame.display.set_mode((window_x, window_y)) 
 
# FPS (frames per second) controller 
fps = pygame.time.Clock() 
 
# defining snake default position 
snake_position = [100, 50] 
 
# defining first 4 blocks of snake body 
snake_body = [[100, 50], 
              [90, 50], 
              [80, 50], 
              [70, 50] 
              ] 
# fruit position 
fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                  random.randrange(1, (window_y // 10)) * 10] 
 
fruit_spawn = True 
 
# setting default snake direction towards 
# right 
direction = 'RIGHT' 
change_to = direction 
 
# initial score 
score = 0 
 
 
# displaying Score function 
def show_score(choice, color, font, size): 
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size) 
 
    # create the display surface object 
    # score_surface 
    score_surface = score_font.render('Score : ' + str(score), True, color) 
 
    # create a rectangular object for the text 
    # surface object 
    score_rect = score_surface.get_rect() 
 
    # displaying text 
    game_window.blit(score_surface, score_rect) 
 
 
# game over function 
def game_over(): 
    # creating font object my_font 
    my_font = pygame.font.SysFont('times new roman', 50) 
 
    # creating a text surface on which text 
    # will be drawn 
    game_over_surface = my_font.render( 
        'Your Score is : ' + str(score), True, red) 
 
    # create a rectangular object for the text 
    # surface object 
    game_over_rect = game_over_surface.get_rect() 
 
    # setting position of the text 
    game_over_rect.midtop = (window_x / 2, window_y / 4) 
 
    # blit will draw the text on screen 
    game_window.blit(game_over_surface, game_over_rect) 
    pygame.display.flip() 
 
    # after 2 seconds we will quit the program 
    time.sleep(2) 
 
    # deactivating pygame library 
    pygame.quit() 
 
    # quit the program 
    quit() 
 
 
# Main Function 
while True: 
 
    # handling key events 
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: 
                change_to = 'UP' 
            if event.key == pygame.K_DOWN: 
                change_to = 'DOWN' 
            if event.key == pygame.K_LEFT: 
                change_to = 'LEFT' 
            if event.key == pygame.K_RIGHT: 
                change_to = 'RIGHT' 
 
    # If two keys pressed simultaneously 
    # we don't want snake to move into two 
    # directions simultaneously 
    if change_to == 'UP' and direction != 'DOWN': 
        direction = 'UP' 
    if change_to == 'DOWN' and direction != 'UP': 
        direction = 'DOWN' 
    if change_to == 'LEFT' and direction != 'RIGHT': 
        direction = 'LEFT' 
    if change_to == 'RIGHT' and direction != 'LEFT': 
        direction = 'RIGHT' 
 
    # Moving the snake 
    if direction == 'UP': 
        snake_position[1] -= 10 
    if direction == 'DOWN': 
        snake_position[1] += 10 
    if direction == 'LEFT': 
        snake_position[0] -= 10 
    if direction == 'RIGHT': 
        snake_position[0] += 10 
 
    # Snake body growing mechanism 
    # if fruits and snakes collide then scores 
    # will be incremented by 10 
    snake_body.insert(0, list(snake_position)) 
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]: 
        score += 10 
        fruit_spawn = False 
    else: 
        snake_body.pop() 
 
    if not fruit_spawn: 
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                          random.randrange(1, (window_y // 10)) * 10] 
 
    fruit_spawn = True 
    game_window.fill(black) 
 
    for pos in snake_body: 
        pygame.draw.rect(game_window, green, 
                         pygame.Rect(pos[0], pos[1], 10, 10)) 
    pygame.draw.rect(game_window, white, pygame.Rect( 
        fruit_position[0], fruit_position[1], 10, 10)) 
 
    # Game Over conditions 
    if snake_position[0] < 0 or snake_position[0] > window_x - 10: 
        game_over() 
    if snake_position[1] < 0 or snake_position[1] > window_y - 10: 
        game_over() 
 
    # Touching the snake body 
    for block in snake_body[1:]: 
        if snake_position[0] == block[0] and snake_position[1] == block[1]: 
            game_over() 
 
    # displaying score continuously 
    show_score(1, white, 'times new roman', 20) 
    # Refresh game screen 
    pygame.display.update() 
 
    # Frame Per Second /Refresh Rate 
    fps.tick(snake_speed) 

