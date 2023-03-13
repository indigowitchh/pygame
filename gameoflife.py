import pygame
import random

pygame.init()
pygame.display.set_caption("Game of life")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

# map = [[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
#        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
#        [0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0],
#        [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0],
#        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
#        [0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0],
#        [0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0],
#        [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
#        [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
#        [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
#        [0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0],
#        [0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0],
#        [0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
#        [0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0],
#        [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
#        ]
map = [[random.randrange(0,2)]*16 for i in range(16)]
print(map)

#Game loop--------------------------------------------------------------------------------
while True:
    clock.tick(40)
    event = pygame.event.wait()

    #Input section------------------------------------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break
        

    #Update section----------------------------------------------------------------------
    pygame.time.wait(200)
    


    for i in range(16):
        for j in range(16):
            counter = 0
            if i < 15 and map[i+1][j] ==1:#check to the right
                counter += 1
            if j < 15 and map[i][j+1] ==1:#check up
                counter += 1
            if i < 15 and j<15 and map[i+1][j+1] ==1: #check top right corner
                counter += 1
            if i < 15 and j>= 0 and map [i+1][j-1] == 1:#top left corner
                counter +=1 
            
            
            if i < 15 and map[i-1][j] ==1:#check to the left
                counter += 1
            if j < 15 and map[i][j-1] ==1:#check down
                counter += 1
            if i >= 0 and j >= 0 and map[i-1][j-1] ==1: #check top left corner
                counter += 1
            if i >= 0 and j < 15 and map [i-1][j+1] == 1: #top right corner
                counter +=1
                
       
            if map[i][j]==1 and counter <= 1:
                map[i][j] = 0
                print("Dies from no madams")
                
            if map[i][j]==1 and counter >= 4:
                map[i][j] = 0
                print("Dies from too many madams")
                
            if map[i][j]==0 and counter == 3:
                map[i][j] = 1
                print("Imma blow up")    
    #render section-----------------------------------------------------------------------
    screen.fill((0,0,0))
    
    for i in range(16):
        for j in range(16):
            if map[i][j] ==0:
                pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50,50))
                pygame.draw.rect(screen, (255,255,255), (j*50, i*50, 50,50),1)
            if map[i][j] ==1:
                pygame.draw.rect(screen, (0,200,200), (j*50, i*50, 50,50))
            
                    
    #Stuff gets drawn here----------------------------------------------------------------

    pygame.display.flip()

pygame.quit()
