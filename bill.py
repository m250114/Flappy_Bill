import pygame
from pygame.locals import *
#Addtional moduels in pygame

pygame.init()

clock= pygame.time.Clock() #locks the frames per second
fps=60

#create game screen

screen_width=400
screen_height=400
#due to sprites

screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bill... USNA Edition')

#define game variables
ground_scroll=0 #infinite ground
scroll_speed=4 #4px speed

#load images
bg = pygame.images.load('images/NA_BG2.bmp') #must load images first then blit(Draw)
gorund_images= pygame.image.load('../Images/cloud_feature_graphic.jpg')





#Create game loop
run= True #initial condition that we set to true

while run: #While run is true carry out all below
    #event handlers in pygame acklowdge user input

    clock.tick(fps)

    screen.blit(bg,(0,0)) #function to show it on the screen

    #draw and scroll the screen
    screen.blit(cloud_feature_graphic.jpg, (ground_scroll,400))
    ground_scroll-= scroll_speed
    if abs(ground_scroll) >35: #gives impression of scrolling backgorund from end of image
        ground_scroll= 0

    for event in pygame.event.get(): # This will get all the events that are happening
        if event.type==pygame.QUIT: #looks for a paticular event
            run= False #no longer meets required condition in the while loop

    pygame.diplay.update() #updates for various changes in the while loop


pygame.quit()