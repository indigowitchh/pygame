import pygame
import random
pygame.init() #initializes Pygame
pygame.display.set_caption("Valentine's day card") #sets the window title
screen = pygame.display.set_mode((1000, 1000)) #creates game screen
font = pygame.font.Font('freesansbold.ttf', 50) #load font
img = pygame.image.load("C:/Users/793767/New folder/catt.jpg")
img2 = pygame.image.load("C:/Users/793767/Pictures/catttt.jpg")
img3 = pygame.image.load("C:/Users/793767/Pictures/surprised.jpg")
#----------------------------------------------------------------------------------------------------------------------------------------------
class heart:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        color1 = random.randrange(0,255)
        color2= random.randrange(0,255)
        color3= random.randrange(0,255)
        pygame.draw.circle(screen, (color1,color2,color3), (self.xpos, self.ypos), 20) #top left circle
        pygame.draw.circle(screen, (color1,color2,color3), (self.xpos+40, self.ypos), 20) #top right circle
        pygame.draw.polygon(screen, (color1,color2,color3), ((self.xpos-20, self.ypos+5),(self.xpos+59, self.ypos+5), (self.xpos+20, self.ypos+50))) #triangle to form base

    def move(self):
        if self.ypos >=1000:
            self.ypos = 0
        self.ypos +=1 


#---------------------------------------------------------------------------------------------------------------------------------------------- 
        
#instantiate more hearts
h1 = heart(200,200)
h2 = heart (400,400)
h3 = heart(100,100)

heartrain = [] #empty list
for i in range(100): 
        heartrain.append(heart(random.randrange(0,1000),random.randrange(0,1000)))#push alien objects into list

while(True):
    screen.fill((0,0,0))
    h1.draw()
    h2.draw()
    h3.draw()
    h1.move()
    h2.move()
    h3.move()
    
    for i in range (len(heartrain)):
        heartrain[i].draw()
        heartrain[i].move()

    text1 = font.render('HOW ARE YOU SO PERFECT??!!!!', True, (255, 255, 255)) #numbers give color
    screen.blit(text1, (100, 100))
    screen.blit(img,(350,400))
    screen.blit(img2,(600,700))
    screen.blit(img3,(100,700))
    pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)
