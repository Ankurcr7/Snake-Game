import pygame
import random
from pygame import mixer

pygame.init()
window=pygame.display.set_mode((550,550))
pygame.display.set_caption('Snake')
clock=pygame.time.Clock()

eating='eating-sound-effect-36186.mp3'



bg=pygame.image.load('pngwing.com.png')
bg1=pygame.image.load('pngwing.com (1).png')

pygame.display.set_icon(bg)

def plot(window,green,sl,size):
        for i,j in sl:
            pygame.draw.rect(window,green,[i,j,size,size],0,7)



font=pygame.font.Font('freesansbold.ttf',23)
def textwin(text,color,x,y):
        screen=font.render(text,True,color)
        window.blit(screen,[x,y])

def how():
    exit=False
    while not exit:
        window.fill((40,40,40))
        font2=pygame.font.Font('freesansbold.ttf',33)
        screen=font2.render("Snake Movements:-",True,(255,255,255))
        window.blit(screen,[20,20])
        textwin("DIRECTION UP -> PRESS UP KEY",(200,200,200),20,80)
        textwin("DIRECTION DOWN -> PRESS DOWN KEY",(200,200,200),20,110)
        textwin("DIRECTION LEFT -> PRESS LEFT KEY",(200,200,200),20,140)
        textwin("DIRECTION RIGHT -> PRESS RIGHT KEY",(200,200,200),20,170)
        textwin("How to Score:-",(255,255,255),20,220)
        textwin("If you eat the food displayed on the screen,",(200,200,200),20,260)
        textwin("then the length of Snake increase",(200,200,200),20,290)
        textwin("BACK",(2,250,200),240,500)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                x=pos[0]
                y=pos[1]
                mousepress=pygame.mouse.get_pressed()
                if x>240 and x<305 and y>500 and y<520:
                    exit=True

        pygame.display.update()


def pause(fps,snakecolor):
    sh.stop()
    exit=False
    while not exit:
        window.fill((90,90,50))
        
        textwin("RESUME",(2,250,100),223,200)
        textwin("RESTART",(2,210,200),220,260)
        textwin("HOME",(2,210,200),235,320)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                x=pos[0]
                y=pos[1]
            
                mousepress=pygame.mouse.get_pressed()
                if x>223 and x<320 and y>200 and y<220:
                    exit=True
                if x>220 and x<325 and y>260 and y<280:
                    if fps>50:
                        cl1.stop()
                        # os2=oversound()
                        # os2.stop()
                        gameloop(fps,snakecolor)
                    else:
                        cl1.stop()
                        # os2=oversound()
                        # os2.stop()
                        gameloop(fps,snakecolor)
                if x>235 and x<306 and y>320 and y<340:
                    cl1.stop()
                    os2=oversound()
                    os2.stop()
                    welcome()
        pygame.display.update()

def changecolor():
    
    global snakecolor
    black=(0,0,0)
    green=(0,255,0)
    white=(255,255,255)
    S="(APPLIED)"
    
    exit=False
    while not exit:
        window.fill((100,111,222))
        textwin("BLACK ",(0,0,0),150,200)
        textwin("GREEN ",(0,255,0),150,250)
        textwin("WHITE ",(255,255,255),150,300)
        textwin("BACK",(255,255,100),240,500)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                quit()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                x=pos[0]
                y=pos[1]
                
                mousepress=pygame.mouse.get_pressed()
                if x>240 and x<305 and y>500 and y<520:
                    exit=True
                if x>150 and x<230 and y>200 and y<220:
                    snakecolor=black
                if x>150 and x<230 and y>250 and y<270:
                    snakecolor=green
                if x>150 and x<230 and y>300 and y<320:
                    snakecolor=white
                
                
            
        if snakecolor==black:
            textwin(S,(255,0,0),300,200)
        if snakecolor==green:
            textwin(S,(255,0,0),300,250)
        if snakecolor==white:
            textwin(S,(255,0,0),300,300)
        pygame.display.update()
        
                    
    return snakecolor



def options(cl2):
    global fps
    global snakecolor
    fps=50
    snakecolor=(0,255,0)
    exit=False
    while not exit:
        window.fill((222,111,222))
        textwin("CHANGE FPS : "+"50 or 70",(0,0,0),110,200)
        
        textwin("CHANGE SNAKE COLOUR",(0,0,0),110,250)
        textwin("START",(25,0,240),237,450)
        textwin("BACK",(0,0,0),240,500)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                quit()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                x=pos[0]
                y=pos[1]
                
                mousepress=pygame.mouse.get_pressed()
                if x>240 and x<305 and y>500 and y<520:
                    exit=True
                if x>110 and x<410 and y>250 and y<270:
                    snakecolor=changecolor()
                if x>235 and x<310 and y>450 and y<470:
                    cl2.stop()
                    gameloop(fps,snakecolor)
                if x>340 and x<373 and y>195 and y<225:
                    fps=70
                if x>280 and x<312 and y>195 and y<225:
                    fps=50
                
        if fps==70:
            pygame.draw.rect(window,(255,0,0),(340,195,33,30),2)
                
        if fps==50:
            pygame.draw.rect(window,(255,0,0),(280,195,32,30),2) 
            
        pygame.display.update()
    
    

