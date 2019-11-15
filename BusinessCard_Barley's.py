#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Matthew Sekirin
#Oct 10, 2017
#BusinessCard_Barley's.py
#Provides a description and creates an informative but elegant business card of a wine bar company 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#import modules and initialize surfaces and the program itself
import pygame
import time
import math
pygame.init()

WIDTH = 805
HEIGHT = 460
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))
surface = pygame.Surface((250,250),pygame.SRCALPHA, 32)
surface = surface.convert_alpha() #adds transparency
    
#initialize colours
BLACK = (0,0,0)
RED = (153,0,18)
DARKRED = (115,5,2)
BROWN = (97,31,31)
BROWNCOUNTER = (60,20,20)
BROWNBORDER = (110,80,80)
WHITE = (253,237,208)
GREEN = (100,141,44)
DARKGREEN = (0,17,0)

#initialize fonts
fontHarTitle = pygame.font.SysFont("Harlow Solid Italic",50,0,1)
fontVlad = pygame.font.SysFont("Vladimir Script",20)
fontHar= pygame.font.SysFont("Harlow Solid Italic",14)
fontHarSub = pygame.font.SysFont("Harlow Solid Italic",16)
fontHarSub.set_underline(1)

#---------------------------------------------------------------------------------------------------------------------------------#
#The main program begins here
#---------------------------------------------------------------------------------------------------------------------------------#

#draw the background
pygame.draw.rect(gameWindow,BROWN,(0,0,805,460))
pygame.draw.rect(gameWindow,RED,(20,20,765,420))

#draw a counter and its shadow
pygame.draw.rect(gameWindow,BROWNBORDER,(20,340,765,100))
pygame.draw.rect(gameWindow, BROWNCOUNTER, (20,340,765,15))
for i in range(50):
    yCoordinate = 355 + i
    BROWNCOUNTER = (60 + i,30 + i,30 + i)
    pygame.draw.line(gameWindow,BROWNCOUNTER,(20 + i,yCoordinate),(785,yCoordinate))

#draw wine bottle's outline
pygame.draw.polygon(gameWindow,BLACK,((90,340),(95,240),(110,195),(110,140),(151,140),(155,200),(168,250),(170,340))) 
pygame.draw.ellipse(gameWindow,BLACK,(125,190,45,130))
pygame.draw.ellipse(gameWindow,BLACK,(93,190,45,130))

#draw the artistic details added to the wine bottle
pygame.draw.polygon(gameWindow,WHITE,((106,320),(106,225),(111,205),(116,205),(116,245),(162,245),(162,323)))
pygame.draw.arc(gameWindow,WHITE,(103,304,70,23),7 * math.pi / 6, 173 * math.pi / 96,4)
pygame.draw.arc(gameWindow,BLACK,(111,195,20,70),3 * math.pi / 4,7 * math.pi / 6,3) #cover
pygame.draw.rect(gameWindow,BLACK,(113,205,5,40)) #cover

pygame.draw.polygon(gameWindow,GREEN,((155,235),(148,235),(148,213),(143,210),(143,240),(125,236),(126,205),(131,211),(145,203)))
pygame.draw.ellipse(gameWindow,GREEN,(122,205,8,35))
pygame.draw.arc(gameWindow,GREEN,(116,196,41,97),math.pi / 12,math.pi / 3,3)
pygame.draw.polygon(gameWindow,GREEN,((127,227),(127,240),(137,240)))

pygame.draw.polygon(gameWindow,BLACK,((110,316),(110,297),(136,320)))
pygame.draw.ellipse(gameWindow,WHITE,(110,270,53,50))
pygame.draw.polygon(gameWindow,BLACK,((121,267),(146,266),(145,261),(125,262)))
pygame.draw.polygon(gameWindow,BLACK,((118,273),(153,273),(153,283),(120,283)))
pygame.draw.rect(gameWindow,BLACK,(129,288,17,4))
pygame.draw.polygon(gameWindow,BLACK,((136,294),(140,294),(138,297)))
pygame.draw.polygon(gameWindow,BLACK,((154,218),(154,235),(159,235)))
pygame.draw.polygon(gameWindow,WHITE,((136,332),(153,332),(154,328),(133,330)))

#draw the bottlneck and cap
pygame.draw.polygon(gameWindow,RED,((118,125),(143,125),(143,175),(118,175)))

