import pygame # Import the pygame library so we can use its functions

#Initialising pygame
pygame.init() # Start up pygame, required before using its features 

#setup display
Myscreen = pygame.display.set_mode((650,600)) # Create a window with width 650 and height 600
pygame.display.set_caption("Circle") # Set the window title text

# define colours (using RGB values: Red,Green,Blue
black=(0,0,0) # Black colour 
blue = (0,0,225) # Blue colour
red = (255,0,0) # Red colour
green = (0,255,0) # Green colour
yellow = (255,255,0) # Yellow colour
turquoise=(76,223,210)




# Fill screen with turquoise
Myscreen.fill(turquoise) # Paint the entire screen turqoise

#---CLASS DEFINITION---
# Circle class
class Circle:
    def __init__(self, color, position, radius): # Initialize each circle object
        self.color=color
        self.position=position
        self.radius=radius

    def draw(self):
        pygame.draw.circle(Myscreen,self.color,self.position,self.radius) # Draw circle using Pygame

# Create objects

circle1 = Circle(blue,(100,100),50) # Create first circle (blue,at x = 100,y = 100, Radius = 50 )
circle2 = Circle(red,(300,200),30)
circle3 = Circle(black,(500,100),40)
circle4 = Circle(green,(200,400),60)
circle5 = Circle(yellow,(450,350),80)



#  DRAW EVERYTHING
circle1.draw()
circle2.draw()
circle3.draw()
circle4.draw()
circle5.draw()      









# update display
pygame.display.update()    # Refresh the screen so the new color appears

# game loop to keep the window open
running = True             # A flag to control the loop (True = keep running)
while running:             # Loop runs until "running" is set to False
    for event in pygame.event.get():        # Check for events (mouse, keyboard, quit, etc.)
        if event.type == pygame.QUIT:       # If the close button (X) is clicked
            running = False                 # Stop the loop and close the window

pygame.quit()    # Shut down pygame completely when loop ends










