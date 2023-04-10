import random

#set up pygame stuff
pygame.init()  
pygame.display.set_caption("top down game")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

#game variables
timer = 0 #used for sheep movement
score = 0

#images and fonts
SheepPic = pygame.image.load("C:/Users/793767/Desktop/sheep/sheep.jpg")
PlayerPic = pygame.image.load("C:/Users/793767/Desktop/sheep/player.jpg")
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score:', True, (200, 200, 0))
text2 = font.render(str(score), True, (200, 200, 0))
text3 = font.render('YOU KICKED CARTMANS BUTT!', True, (200, 200, 0))

#CONSTANTS (not required, just makes code easier to read)
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

#function defintions------------------------------------
#can you tell me what the parameters are for these functions, and what they return (if anything)?
def sheepMove(position):
    if timer % 100 == 0: #only change direction every 50 game loops
        position[2] = random.randrange(0, 4) #set random direction
    if position[2] == LEFT:
        if position[0] > 0:
            position[0]-=5 #move left
        else:
            position[2]=RIGHT
    elif position[2] == RIGHT:
        if position[0]+70 < 800:
            position[0] += 5 #move right
        else:
            position[2]=LEFT
    elif position[2] == UP: 
        if position[1] >50: 
            position[1] -=5 #move up
        else:
            position[1] == DOWN
    elif position[2] == DOWN:
        if position[1]+50 < 800:
            position[1] +=5
        else:
            position[1] == UP
    return position

def collision(PlayerX, PlayerY, sheepInfo):
    if PlayerX+40 > sheepInfo[0]: #check right edge of player against left edge of animal
       if PlayerX < sheepInfo[0]+80: #checking left edge of player against right edge of animal
           if PlayerY+40 >sheepInfo[1]:
               if PlayerY < sheepInfo[1]+40:
                   if sheepInfo[3] == False: #only catch uncaught sheeps!
                    sheepInfo[3] = True #catch da sheepies!
                    global score #make it so this function can change this value
                    score +=1



#create sheep!
#numbers in list represent xpos, ypos, direction moving, and whether it's been caught or not!
sheep1 = [200, 400, RIGHT, False]
sheep2 = [300, 500, LEFT, False]
sheep3 = [400, 500, LEFT, False]
sheep4 = [350, 550, RIGHT, False]
sheep5 = [770, 200, LEFT, False]
sheep6 = [600, 500, RIGHT, False]
#make more sheeps here!



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity (left/right speed) of player
vy = 0 #y velocity (up/down speed) of player
keys = [False, False, False, False] #this list holds whether each key has been pressed



while score<6: #GAME LOOP############################################################
    clock.tick(60) #FPS
    timer+=1
    
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        #check if a key has been PRESSED
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True

        #check if a key has been LET GO
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
          
    #physics
    #section--------------------------------------------------------------------
    
    #player movement!--------
    if keys[LEFT] == True:
        vx = -3
    elif keys[RIGHT] == True:
        vx = 3
    else:
        vx = 0
  
    if keys[DOWN]== True:
        vy = 3
    elif keys[UP]== True:
        vy= -3
    else:
        vy= 0


    #player/sheep collision!
    collision(xpos, ypos, sheep1)
    collision(xpos, ypos, sheep2)
    collision(xpos, ypos, sheep3)
    collision(xpos, ypos, sheep4)
    collision(xpos, ypos, sheep5)
    collision(xpos, ypos, sheep6)
    
    
    #update player position
    xpos+=vx 
    ypos+=vy
    
    #update sheep position
    sheep1 = sheepMove(sheep1)
    sheep2 = sheepMove(sheep2)
    sheep3 = sheepMove(sheep3)
    sheep4 = sheepMove(sheep4)
    sheep5 = sheepMove(sheep5)
    sheep6 = sheepMove(sheep6)
    
    # RENDER
    # Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    #draw player
    screen.blit(PlayerPic, (xpos,ypos,40,40))
    #draw sheep
    if sheep1[3] == False: #don't draw them if they're already caught!
        screen.blit(SheepPic, (sheep1[0], sheep1[1]))
    
    if sheep2[3] == False:
        screen.blit(SheepPic, (sheep2[0], sheep2[1]))
        
    if sheep3[3] == False: #don't draw them if they're already caught!
        screen.blit(SheepPic, (sheep3[0], sheep3[1]))
    
    if sheep4[3] == False:
        screen.blit(SheepPic, (sheep4[0], sheep4[1]))

    if sheep5[3] == False: #don't draw them if they're already caught!
        screen.blit(SheepPic, (sheep5[0], sheep5[1]))
    
    if sheep6[3] == False:
        screen.blit(SheepPic, (sheep6[0], sheep6[1]))
        
    #display score
    screen.blit(text, (20, 20))
    text2 = font.render(str(score), True, (200, 200, 0))#update score number
    screen.blit(text2, (140, 20))

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------

#end screen
screen.fill((0,0,0)) 
screen.blit(text3, (100,100))
pygame.display.flip()
pygame.time.wait(2000)#pause for a bit before ending

pygame.quit()
