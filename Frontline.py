#Frontline 
import pygame
import random
import os 

#img_dir = path.join(path.dirname(__file__),'img')

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

#Player 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('img','jet.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


#Pygame initialiser, Music, Screen ratio, Title game, 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frontline')
clock = pygame.time.Clock 

all_sprites = pygame.sprite.Group()

# Display title icon, Background
icon = pygame.image.load(os.path.join('img','jet.png')).convert()
pygame.display.set_icon(icon)
background = pygame.image.load(os.path.join('img','Background.jpg')).convert()

#Game Loop, Running speed
running = True
while running:
    screen.blit(background,(WIDTH,HEIGHT))
    clock.tick(FPS)
    # Process input (Events)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    # Process input (Events)
    # Update 
    all_sprites.update()
    # Draw / Render
    screen.fill()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
