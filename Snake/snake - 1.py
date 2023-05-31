import pygame
import random
pygame.init()
window=pygame.display.set_mode((550,550))
pygame.display.set_caption('Snake')
clock=pygame.time.Clock()

bg=pygame.image.load('pngwing.com.png')
bg1=pygame.image.load('pngwing.com (1).png')

pygame.display.set_icon(bg)

def plot(window,green,sl,size):
        for i,j in sl:
            pygame.draw.rect(window,green,[i,j,size,size])



font=pygame.font.Font('freesansbold.ttf',23)
def textwin(text,color,x,y):
        screen=font.render(text,True,color)
        window.blit(screen,[x,y])


def changecolor():
    
    global snakecolor
    black=(0,0,0)
    green=(0,255,0)
    white=(255,255,255)
    S="(APPLIED)"
    
    exit=False
    while not exit:
        window.fill((100,111,222))
        textwin("BLACK 'B'",(0,0,0),150,200)
        textwin("GREEN 'G'",(0,255,0),150,250)
        textwin("WHITE 'W'",(255,255,255),150,300)
        textwin("PRESS BACKSPACE",(255,255,100),160,450)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    exit=True
                    

                if event.key==pygame.K_b:
                    snakecolor=black
                 
                    
                if event.key==pygame.K_g:
                    snakecolor=green
              
                if event.key==pygame.K_w:
                    snakecolor=white
            
        if snakecolor==black:
            textwin(S,(255,0,0),300,200)
        if snakecolor==green:
            textwin(S,(255,0,0),300,250)
        if snakecolor==white:
            textwin(S,(255,0,0),300,300)
        pygame.display.update()
        
                    
    return snakecolor



def options():
    global fps
    global snakecolor
    fps=50
    snakecolor=(0,255,0)
    exit=False
    while not exit:
        window.fill((222,111,222))
        textwin("CHANGE FPS 'Y' or 'N':"+" "+str(fps),(0,0,0),110,200)
        textwin("CHANGE SNAKE COLOUR 'S'",(0,0,0),110,250)
        textwin("APPLY (PRESS 'SPACE')",(255,0,0),140,450)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                quit()
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_y:
                    fps=70 
                if event.key==pygame.K_n:
                    fps=50   
                    
                if event.key==pygame.K_s:
                    snakecolor=changecolor()  

                if event.key==pygame.K_SPACE:
                    if fps==50:
                        gameloop(fps,snakecolor)
                    
                    else:
                        gameloop(fps,snakecolor)
                    
                if event.key==pygame.K_BACKSPACE:
                    exit=True
        
        pygame.display.update()
    
    

def welcome():
    
    exit=False
    while not exit:
        window.fill((20,200,2))
        window.blit(bg1,(170,60))
        textwin("~Welcome To Snake~",(0,0,0),150,200)
        font1=pygame.font.Font('freesansbold.ttf',40)
        screen1=font1.render("GAME",True,(20,20,100))
        window.blit(screen1,[205,240])
        textwin("PRESS 'SPACE' TO PLAY",(245,22,222),130,380)
        textwin("OPTIONS 'O'",(255,0,100),200,430)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop(fps=50,snakecolor=(0,255,0))

                if event.key==pygame.K_o:
                    options()
                
        pygame.display.update()
        clock.tick(60)
    quit()

def gameloop(fps,snakecolor):
    
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
    
    


    while not exit:
        
        if over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))        

            window.fill((0,0,0))
            textwin("GAME OVER, PRESS 'ENTER' TO RETRY",(255,2,2),50,225)
            textwin("YOUR SCORE IS: "+str(score),(255,2,2),150,270)
            textwin("HOME 'Y'",(255,2,2),220,450)
            
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop(fps=50,snakecolor=(0,255,0))
                    if event.key==pygame.K_y:
                        welcome()
        else:
            window.fill((150,150,20))
            for event in pygame.event.get():
               
                if event.type==pygame.QUIT:
                    exit=True

                if event.type==pygame.KEYDOWN:
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
            
            if abs(x-foodx)<18 and abs(y-foody)<18:
                score+=10
                foodx=random.randint(20,510)
                foody=random.randint(20,510)
                slen+=5
                if score>int(highscore):
                    highscore=score



            pygame.draw.rect(window,(255,0,0),[foodx,foody,size,size] )

            head=[]
            head.append(x)
            head.append(y)
            sl.append(head)
            if len(sl)>slen:
                del sl[0]

            if head in sl[:-1]:
                pygame.time.wait(2000)
                over =True  
                

            if x<5 or x>525 or y<5 or y>525:
                pygame.time.wait(2000)
                over=True
                
            x+=vx
            y+=vy
            pygame.draw.rect(window,snakecolor,[x,y,size,size] )

            plot(window,snakecolor,sl,size)


            textwin("Score: "+str(score),(255,255,255),5,5)
            textwin("Highscore: "+str(highscore),(255,255,255),350,5)
        clock.tick(fps)

        pygame.display.update()
    quit()

welcome()