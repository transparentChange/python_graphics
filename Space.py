#---------------------------------------------------------------------------------------------------------------------------------------------------
#Matthew Sekirin & Etienne Brazeau
#Nov 9,2017
#Space.py
#creates an image of space using shapes, the main focus being a rocket
#---------------------------------------------------------------------------------------------------------------------------------------------------

#initialize the program
import pygame
import random
import math
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))
surface = pygame.Surface((500,500))

#initialize the colours
DARKBLUE=(30,58,104)
GRAY=(151,163,150)
BLACK=(0,0,0)
ORANGESATURN=(219,52,16)
VENUS = (209,114,25)
NEPTUNEBLUE=(3,17,153)
YELLOW = (254,218,14)
LIGHTBLUE = (51,130,134)
WHITE = (255,255,255)
PURPLE = (162,120,248)

#draw the wings of the spaceship
pygame.draw.ellipse(surface,LIGHTBLUE,(240,225,100,230)) 
pygame.draw.ellipse(surface,BLACK,(290,395,40,120)) 
pygame.draw.ellipse(surface,LIGHTBLUE,(180,225,100,230)) 
pygame.draw.ellipse(surface,BLACK,(195,402,40,120))

#draw the body of the space ship and cover the wings
pygame.draw.ellipse(surface,LIGHTBLUE,(225,130,70,280))
pygame.draw.ellipse(surface,LIGHTBLUE,(200,200,120,240))

pygame.draw.ellipse(surface,BLACK,(200,200,120,240),3)
pygame.draw.ellipse(surface,BLACK,(225,130,70,280),3)
pygame.draw.ellipse(surface,BLACK,(220,415,100,50))

pygame.draw.circle(surface,BLACK,(260,250),21)
pygame.draw.circle(surface,BLACK,(260,290),21)
pygame.draw.circle(surface,BLACK,(260,330),21)
pygame.draw.circle(surface,DARKBLUE,(260,250),17)
pygame.draw.circle(surface, DARKBLUE, (260,290),17)
pygame.draw.circle(surface, DARKBLUE, (260,330),17)

surface2 = pygame.transform.rotate(surface,30) #rotate surface
gameWindow.blit(surface2, (300, 70)) #blit surface with gameWindow


#draw circular asteroid belt using for loop
for h in range (10):
    radius = random.randint(700,750)
    for j in range(30):
        y = random.randint(0,600)
        x = math.sqrt(radius ** 2 - (y - 400) ** 2) - 200
        pygame.draw.polygon(gameWindow,GRAY,((x,y + 1),(x,y - 1),(x - 1,y),(x + 1, y)))

#draw randomly placed stars 
i = 0 #initialize accumulator variable
while (i != 45):
    while (i != 45):
        i += 1
        x = random.randint(0,800)
        y = random.randint(0,600)
        if x > 600 and y > 300:
            break
        halfLength = random.randint(0,2)
        heightLarge = int(math.sqrt(3) * halfLength)
        heightSmall = int(heightLarge / 3)
        pygame.draw.polygon(gameWindow,WHITE,((x,y),(x + halfLength, y + heightLarge),(x - halfLength, y + heightLarge)))
        pygame.draw.polygon(gameWindow,WHITE,((x - halfLength,y + heightSmall),(x + halfLength,y + heightSmall),(x, y + heightLarge + heightSmall)))

#draw the sun
for j in range(19,0,-1): #accounts for the sun's rays and glow
    YELLOW = (254 - 12 * j,74 - 3 * j,19 - j)
    pygame.draw.circle(gameWindow,YELLOW,(0,200),95 + 10 * j)
for i in range(25,0,-1): #accounts for the sun itself
    YELLOW = (254,130 - 4 * i,29 - i)
    pygame.draw.circle(gameWindow,YELLOW,(0,200),20 + 3 * i)
pygame.draw.arc(gameWindow, VENUS, (0,585,800,30),0,math.pi,15)

#planets
pygame.draw.circle(gameWindow,GRAY,(400,350),40,40) #mercury

pygame.draw.circle(gameWindow, NEPTUNEBLUE, (700,70),25) #neptune
pygame.draw.arc(gameWindow, PURPLE, (665,70,70,10),0,math.pi * 2, 3) #neptune's rings
pygame.draw.arc(gameWindow,PURPLE,(665,70,70,15),13 * math.pi / 12, 23 * math.pi / 12,3) #more rings
pygame.draw.rect(gameWindow,NEPTUNEBLUE,(675,68,50,7)) #cover

pygame.draw.ellipse(gameWindow,ORANGESATURN,(550,200,70,75)) #venus

  
#store and quit program
pygame.display.update()

time.sleep(15)
pygame.quit()
