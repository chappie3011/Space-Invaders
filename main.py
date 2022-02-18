#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame 
import random
from pygame import mixer
pygame.init()


# In[2]:


#dispaly screen
screen=pygame.display.set_mode((800,600))


# In[3]:


#title
pygame.display.set_caption('space invader')


# In[4]:


#image
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


# In[5]:


#backgrround image
background=pygame.image.load("background.png")

#background music
mixer.music.load("background.wav")
#-1 is for playing untill we stop game ,like a infinite loop
mixer.music.play(-1)


# In[6]:


#player
playerimg=pygame.image.load("space-invaders.png")
playerx=370
playery=480
playerx_change=0


# In[7]:


#score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


# In[8]:


#gamo_over_text
over_font=pygame.font.Font("freesansbold.ttf",64)

def game_over_text():
    over_text1=over_font.render("Game Over",True,(255,255,255))
    screen.blit(over_text1,(200,250))


# In[9]:


#enemy
#multiple enemies
enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_enemies=6
for i in range(num_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    #some random ppsition of enemy
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(15,200))
    enemyx_change.append(4)
    enemyy_change.append(15)


# In[10]:


#bullet
#ready=bullet cannot be seen but ready to fire  
#fire=bullet ill be seen firing
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=480 #bullet should come from the player
bulletx_change=0
bullety_change=10
bullet_state="ready"


# In[11]:


def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))


# In[12]:


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    #this +16,+10 is for seeing the bullet to be fired from the middle of spaceship
    screen.blit(bulletimg,(x+16,y+10))
    


# In[13]:


def iscollision(enemyx,enemyy,bulletx,bullety):
    #finding distance between bullet and enemy
    dis=(((enemyx-bulletx)**2)+((enemyy-bullety)**2))**0.5
    if dis<=27: 
        return True
    else:
        return False


# In[14]:


#for closing the window when x is clicked
running=True
while running:
    #for background color
    screen.fill((0,0,0))
    #printing background image from top left corner. position=(0,0)
    #as image is big it takes time for whle to execute and so our player and enemy gets slower  so increase speed
    screen.blit(background,(0,0))
    #increasing the x value of player
    #for going left -=is used
    #playerx+=0.2
    #playery-=0.2
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #this means if any key is pressed down    
        if event.type==pygame.KEYDOWN:
            #print("key is pressed")
            if event.key==pygame.K_LEFT:
                #print("left key is pressed")
                playerx_change= -10
            if event.key==pygame.K_RIGHT:
                #print("right key is pressed")
                playerx_change= 10
            #when space is pressed firing bullet
            if event.key==pygame.K_SPACE:
                
                if bullet_state=="ready":
                    #laser sound
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    
                    bulletx=playerx
                    fire_bullet(bulletx,bullety)
                
        #key is up means not clicked
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                #print("key is released")
                playerx_change=0
            
    #changing x while button is clikced
    playerx+=playerx_change
    #making boundaries
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736
        
    #enemy movements
    for i in range(num_enemies):
        
        #game over
        if enemyy[i]>400:
            for j in range(num_enemies):
                enemyy[j]=2000
            game_over_text()
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=8
            #bringing the enemy down when it comes to an end
            enemyy[i]=enemyy[i]+enemyy_change[i]

        elif enemyx[i]>=736:
            enemyx_change[i]=-8
            #bringing the enemy down when it comes to an end
            enemyy[i]=enemyy[i]+enemyy_change[i]
        #collosion
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            explosion_sound=mixer.Sound("explosion.wav")
            explosion_sound.play()
            
            bullety=480
            bullet_state="ready"
            enemyx[i]=random.randint(0,736)
            enemyy[i]=random.randint(15,200)
            score_value+=1        
    
    #when  it reaches end making bullet ready again
    if bullety<=0:
        bullety=480
        bullet_state="ready"
        
    #bullet movement
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
        
    
    #calling player
    player(playerx,playery)
    #score show
    show_score(textx,texty)
    #CALLING ENEMY
    for i in range(num_enemies):
        enemy(enemyx[i],enemyy[i],i)
    #confirm line that should be there in a game
    pygame.display.update()


# In[ ]:




