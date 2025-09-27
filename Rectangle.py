import pygame
# Initializing pygame
pygame.init()

#setup display
Myscreen=pygame.display.set_mode((650,600))
pygame.display.set_caption("oval")

#define colours
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
turquoise=(76,223,210)



# Fill screen with turquoise
Myscreen.fill(turquoise)

#update display
pygame.display.update()

#gameloop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

pygame.quit()