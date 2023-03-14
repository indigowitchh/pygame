import pygame
import random
import winsound
import math
pygame.init()#initializes Pygame
pygame.display.set_caption("Simon!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen

#game variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers in a TUPLE
turn = False
pattern = [] #this holds the random pattern
pi = 3.1415
playerPattern = []
hasClicked = False

#draw everything first so things don't appear one at a time
pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100) # RED
pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100) # Green
pygame.draw.arc(screen, (0,0,155), (200, 200, 400, 400), 0, (pi/2), 100) # Blue
pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi)/2, (0), 100) # Yellow
pygame.display.flip()

 #collision function-----
def collision(xpos, ypos):
    print("inside collision function")
    if math.sqrt((xpos-400)**2+(ypos-400)**2)>200 or math.sqrt((xpos-400)**2+(ypos-400)**2)<100 :
        print("Outside of ring!")
        return -1
    elif xpos < 400 and ypos <400:
        print("Over red button!")
        pygame.draw.arc(screen, (255, 0,0), (200,200,400,400), pi/2, pi, 100)
        pygame.display.flip()
        winsound.Beep(440, 500)
        return 0
    
    elif xpos<400 and ypos>400:
        print("Over green button!")
        pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
        pygame.display.flip()
        winsound.Beep(640, 500)        
        return 1
    
    elif xpos > 400 and ypos <400:
        print("Over blue button!")
        pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), 0, (pi/2), 100)
        pygame.display.flip()
        winsound.Beep(150, 500)
        return 2

    elif xpos>400 and ypos>400:
        print("Over yellow button!")
        pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), (3*pi)/2, (0), 100)
        pygame.display.flip()
        winsound.Beep(300, 500)
        return 3
    
#gameloop###################################################
while True:
    
    event = pygame.event.wait()#event queue 

    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        hasClicked = True 
        turn = True

    if event.type == pygame.MOUSEBUTTONUP:
        hasClicked = False 
        #turn = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
    
     #update section---------------------------------------------   
    
    #player turn
    if turn == True:
        print("Starting player turn!")
        if len(playerPattern) < len(pattern):
            if hasClicked == True:
                print("adding to player pattern")
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False
            for i in range(len(playerPattern)):
                if playerPattern[i]!=pattern[i]:
                    ded = True
                    winsound.Beep(200, 1200)
                    pygame.time.wait(500) #slows the game down a bit
                    playerPattern.clear()
                    pattern.clear()
                    turn = False
                
        else:
            turn = False
            pygame.time.wait(800)
        
            

#     collision(mousePos[0], mousePos[1])#collision call
    #machine turn
    if turn == False:      
        pattern.append(random.randrange(0, 4)) #push a new value into the pattern list
        
        #brighten colors and play beep for each number in the pattern
        for i in range(len(pattern)): 
            if pattern[i]==0: #RED
                pygame.draw.arc(screen, (255, 0,0), (200,200,400,400), pi/2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)
                
            elif pattern[i]==1:#GREEN
                pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)

            elif pattern[i]==2:#BLU
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), 0, (pi/2), 100)
                pygame.display.flip()
                winsound.Beep(150, 500)

            elif pattern[i]==3:#YELLOW
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), (3*pi)/2, (0), 100)
                pygame.display.flip()
                winsound.Beep(300, 500)
     

            
            #redraw board after every beep
            pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100) #red
            pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100) #green
            pygame.draw.arc(screen, (0,0,155), (200, 200, 400, 400), 0, (pi/2), 100) #blue
            pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi)/2, (0), 100)#yellow
            pygame.display.flip()
            pygame.time.wait(200) #slows the game down a bit
            playerPattern.clear()
            turn = True
            
    #render section---------------------------------------------
    
    #game board
    pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
    pygame.draw.arc(screen, (0,0,155), (200, 200, 400, 400), 0, (pi/2), 100) 
    pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi)/2, (0), 100)
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()
