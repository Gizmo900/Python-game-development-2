import pygame   # Import the pygame library so we can use its functions

# Initializing pygame
pygame.init()   # Start up pygame, required before using its features

# setup display
Myscreen = pygame.display.set_mode((650,600))  # Create a window with width=650 and height=600
pygame.display.set_caption("oval")             # Set the window title to "oval"

# define colours (using RGB values: Red, Green, Blue)
black = (0,0,0)        # Black color
blue = (0,0,255)       # Blue color
red = (255,0,0)        # Red color
turquoise = (76,223,210) # Turquoise color

# Fill screen with turquoise
Myscreen.fill(turquoise)   # Paint the entire screen turquoise
class Rect:
    def __init__(self,color,dimensions):
        self.rect_surf=Myscreen #Self is like a reference for the current object you are creating
        self.color=color
        self.dimensions=dimensions

    def draw(self):
         self.cuboid=pygame.draw.rect(self.rect_surf,self.color,self.dimensions) #dimension (x,y,width,height)
         
#rect objects
rect1=Rect(blue,(290,300,200,50))
rect2=Rect(red,(10,10,60,40))
rect3=Rect(black,(10,500,400,50))

# draw rectangle
rect1.draw()
rect2.draw()
rect3.draw()
       









# update display
pygame.display.update()    # Refresh the screen so the new color appears

# game loop to keep the window open
running = True             # A flag to control the loop (True = keep running)
while running:             # Loop runs until "running" is set to False
    for event in pygame.event.get():        # Check for events (mouse, keyboard, quit, etc.)
        if event.type == pygame.QUIT:       # If the close button (X) is clicked
            running = False                 # Stop the loop and close the window

pygame.quit()    # Shut down pygame completely when loop ends