def welcome():
    l=['motivational-corporate-medium1-110677.mp3','Luke-Bergs-Tropical-Soulmp3.mp3']
    cl=random.choice(l)
    cl2=mixer.Sound(cl)
    cl2.play(-1)
    cl2.set_volume(0.4)

    fps=50
    snakecolor=(0,255,0)
    exit=False
    while not exit:

        window.fill((20,150,2))
        window.blit(bg1,(170,60))
        textwin("~Welcome To Snake~",(0,0,0),150,200)
        font1=pygame.font.Font('freesansbold.ttf',40)
        screen1=font1.render("GAME",True,(20,50,100))
        window.blit(screen1,[208,240])
        textwin("START",(24,12,222),235,380)
        textwin("OPTIONS",(255,0,100),215,430)
        textwin("HOW TO PLAY",(255,160,0),190,480)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            
                    
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                x=pos[0]
                y=pos[1]
               
                mousepress=pygame.mouse.get_pressed()
                if x>235 and x<308 and y>380 and y<400:
                    cl2.stop()
                    gameloop(fps,snakecolor)

                if x>215 and x<322 and y>434 and y<450:
                   
                    options(cl2)
                if x>190 and x<350 and y>480 and y<500:
                   
                    how()
                
        pygame.display.update()
        clock.tick(60)
    quit()

def snakehiss():
    global sh
    shiss='snake-hiss-95241.mp3'
    sh=mixer.Sound(shiss)
    return sh



def oversound():
    global os2
    os=['floating-in-time-145495.mp3','floating-abstract-142819.mp3']
    os1=random.choice(os)
    os2=mixer.Sound(os1)
    os2.play(-1)
    os2.set_volume(0.3)
    return os2
    

def gameloop(fps,snakecolor):
    global cl1
    
    exit=False
    over=False
    
   
    x=50
    y=50
    size=20
    
    
    vx=0
    vy=0
    foodx=random.randint(20,510)
    foody=random.randint(20,510)




    sl=[]
    slen=0
    
    with open("highscore.txt","r") as f:
        highscore=f.read()        

    
    score=0 
    l='gamemusic-6082.mp3'
    cl1=mixer.Sound(l)
    cl1.play(-1)
    cl1.set_volume(0.25)

    s=snakehiss()
    

    while not exit:
        
        
        if over:
            cl1.stop()
            
            with open("highscore.txt","w") as f:
                f.write(str(highscore))        

            window.fill((0,0,0))
            textwin("GAME OVER",(255,2,2),195,225)
            textwin("YOUR SCORE IS: "+str(score),(250,200,110),150,270)
            textwin("RETRY",(255,255,2),226,400)
            textwin("HOME",(255,2,255),230,450)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit=True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x=pos[0]
                    y=pos[1]
                    
                    mousepress=pygame.mouse.get_pressed()
                    if x>225 and x<305 and y>400 and y<420:
                        cl1.stop()
                        os2.stop()
                        gameloop(fps,snakecolor)

                    if x>230 and x<300 and y>450 and y<470:
                        cl1.stop()
                        os2.stop()
                        welcome()
        
        else:
            window.fill((150,150,20))
            pygame.draw.rect(window,(255,255,255),[525,5,20,20],1,100)
            pygame.draw.rect(window,(255,255,255),[530,9,2,12])
            pygame.draw.rect(window,(255,255,255),[537,9,2,12])
            
            for event in pygame.event.get():
               
                if event.type==pygame.QUIT:
                    exit=True

                if event.type==pygame.KEYDOWN:
                    s.play()
                    s.set_volume(0.1)
                    if event.key==pygame.K_RIGHT:
                        vx=5   
                        vy=0
                    if event.key==pygame.K_LEFT:
                        vx=-5
                        vy=0     
                    if event.key==pygame.K_UP:
                        vy=-5
                        vx=0    
                    if event.key==pygame.K_DOWN:
                        vy=5
                        vx=0     
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    px=pos[0]
                    py=pos[1]
               
                    mousepress=pygame.mouse.get_pressed()
                    if px>525 and px<545 and py>5 and py<25:
                    
                        pause(fps,snakecolor)
                        
            
            if abs(x-foodx)<18 and abs(y-foody)<18:
                score+=10
                mixer.music.load(eating)
                mixer.music.play(1)
                mixer.music.set_volume(0.4)
                
                foodx=random.randint(20,510)
                foody=random.randint(20,510)
                slen+=5
                if score>int(highscore):
                    highscore=score



            pygame.draw.rect(window,(255,0,0),[foodx,foody,size,size],0,3)

            head=[]
            head.append(x)
            head.append(y)
            sl.append(head)
            if len(sl)>slen:
                del sl[0]

            if head in sl[:-1]:
                pygame.time.wait(2000)
                
                oversound()
                s.stop()
                over =True  
                

            if x<5 or x>525 or y<5 or y>525:
                pygame.time.wait(2000)
                
                oversound()
                s.stop()
                over=True
                
            x+=vx
            y+=vy
            pygame.draw.rect(window,snakecolor,[x,y,size,size],0,7)

            plot(window,snakecolor,sl,size)


            textwin("Score: "+str(score),(255,255,255),5,5)
            textwin("Highscore: "+str(highscore),(255,255,255),200,5)
        clock.tick(fps)

        pygame.display.update()
    
        

    quit()
    
welcome()