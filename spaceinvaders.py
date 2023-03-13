import pygame #module which handles graphics, input, etc
import random
import time

#variables----------------------------------------------------------------------------------------
xpos = 400
ypos = 750
moveLeft = False
moveRight = False
shoot = False

#game variables--------------------------------------------------------------------------------
countdown = 0
lives = 3

pygame.init() #set up pygame
pygame.display.set_caption("Space Invaders!") #sets the window title
popup = pygame.display.set_mode((850,800)) #creates game screen
timer = pygame.time.Clock() #sets up clock
endgame = False #variable that runs game loop

#classes-------------------------------------------------------------------------------------------
class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
   
    def draw(self):
        if self.isAlive == True:
            pygame.draw.rect(popup, (250,0,250), (self.xpos, self.ypos, 40, 40))
   
    def move(self,time):
        if time %400 == 0:
            self.ypos +=100 #move down
            self.direction *=-1 #flip direction
            return 0 #resets timer to 0
        #move every time the timer increases by 100:
        if time %100 == 0:
            self.xpos+=50*self.direction #move right
        return time #doesnt reset if first if statement hasnt executed
   
    def collide(self, BulletX, BulletY):
        if self.isAlive: #only hit live aliens
            if BulletX > self.xpos and BulletX < self.xpos + 40 and BulletY < self.ypos +40 and BulletY > self.ypos: #check if bullet is below the top of the alien
                print("hit!")#for testing lol
                self.isAlive = False #sets alien to dead
                return False #set bullet to dead
        return True #otherwise  keep bullet alive
               
   
class Bullet:
    def __init__(self, xpos, ypos):
           self.xpos = xpos
           self.ypos = ypos
           self.isAlive = False
   
    def move (self, xpos, ypos):
           if self.isAlive == True: #only shoots live bullets
               self.ypos -= 10 #move up when shot
           if self.ypos < 0: #check if youve hit top of screen
               self.isAlive = False #set to dead
               self.xpos = xpos #reset player position
               self.ypos = ypos

    def draw(self):
            pygame.draw.rect(popup, (255,179,0), (self.xpos, self.ypos, 10, 20))
   
class Wall:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.numHits = 0
           
    def collide(self, BulletX, BulletY):
        if self.numHits < 3:
            if BulletX > self.xpos and BulletX < self.xpos + 40 and BulletY < self.ypos +40 and BulletY > self.ypos:
                print("hit!")#for testing lol
                self.numHits +=1 #sets alien to dead
                return False #set bullet to dead
        return True #otherwise  keep bullet alive
   
    def draw(self):
        if self.numHits ==0:
            pygame.draw.rect(popup,(30,144,255), (self.xpos, self.ypos, 40, 40))
        if self.numHits ==1:
            pygame.draw.rect(popup,(0,191, 255), (self.xpos, self.ypos, 40, 40))
        if self.numHits ==2:
            pygame.draw.rect(popup,(135,206,250), (self.xpos, self.ypos, 40, 40))

class Missle:
    def __init__(self):
        self.xpos = -10
        self.ypos = -10
        self.isAlive = False
    def move (self, xpos, ypos):
        if self.isAlive == True: #only shoots live bullets
            self.ypos += 10 #move down when shot
        if self.ypos < 0: #check if youve hit bottom of screen
            self.isAlive = False #set to dead
            self.xpos = xpos #reset player position
            self.ypos = ypos
    def draw(self):
        if self.isAlive == True : 
            pygame.draw.rect(popup, (255,179,0), (self.xpos, self.ypos, 10, 10))


#for loops to create multiple objects----------------------------------------------------------
missles = []
for i in range(10):
    missles.append(Missle())
   
armada = [] #empty list
for i in range(4): #handles rows
    for j in range(9): #handles columns
        armada.append(Alien(j*80+50, i*90+50)) #push alien objects into list
        
