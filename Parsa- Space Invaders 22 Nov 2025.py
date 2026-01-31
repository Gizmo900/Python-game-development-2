

#This project is a simple Space-Invaders-style demo created using Pygame, 
# featuring a controllable spaceship placed at the centre of the screen, 
# two asteroids positioned at the top, and three stars scattered across the display 
# as potential collectible items. The spaceship image is loaded, scaled, and moved 
# using the arrow keys, with each key press shifting its position by 30 pixels in 
# the corresponding direction. The asteroids and stars are loaded and drawn at fixed locations, 
# and the screen refreshes continuously to update all objects in real time.

import random
import pygame
pygame.init()                      # Initialise all Pygame modules

screenwidth = 800
screenheight = 500
screen = pygame.display.set_mode((screenwidth, screenheight))  # Create game window

pygame.display.set_caption("space invaders")   # Set window title

# Load and scale spaceship image
spaceshipimage = pygame.image.load(r"C:\Users\Bahadori-jahromia\OneDrive - University of West London\Desktop\Jetlearn coding\Game development 2\spaceship.png").convert_alpha()
scalespaceship = pygame.transform.scale(spaceshipimage, (70, 70))

# Load and scale asteroid image
astroidimage = pygame.image.load(r"C:\Users\Bahadori-jahromia\OneDrive - University of West London\Desktop\Jetlearn coding\Game development 2\Astroid.png").convert_alpha()
scaleastroid = pygame.transform.scale(astroidimage, (100, 100))

# Load star image
starimage = pygame.image.load(r"c:\Users\Bahadori-jahromia\OneDrive - University of West London\Desktop\Jetlearn coding\Game development 2\star.png").convert_alpha()

score = 0   # Score variable (not used yet)
# Create font for displaying text
font = pygame.font.SysFont(None, 40)   # None = default font, 40 = size




# Create rectangles for positioning images
image_rect = scalespaceship.get_rect()
image_rect.center = (screenwidth//2, screenheight//2)   # Start spaceship in centre

# Asteroid positions
image_rect2 = scaleastroid.get_rect()
image_rect2.center = (100, 25)

image_rect3 = scaleastroid.get_rect()
image_rect3.center = (700, 25)

# Star positions
image_rect4 = starimage.get_rect()
image_rect4.center = (250, 249)

image_rect5 = starimage.get_rect()
image_rect5.center = (465, 450)

image_rect6 = starimage.get_rect()
image_rect6.center = (676, 200)

running = True
star1 = True
star2 = True
star3 = True
while running:
    for event in pygame.event.get():      # Check all events (keyboard, mouse, close)
        if event.type == pygame.QUIT:     # If user clicks X
            running = False               # Exit game loop

        elif event.type == pygame.KEYDOWN:    # If a key is pressed
            if event.key == pygame.K_LEFT:
                image_rect.x -= 30        # Move spaceship left
            elif event.key == pygame.K_RIGHT:
                image_rect.x += 30        # Move spaceship right
            elif event.key == pygame.K_UP:
                image_rect.y -= 30        # Move spaceship up
            elif event.key == pygame.K_DOWN:
                image_rect.y += 30        # Move spaceship down

    #A sprite is like a character in the game
    # collided_enemies = pygame.sprite.spritecollide(image_rect, image_rect4, True) # True removes collided enemies
    #for enemy in collided_enemies:
       # print("Spaceship touched star!")
    
    
    screen.fill((0, 0, 0))                # Paint background black

    # Draw images onto window
    screen.blit(scalespaceship, image_rect) # Draw the spaceship image (scalespaceship) 
                                             #at the position stored in image_rect.
    screen.blit(scaleastroid, image_rect2)
    screen.blit(scaleastroid, image_rect3)
    if star1:
        screen.blit(starimage, image_rect4)
    if star2:
        screen.blit(starimage, image_rect5)
    if star3:
        screen.blit(starimage, image_rect6)

    # Render and draw score text on screen
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White text
    screen.blit(score_text, (150, 10))   # Draw at top-left of the screen
    if image_rect.colliderect(image_rect4):
        star1 = False
        score = score +1
        print("collision")
        image_rect4.center = (800,500)

    if image_rect.colliderect(image_rect5):
        star2 = False
        score = score +1
        print("collision") 
        image_rect5.center = (800,500)
        
    if image_rect.colliderect(image_rect6):
        star3 = False
        score = score +1
        print("collision")
        image_rect6.center = (800,500)
    
    if image_rect.colliderect(image_rect2):
        print("collision")
        lose_text = font.render("You lost!", True, (255, 0, 0))  # Red text
        screen.blit(lose_text, (300, 250)) 
        image_rect.center = (1000,1000)
    
    if image_rect.colliderect(image_rect3):
        print("collision")
        lose_text = font.render("You lost!", True, (255, 0, 0))  # Red text
        screen.blit(lose_text, (300, 250)) 
        image_rect.center = (1000,1000)

    if score==3:
        win_text = font.render("You won!", True, (0, 255, 0))  # Green text
        screen.blit(win_text, (300, 250)) 
    pygame.display.update()               # Refresh the window

pygame.quit()                             # Quit Pygame cleanly



