import pygame
from pygame.sprite import Sprite
#from pygame.locals import *
#Addtional moduels in pygame

pygame.init()

clock= pygame.time.Clock() #locks the frames per second
fps=40

#create game screen

screen_width=640
screen_height=450
#due to sprites

screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bill... USNA Edition')

#define game variables
ground_scroll=0 #infinite ground
scroll_speed=4 #4px speed
flying= False
game_over= False

#load images
bg = pygame.image.load('images/NA_BG2.bmp') #must load images first then blit(Draw)
ground_img= pygame.image.load('images/waves.PNG')

# class Bill(Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         #pygame.sprite.Sprite.__init__(self)
#         self.image=pygame.image.load('images/goat.png')
#         self.index=0
#         self.counter=0
#         self.image=self.image[self.index]
#         self.rect= self.image.get_rect()
#         self.rect.center= [x,y]
#         self.vel=0 # Acounting for the velocity and gravity
#         self.clicked= False

    # def update(self):
    #
    #     if flying== True:
    #     #Gravity
    #         self.vel += 0.5 #so bird is accelerating
    #     if self.vel>8:
    #         self.vel=8
    #     if self.rect.bottom < 330:
    #         self.rect.y +=int(self.vel) # this is a float so it must be wrapped in int function
    #
    #     #jump
    #     if pygame.mouse.get_pressed()[0]==1 and self.clicked== False:
    #         self.clicked= True
    #         self.vel= -10
    #     if pygame.mouse.get_pressed()[0] == 0:
    #         self.clicked = False
    #
    #     #roatate the goat
    #         self.image= pygame.transform.roatate(self.images[self.index], self.vel * -2)
    #     else:
    #         self.image = pygame.transform.roatate(self.images[self.index], -90)

#keeps track of all of sprites similar to a python list
# goat_group= Bill(20, 20)
#     #pygame.sprite.Group()
# print(goat_group)

#flappy= Bill(100,(int(screen_height/2))

#goat_group.add(flappy)



#Create game loop
run= True #initial condition that we set to true

while run: #While run is true carry out all below
    #event handlers in pygame acklowdge user input

    clock.tick(fps)

    screen.blit(bg,(0,0)) #function to show it on the screen

    # goat_group.draw(screen)
    # goat_group.update()

    #draw the ground
    screen.blit(ground_img, (ground_scroll, 330))

    #Check if goat has hit the ground
    # if flappy.rect.bottom> 330:
    #     game_over=True
    #     flying=False


    if game_over== False:
        #draw and scroll the screen
        ground_scroll-= scroll_speed
        if abs(ground_scroll) >300: #gives impression of scrolling backgorund from end of image
            ground_scroll= 0
    #
    for event in pygame.event.get(): # This will get all the events that are happening
            if event.type==pygame.QUIT: #looks for a paticular event
                run= False #no longer meets required condition in the while loop
            if event.type== pygame.MOUSEBUTTONDOWN and flying == False and game_over== False:
                flying= True
    pygame.display.update() #updates for various changes in the while loop


pygame.quit()