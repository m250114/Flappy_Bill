import pygame

pygame.init()


#locks the frames per second
clock= pygame.time.Clock()
fps=40

#create game screen dimensions
screen_width=450
screen_height=375

#creates blank game window with a caption
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bill... USNA Edition')

#define game variables
ground_scroll=0 #infinite ground
scroll_speed=4 #4px speed
flying= False
game_over= False

#load images
#must load images first then blit(Draw)
bg = pygame.image.load('images/BG (2).png')
ground_img= pygame.image.load('images/cloud.jpg')

#Create game loop
#While run is true carry out all below
run= True
while run:
    #event handlers in pygame acklowdge user input

    clock.tick(fps)

    screen.blit(bg,(0,0)) #function to show it on the screen


    #draw the ground
    screen.blit(ground_img,(ground_scroll, 330))

    if game_over== False:
        #draw and scroll the screen
        ground_scroll-= scroll_speed
        if abs(ground_scroll) >300: #gives impression of scrolling backgorund from end of image
            ground_scroll= 0

     # This will get all the events that are happening
    for event in pygame.event.get():
            # looks for a paticular event
            if event.type==pygame.QUIT:
                # no longer meets required condition in the while loop
                run= False
            if event.type== pygame.MOUSEBUTTONDOWN and flying == False and game_over== False:
                flying= True

    # updates for various changes in the while loop
    pygame.display.update()


pygame.quit()