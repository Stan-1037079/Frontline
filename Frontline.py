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

#Player 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('img','jet.png')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (200, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0 

    def update(self):
        self.speedx = 0 
        self.speedy = 0 
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5 
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5 
        if keystate[pygame.K_UP]:
            self.speedy = -5 
        if keystate[pygame.K_DOWN]:
            self.speedy = 5 
        self.rect.x += self.speedx
        if self.rect.right > WIDTH: 
            self.rect.right = WIDTH
        if self.rect.left < 0: 
            self.rect.left = 0


#Pygame initialize, Music, Screen ratio, Title game, 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frontline')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
    screen.fill(GREY)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
