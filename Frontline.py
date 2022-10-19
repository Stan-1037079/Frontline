#Frontline 
import pygame
import random 
import os 

WIDTH = 1000
HEIGHT = 800 
FPS = 60 

#Colors 
GREY = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0 , 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#Pygame initialiser, Music, Screen ratio, Title game, 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frontline')
clock = pygame.time.Clock 

# Display title icon 
#icon = pygame.image.load('jet.png')
#pygame.display.set_icon(icon)

#Game Loop, Running speed
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(GREY)
    
    pygame.display.flip()

pygame.quit()
