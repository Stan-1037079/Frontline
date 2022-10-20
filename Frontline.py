#Frontline 
import pygame
import random
import os 

WIDTH = 1000
HEIGHT = 700 
FPS = 60 

#Colors 
GREY = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0 , 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#Player, Sprite, Start position, background fade, Speed x,y
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('img','jet.png')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0 
    # Movements 
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
        self.rect.y += self.speedy
        if self.rect.right > WIDTH: 
            self.rect.right = WIDTH
        if self.rect.left < 0: 
            self.rect.left = 0
        if self.rect.bottom > HEIGHT: 
            self.rect.bottom = HEIGHT
        if self.rect.top < 0: 
            self.rect.top = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('img','helicopter.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        self.rect.x = random.randrange(950, 1025)
        self.speedy = random.randrange(-3,5)
        self.speedx = random.randrange(-8,0)

    def update(self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy 
        if self.rect.top > HEIGHT + 10 or self.rect.left < -15 or self.rect.right > WIDTH + 20: 
            self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
            self.rect.x = random.randrange(950, 1025)
            self.speedy = random.randrange(-3,5)
            self.speedx = random.randrange(-8,0)   

#Pygame initialize, Music, Screen ratio, Title game, 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frontline')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(12):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

# Display title icon, Background,Scale
icon = pygame.image.load(os.path.join('img','jet.png')).convert()
pygame.display.set_icon(icon)
background = pygame.image.load(os.path.join('img','Background.jpg')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#Game Loop, Running speed
running = True
while running:
    clock.tick(FPS)
    # Process input (Events)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    # Process input (Events)
    # Update 
    all_sprites.update()
    # Draw / Render
    #screen.fill(GREY)
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    pygame.display.update()
    #pygame.display.flip()

pygame.quit()
