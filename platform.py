import pygame
pygame.init()  

gamescreen = pygame.display.set_mode((800,800))
mario = pygame.image.load("mario.jpg")



pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3


#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform



while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
            
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
            
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT
    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    
    

    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >600 and ypos+40 <620:
        ypos = 600-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >700 and ypos+40 <720:
        ypos = 700-40
        isOnGround = True
        vy = 0
    elif xpos>445 and xpos<545 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >500 and ypos+40 <520:
        ypos = 500-40
        isOnGround = True
        vy = 0
    
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    gamescreen.blit(mario, (100,400))
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (170, 650, 100, 20))
    
    #my platforms
    pygame.draw.rect(screen, (200, 0, 200), (300, 600, 100, 20))
    
    pygame.draw.rect(screen, (200, 200, 0), (300, 700, 100, 20))
    
    pygame.draw.rect(screen, (0, 200, 200), (445, 650, 100, 20))
    
    pygame.draw.rect(screen, (200, 200, 200), (500, 750, 100, 20))
    
    pygame.draw.rect(screen, (100, 150, 200), (300, 500, 100, 20))
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
