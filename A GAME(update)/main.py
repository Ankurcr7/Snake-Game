import pygame
import random
import math
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((800,600))

background=pygame.image.load("pygame\space-galaxy-background.jpg")

mixer.music.load('pygame\WhatsApp Audio 2023-05-02 at 15.06.39.mp3')
mixer.music.play(-1)

pygame.display.set_caption("lol")
icon=pygame.image.load("pygame\dj.png")
pygame.display.set_icon(icon)



playerimg=pygame.image.load('pygame\\arcade-game.png')
playerx=384
playery=550
changex=0
changey=0


enemyimg=[]
enemyx=[]
enemyy=[]
ex=[]
ey=[]
numofenemies=5
for i in range(numofenemies):
    enemyimg.append(pygame.image.load('pygame\\ufo.png'))
    enemyx.append(random.randint(32,768))
    enemyy.append(random.randint(32,68))
    ex.append(0.3)
    ey.append(40)


# enemyimg=pygame.image.load('ufo.png')
# enemyx=random.randint(32,768)
# enemyy=random.randint(32,68)
# ex=0.3
# ey=40

bulletimg=pygame.image.load('pygame\\bullet.png')
bulletx=0
bullety=550
bullx=0
bully=0.75
bulletstate="ready"

# score=0
scorevalue=0
font=pygame.font.Font('freesansbold.ttf',25)
textx=10
texty=10

over=pygame.font.Font('freesansbold.ttf',64)

def showscore(x,y):
    score=font.render("Score: "+str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y)) 

def gameover():
    overfont=over.render("GAME OVER",True,(255,255,255))
    screen.blit(overfont,(210,250)) 


def player(x,y):
    screen.blit(playerimg,(x,y)) 

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y)) 

def fire(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x,y))

def collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow((enemyx-bulletx),2))+ (math.pow((enemyy-bullety),2)))
    if distance<27:
        return True
    else:
        return False

running=True
while running:
    screen.fill((0, 0, 0))

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT:
                changex=-0.3
            if event.key==pygame.K_RIGHT:
                changex=0.3
            if event.key==pygame.K_UP:
                changey=-0.3
            if event.key==pygame.K_DOWN:
                changey=0.3
            if event.key==pygame.K_SPACE:
                
                if bulletstate=="ready":
                    bulletsound= mixer.Sound('pygame\laser-gun-81720.mp3')
                    bulletsound.play()
                    bulletx=playerx
                    bullety=playery-30

                    fire(bulletx,bullety)
        

            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN :
                changex=0
                changey=0
                


    playerx+=changex   
    playery+=changey  

    if playerx<=0:
        playerx=0
    elif playerx>=768:
        playerx=768

    elif playery<=0:
        playery=0
    elif playery>=568:
        playery=568
    
    for i in range(numofenemies):
        if enemyy[i]>550:
            for j in range(numofenemies):
                enemyy[j]=2000
            gameover()
            break

        enemyx[i]+=ex[i]
    # enemyx+=ex   
        if enemyx[i]<=0:
            ex[i]=0.3
            enemyy[i] += ey[i] #+ enemyy
        elif enemyx[i]>=768:
            ex[i]=-0.3
            enemyy[i] += ey[i] #+ enemyy

        coll=collision(enemyx[i],enemyy[i],bulletx,bullety)
        if coll:
            explodesound= mixer.Sound('pygame\explosion-6055.mp3')
            explodesound.play()
            bullety=playery
            bulletstate="ready"
            scorevalue+=1
            enemyx[i]=random.randint(32,768)
            enemyy[i]=random.randint(32,68)
            
            
        enemy(enemyx[i],enemyy[i],i)

    if bullety<=0:
        #bullety=playery
        bulletstate="ready"

    if bulletstate is "fire":
        fire(bulletx,bullety)
        bullety-=bully
    

    player(playerx,playery)
    showscore(textx,texty)
    pygame.display.update()