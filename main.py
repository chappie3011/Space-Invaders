#############################################################################################################
#                                              --SPACE_INVADER --                                           #
 
#                                              Author: Ishan Shukla                                         #
 
#                                              Description: Blah Blah                                       #
 
#                                                                                                           #
 
#                                                                                                           #
 
#                                                                                                           #
 
#                                                                                                           #
#############################################################################################################
 
#Import Libraries
 
import pygame
import random
#Screen Constants
 
XMODE = 800
YMODE = 600
SHIPX = 75
SHIPY = 60
 
pygame.init()
 
 
 
# Game Images                                                                                                                                                             
 
backImg = 'Images\\starfield.png'
bg = pygame.image.load(backImg)
bg = pygame.transform.scale(bg, (XMODE, YMODE))
defImg = 'Images\\ship.png'
defender = pygame.image.load(defImg)
defender = pygame.transform.scale(defender, (SHIPX, SHIPY))
defender.set_colorkey((0, 0, 0))
playerx=370
playery=480
playerx_change=0
# Setup Screen
 
screen = pygame.display.set_mode((XMODE, YMODE))
 
# Game loop
 
 
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
 
 
 
 
 
 
over_font=pygame.font.Font("freesansbold.ttf",64)
 
def game_over_text():
    over_text1=over_font.render("Game Over",True,(255,255,255))
    screen.blit(over_text1,(200,250))
 
 
 
 
 
 
enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_enemies=6
for i in range(num_enemies):
    enemyimg.append(pygame.image.load("Images\\invader.png")) 
    
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(15,200))
    enemyx_change.append(4)
    enemyy_change.append(15)
 
 
 
bulletimg=pygame.image.load("Images\\bullet.jpg")
bulletx=0
bullety=480 
bulletx_change=0
bullety_change=10
bullet_state="ready"
 
 
 
 
 
def player(x,y):
    screen.blit(defender,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
 
 
 
 
 
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    
    screen.blit(bulletimg,(x+16,y+10))
    
 
 
 
 
 
def iscollision(enemyx,enemyy,bulletx,bullety):
    
    dis=(((enemyx-bulletx)**2)+((enemyy-bullety)**2))**0.5
    if dis<=27: 
        return True
    else:
        return False
 
 
 
 
 
 
running=True
while running:
    
    screen.fill((0,0,0))
    
    screen.blit(bg,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
          
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT:
                
                playerx_change= -10
            if event.key==pygame.K_RIGHT:
                
                playerx_change= 10
            
            if event.key==pygame.K_SPACE:
                
                if bullet_state=="ready":
                    
                    
                    
                    bulletx=playerx
                    fire_bullet(bulletx,bullety)
                
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                
                playerx_change=0
            
    
    playerx+=playerx_change
    
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736
        
    
    for i in range(num_enemies):
        
        
        if enemyy[i]>400:
            for j in range(num_enemies):
                enemyy[j]=2000
            game_over_text()
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=8
            
            enemyy[i]=enemyy[i]+enemyy_change[i]
 
        elif enemyx[i]>=736:
            enemyx_change[i]=-8
            
            enemyy[i]=enemyy[i]+enemyy_change[i]
        
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            
            bullety=480
            bullet_state="ready"
            enemyx[i]=random.randint(0,736)
            enemyy[i]=random.randint(15,200)
            score_value+=1        
    
    
    if bullety<=0:
        bullety=480
        bullet_state="ready"
        
    
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
        
    
    
    player(playerx,playery)
    
    show_score(textx,texty)
    
    for i in range(num_enemies):
        enemy(enemyx[i],enemyy[i],i)
    
    pygame.display.update()
 
 
 
 
 
 