pygame.draw.ellipse(gameWindow,BLACK,(109,125,13,50))
pygame.draw.ellipse(gameWindow,RED,(106,125,10,50)) #cover
pygame.draw.ellipse(gameWindow,RED,(95,128,20,70)) #cover
pygame.draw.ellipse(gameWindow,BLACK,(140,125,7,50))
pygame.draw.ellipse(surface,RED,(142,92,25,105)) #cover
surface2 = pygame.transform.rotate(surface,5) #rotate surface
gameWindow.blit(surface2, (-10,0)) #blit surface with gameWindow

pygame.draw.rect(gameWindow,BLACK,(123,123,7,20))
pygame.draw.ellipse(gameWindow,RED,(123,120,14,7)) #cover
pygame.draw.arc(gameWindow,RED,(115,136,15,14),0,math.pi/ 2,7) #cover

pygame.draw.rect(gameWindow,BLACK,(128,117,14,4))
pygame.draw.polygon(gameWindow,BLACK,((139,103),(137,107),(141,107),(141,114),(130,114),(118,114),(118,107),(122,107),(120,103),))

#draw the second wine glass from the left
pygame.draw.rect(gameWindow,BLACK,(267,275,11,65))
pygame.draw.ellipse(gameWindow,BLACK,(239,215,70,93))
pygame.draw.ellipse(gameWindow,WHITE,(260,233,45,62))
pygame.draw.ellipse(gameWindow,BLACK,(277,233,20,67)) #cover
pygame.draw.rect(gameWindow,BLACK,(255,240,30,60)) #cover
pygame.draw.polygon(gameWindow,RED,((230,240),(310,236),(280,200))) #cover
pygame.draw.rect(gameWindow,BLACK,(225,275,10,65)) 
pygame.draw.polygon(gameWindow,BLACK,((260,237),(260,243),(303,240),(303,234))) 

#draw the first wine glass from the left
pygame.draw.ellipse(gameWindow,BLACK,(193,211,65,90))
pygame.draw.ellipse(gameWindow,BLACK,(209,208,55,93))
pygame.draw.ellipse(gameWindow,WHITE,(203,218,55,77))
pygame.draw.ellipse(gameWindow,DARKRED,(202,225,40,70))
pygame.draw.rect(gameWindow,BLACK,(200,230,30,30)) #cover
pygame.draw.rect(gameWindow,BLACK,(221,229,23,66)) #cover
pygame.draw.polygon(gameWindow,RED,((190,230),(270,225),(240,190))) #cover
pygame.draw.polygon(gameWindow,BLACK,((200,230),(255,230),(255,225))) #cover
pygame.draw.ellipse(gameWindow,BLACK,(230,228,20,67)) #cover


#draw fonts
graphics = fontHarTitle.render("Barley's Wine Bar",1,BLACK)
gameWindow.blit(graphics,(250,50))
graphics = fontVlad.render("Where quality is a given",1,BLACK)
gameWindow.blit(graphics,(340,90))
graphics = fontHar.render("Celebtrate life through good company and our vast selection",1,BLACK)
gameWindow.blit(graphics,(340,135))
graphics = fontHar.render("of fine wine and champagne from across the world.",1,BLACK)
gameWindow.blit(graphics,(340,147))
graphics = fontHarSub.render("Business Hours:",1,DARKGREEN)
gameWindow.blit(graphics,(400,220))
graphics = fontHar.render("Mon. to Sat. 10AM - 9PM",1,DARKGREEN)
gameWindow.blit(graphics,(410,240))
graphics = fontHar.render("Sun. 11AM - 5PM",1,DARKGREEN)
gameWindow.blit(graphics,(410,252))
graphics = fontHarSub.render("Tel:",1,DARKGREEN)
gameWindow.blit(graphics,(400,272))
graphics = fontHar.render("(905)-123-4567",1,DARKGREEN)
gameWindow.blit(graphics,(425,273))
graphics = fontHarSub.render("Adress:",1,DARKGREEN)
gameWindow.blit(graphics,(400,292))
graphics = fontHar.render("101 Centre St, RichmondVille, ON \t L4B 3Q9",1,DARKGREEN)
gameWindow.blit(graphics,(450,293))

#update and quit the program 
pygame.display.update()

time.sleep(50)
pygame.quit()