walls=[]
for k in range (4):
    for i in range (2):
        for j in range (3):
            walls.append(Wall(j*40+200*k+50, i*40+600))

#instantiate bullet object------------------------------------------------------------------------
bullet = Bullet(xpos+28, ypos)

#gameloop------------------------------------------------------------------------------------------
while lives > 0: 
    timer.tick(60) #fps
    countdown += 1

#input section ----------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = True #quit game if X is clicked in top corner of game screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
        elif event.type == pygame.KEYUP:
            if event.key ==  pygame.K_LEFT:
                moveLeft = False
               
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight = True
        elif event.type == pygame.KEYUP:
            if event.key ==  pygame.K_RIGHT:
                moveRight = False
               
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot = True
        elif event.type == pygame.KEYUP:
            if event.key ==  pygame.K_SPACE:
                shoot = False
               
#physics section---------------------------------------------------------------------

#check variables
    if moveLeft == True:
        vx =-5
    elif moveRight == True:
        vx = 5
    else:
        vx = 0
       
    for i in range (len(armada)):
        countdown = armada[i].move(countdown)
    for i in range(len(missles)):
        missles[i].move(-10,-10)
    
    for i in range (len(walls)):
        for j in range(len(missles)):
            if missles[j].isAlive == True:
                if walls[i].collide(missles[j].xpos, missles[j].ypos) == False:
                    missles[j].isAlive = False
                    break
    
    enemyfire =  random.randrange(100)
    if enemyfire < 2:
        select = random.randrange(len(armada))
        if armada[select].isAlive == True:
            for i in range (len(missles)):
                if missles[i].isAlive == False:
                    missles[i].isAlive = True
                    missles[i].xpos = armada[select].xpos+8
                    missles [i].ypos = armada[select].ypos
                    break
    
    for i in range (len(missles)):
        if missles[i].isAlive:
            if missles[i].xpos > xpos:
                if missles[i].xpos < xpos +70:
                    if missles[i].ypos < ypos +70:
                        if missles[i].ypos > ypos:
                            print("PLAYER HIT!")
                            lives -=1
                            time.sleep(1)
                            xpos = 400
                            
                            
#update player position
    xpos += vx
    
    
#render section----------------------------------------------------------------------
    popup.fill((0,0,0)) #wipes screen
    wall=Wall(150, 450)
   
    #draw all aliens in list:
    bullet.draw()
    for i in range(len(armada)):
        armada[i].draw()
    for i in range(len(walls)):
        walls[i].draw()
    for i in range(len(missles)):
        missles[i].draw()
       
    if lives == 3:
        pygame.draw.rect(popup, (20,255,50), (700,20,50,20))
    if lives >=2:
        pygame.draw.rect(popup, (20,255,50), (600,20,50,20))
    if lives >= 1:
         pygame.draw.rect(popup, (20,255,50), (500,20,50,20))
    

         
    if shoot == True:
        bullet.isAlive = True
   
    if bullet.isAlive == True:
        bullet.move(xpos+28, ypos)
        if bullet.isAlive == True:
            for i in range (len(armada)):
                bullet.isAlive = armada[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isAlive == False:
                    break
        if bullet.isAlive == True:
            for i in range(len(walls)):
                bullet.isAlive = walls[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isAlive == False:
                    break
    else:
        bullet.xpos = xpos +45
        bullet.ypos = ypos
       
    pygame.draw.rect(popup, (20,255,50), (xpos,750,100,20)) #draw player
    pygame.draw.rect(popup, (20,255,50), (xpos+5, 740,90,20))
    pygame.draw.rect(popup, (20,255,50), (xpos+40, 720,20,20))
    pygame.draw.rect(popup, (20,255,50), (xpos+45, 700,10,20))
    pygame.display.flip() #flips memory where stuff had been drawn to the screen
   
#end game loop----------------------------------------------------------------------
pygame.quit()
print("Game Over!")
