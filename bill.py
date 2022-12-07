import pygame
import random


pygame.init()


#locks the frames per second
#rather than running as quickly as it can your fixing it to a speed
clock= pygame.time.Clock()
#Frame rate per second using time function in pygame
fps=25

#create game screen dimensions

screen_width=400
screen_height=375


#creates blank game window with a caption
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bill... USNA Edition')



#def game font
font=pygame.font.SysFont('Bauhaus 93',40)
#def Color
yellow=(0,0,0)




#define game variables


# infinite ground
#I need to adjust x cordinate where image is drawn.
# when it starts off the x cordinate is 0. If I want it to the right it needs to inc. If i want it to the left it must decrease.
ground_scroll=0
# 4px speed

#How quickly the ground will scroll to the left
scroll_speed=4

#initial start game varibles
flying= False
game_over= False

#Sword varibles
sword_gap=130
sword_freq= 1850 #miliseconds 1.5 seconds
last_sword=pygame.time.get_ticks() - sword_freq #takes measure of time when game is started

#score counter
score=0
pass_sword=False


#load images
#must load images first then blit(Draw)
bg = pygame.image.load('images/BG (2).png')
ground_img= pygame.image.load('images/cloud.jpg')
button_image=pygame.image.load_extended('images/restart.png')

#Pygame Sprite clases already have blit
#Must include a x and y cordinate for where the goat will be drawn
#pygame sprite classes already have update and draw built into them, which makes the code neater


def draw_text(text,font,text_col,x,y):
    img= font.render(text,True, text_col)
    screen.blit(img,(x,y))


def reset_game():
    sword_group.empty()
    flappy.rect.x=100
    flappy.rect.y=int(screen_height/2)
    score=0
    return score


class Goat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.images=[]
        #tells me what image to show at certain time in list
        self.index = 0
        #controls speed at which pictures run
        self.counter = 0
        #populating images using for loop to create iterations
        for num in range(1,4):
            img=pygame.image.load(f'images/goat{num}.png').convert_alpha()
            self.images.append(img)
        #create images in class
        #this is the image that the sprite will be assigned
        self.image= self.images[self.index]
        #now i need a rectangle from the loaded image
        #get rect will create a rectangle for me from the boundaries of the image
        self.rect = self.image.get_rect()
        #now I need to position the rect/image
        #which I will do from the center of the goat rectangle
        #this will be my x and y cordinate
        self.rect.center=[x,y]
        #This is the upward movment against gravity
        self.vel=0
        self.clicked= False

    def movment(self):

        #handle the animation
        #use counter in goat class to increase the image every iteration
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            #cant go above the images I have in folder so I have to put a buffer to have it reset
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]



    #Gravity
        if flying== True:
            #increase velocity with every iteration
            self.vel += 0.5
            #cap to limit the increasing velocity thats desending
            if self.vel> 8:
                self.vel=8
            # print(self.vel)
            #I only want the bird to be affected by gravity by the hight of my ground
            if self.rect.bottom < 330:
            #add to y cordniate of the goat
            #self.vel will come out as a float so im wrapping it in an integer function
                self.rect.y += int(self.vel)
    #Jump
        if game_over==False:
        #Jumping happens everytime I click the pad
            if pygame.mouse.get_pressed()[0]==1 and self.clicked== False:
                self.clicked= True
                self.vel = -6
        # I need to add a trigger to let pygame know when the mouse has been released
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #Roate the goat

            #First feed in source image
            #transform is a function in pygame
            #whatever point im at in the animation I will rotate the image accordingly by indexing the path relative to the velocity
            #by default the angle is counterclockwise
            self.image= pygame.transform.rotate(self.images[self.index],self.vel *-1.5)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-180)

class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/sword.png')
        self.rect = self.image.get_rect()

        # define position of pipes based on x and y cord
        #position 1 is from the top,-1 is from the bottom

        #flipping pipes
        if position==1:
            #False true is talking about where the other sword is being flipped
            self.image= pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y - int(sword_gap/2)]
        if position==-1:
            self.rect.topleft = [x, y +  int(sword_gap/2)]

    #moving pipes with movment function
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

