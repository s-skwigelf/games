# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:57:04 2020

@author: harsh
"""

# --------- MY GAME IN PYTHON WITH PYGAME - SPACE INVADER LIKE CONCEPT ----------

import pygame as pg
from pygame import mixer as mx
import random
import math as m

#initalizing pygame
pg.init()

#creating the game window
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("My Space Invaders type game")
#icon = pg.image.load('name of the image')
#pg.display.set_icon(icon)

#background = pg.image.load('name of the bg image') should be of the same dimension as the game window

#background sound
#mx.music.load('filename')
#mx.music.play(-1) 

#adding an image
#the player
player = pg.image.load('ssicon.png')
playerX = 370
playerY = 480
x_change = 0
y_change = 0

#the enemy
enemy = []
enemyX = []
enemyY = [] 
ex_change = []
ey_change = [] 
nene = 6
for i in range(nene):
    enemy.append(pg.image.load('enemyship.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))
    ex_change.append(0.4)
    ey_change.append(30)

#the bullet
bullet = pg.image.load('bullet.png')
bulletX = 0
bulletY = 480
bx_change = 0
by_change = 1.5
b_state = "ready"

#score 
score_value = 0
font = pg.font.Font('freesansbold.ttf', 24)
textX = 10
textY = 10

def scoring(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def play(x, y):
    screen.blit(player, (x, y))

def eneplay(x, y, i):
    screen.blit(enemy[i], (x, y))
    
def fire_bullet(x, y):
    global b_state
    b_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))
    
def collision(enemyX, enemyY, bulletX, bulletY):
    dist = m.sqrt((m.pow(enemyX - bulletX, 2)) + (m.pow(enemyY - bulletY, 2)))
    if dist < 27:
        return True
    else:
        return False

over = pg.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text = over.render("GAME OVER" + str(score_value), True, (0, 0, 0))
    screen.blit(over_text, (200, 250)) 

#game loop where all the events of the game take place
running = True
while running:
    screen.fill((255, 255, 255))
    #background will come here on the next line. Increase the movement speed of the chars after adding bg.
    #screen.blit(background, (0, 0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change = -0.75
                #print("left pressed")
            if event.key == pg.K_RIGHT:
                x_change = +0.75
                #print("right pressed")
            if event.key == pg.K_SPACE:
                if b_state is "ready":
                    #adding bullet sound
                    #bullet_sound = mx.Sound('filename') 
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)  
                
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                x_change = 0
                
    #adding boundaries
    #for the player
    playerX += x_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    #for the enemy  
    for i in range(nene):
        #game over
        if enemyY[i] > 440:
            for j in range(nene):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += ex_change[i]
        if enemyX[i] <= 0:
            ex_change[i] = 0.4
            enemyY[i] += ey_change[i]
        elif enemyX[i] >= 736:
            ex_change[i] = -0.4
            enemyY[i] += ey_change[i] 
        
        #for the collision
        coln = collision(enemyX[i], enemyY[i], bulletX, bulletY) 
        if coln is True:
            #adding explosion sound
            #xpln_sound = mx.Sound('filename') 
            bulletY = 480
            b_state = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 150) 
            score_value += 1
        
        eneplay(enemyX[i], enemyY[i], i)
        
        
    #for the bullet
    if bulletY <= 0:
        bulletY = 480 
        b_state = "ready"
        
    if b_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= by_change

    play(playerX, playerY)
    scoring(textX, textY) 
    pg.display.update()
