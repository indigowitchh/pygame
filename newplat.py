import pygame
pygame.init()
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

LEFT=0
RIGHT=1
UP = 2
DOWN = 3

Link = pygame.image.load('C:/Users/793767/Downloads/pogoifhkpongkoghkfpngfpk (5).png')
Link.set_colorkey((255,0,255))

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False]
isOnGround = False

#controller = pygame.joystick.Joystick(0) 
#controller.init()


#animation variable
frameWidth = 160
frameHeight = 160
RowNum = 0
frameNum = 0
ticker = 0

while not gameover: #GAME LOOP
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0]=True
            
            elif event.key == pygame.K_RIGHT:
                keys[1]=True
            
            elif event.key == pygame.K_UP:
                keys[2]=True
            
            elif event.key == pygame.K_DOWN:
                keys[3]=True
    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0]=False
            
            elif event.key == pygame.K_RIGHT:
                keys[1]=False
            
            elif event.key == pygame.K_UP:
                keys[2]=False
            
            elif event.key == pygame.K_DOWN:
                keys[3]=False
                
    
    
    
#physics section--------------------------------------------------------------------
    
    #LEFT MOVEMENT
    if keys[0]==True:
        vx=-3
    #RIGHT MOVEMENT
    elif keys[1]==True:
        vx=3
    else:
        vx = 0
    #UP MOVEMENT
    if keys[2]==True:
        vy=-3
    elif keys[3]==True:
        vy=3
    else:
        vy = 0
    #turn off velocity
    
        #JUMPING
   #stop falling if on bottom of game screen
    if ypos > 700:
        isOnGround = True
        vy = 0
        ypos = 700
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    #xVel = controller.get_axis(0) #returns a number b/t -1 and 1
    #yVel = controller.get_axis(1) #returns a number b/t -1 and 1
    #xpos += int(xVel * 10)
    #ypos += int(yVel * 10)
    
#animation  sec-------------------------------------------             
    if vx < 0: #or xVel < 0:
        RowNum = 0
        ticker+=1
        if ticker %20==0:
            frameNum+=1
        if frameNum>7:
            frameNum=0
    elif vx > 0: #or xVel > 0:
        RowNum = 1
        ticker+=1
        if ticker %20==0:
            frameNum+=1
        if frameNum>7:
            frameNum=0
    
    elif vy < 0: #or yVel < 0:
        RowNum = 2
        ticker+=1
        if ticker %20==0:
            frameNum+=1
        if frameNum>7:
            frameNum=0
    
    elif vy > 0: #or yVel > 0:
        RowNum = 3
        ticker+=1
        if ticker %20==0:
            frameNum+=1
        if frameNum>7:
            frameNum=0


#render section--------------------------------------------------
    screen.fill((134,134,175)) #wipe screen so it doesn't smear
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    pygame.display.flip()#this actually puts the pixel on the screen

#end loop--------------------
pygame.quit()