class Button():

    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

    def draw(self):

        action=False

        #get mouse position
        pos= pygame.mouse.get_pos()

        #check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action= True


        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


    #start the game



#Group will keep track of all the sprites that I add to it.
#similar to a list, but one of the differences is using the add function instead of append that I would use in a list function

#goat group
goat_group = pygame.sprite.Group()
sword_group= pygame.sprite.Group()

#Flappy is my first item or instence in the group that was added to the goat group
flappy = Goat(60, int(screen_height / 3))
goat_group.add(flappy)

#create restart button instance
button= Button(screen_width// 2-50,screen_height//2-100, button_image)


#Create game loop
#While run is true carry out all below
run= True
while run:
    #Fixing ground to the frames per second

    clock.tick(fps)

    # function to show it on the screen
    screen.blit(bg,(0,0))

    #Draw bird function
    #Notice that we do not need to blit and use a draw meathod. This is because the draw meathod is built into the sprite class.

    goat_group.draw(screen)
    sword_group.draw(screen)


    # #calls function
    # flappy.movment()
    # goat_group.update()



    #draw the ground
    screen.blit(ground_img, (ground_scroll, 330))

    #check Score
    #cant do this when there arnt any pipes on the screen
    #this is done by checking the length


    if len(sword_group)> 0:
        if goat_group.sprites()[0].rect.left < sword_group.sprites()[0].rect.left\
            and goat_group.sprites()[0].rect.right > sword_group.sprites()[0].rect.right\
            and pass_sword == False:
            pass_sword=True
        if pass_sword==True:
            if goat_group.sprites()[0].rect.left> sword_group.sprites()[0].rect.right:
                score+= 1
                pass_sword= False

    draw_text(str(score),font,yellow, int(screen_width/2),20)

    # calls function
    flappy.movment()
    goat_group.update()


            #look for collision
    #if I set the falses to true the goat and swords would be deleted
    if pygame.sprite.groupcollide(goat_group,sword_group,False,False) or flappy.rect.top <= 0:
        game_over=True

    #check to see if bird has hit the ground
    # take instance flappy and rectangle and look for the bottom
    if flappy.rect.bottom >= 330:
        game_over= True
        flying= False



    if game_over== False and flying== True:

        #generate new pipes
        time_now=pygame.time.get_ticks()
        if time_now- last_sword> sword_freq:
            # Create instance of sword
            sword_height = random.randint(-100,75)
            btm_sword = Sword(screen_width, int(screen_height / 2)+ sword_height, -1)
            top_sword = Sword(screen_width, int(screen_height / 2)+sword_height, 1)
            sword_group.add(btm_sword)
            sword_group.add(top_sword)
            last_sword= time_now

        #draw and scroll the screen
        #It will start at the initial condition 0, then quickly scroll to the left by 4 px a sec
        ground_scroll-= scroll_speed
        if abs(ground_scroll) >40: #gives impression of scrolling backgorund from end of image
            ground_scroll= 0

        sword_group.update()


        #check for game over and reset

    if game_over== True:
        if button.draw()== True:
            game_over= False
            score= reset_game()

     # This will get all the events that are happening
    # event handlers in pygame acklowdge user input and will look for a specfic one
    for event in pygame.event.get():
            # looks for a paticular event
            if event.type==pygame.QUIT:
                # no longer meets required condition in the while loop
                run= False
            #both conditions will be false at the start of the game when clicked the game will start
            if event.type== pygame.MOUSEBUTTONDOWN and flying == False and game_over== False:
                flying= True



    # updates for various changes in the while loop
    #update instead of flip because there will be mutiple changes to the game loop
    #Update meathod is already pre programmed into pygame
    pygame.display.update()


pygame.quit()