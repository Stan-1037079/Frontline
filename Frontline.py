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

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        bullet_sound.play()

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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('img','bullet.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 10
    
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > WIDTH: 
            self.kill

#Pygame initialize, Music, Screen ratio, Title game, 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frontline')
clock = pygame.time.Clock()

#Background music and sounds 
pygame.mixer.music.load(os.path.join('sound','Front line.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

bullet_sound = pygame.mixer.Sound(os.path.join('sound','bullet.mp3'))
explosion_sound = pygame.mixer.Sound(os.path.join('sound','explosion.wav'))

# Score variable 
score = 0

#Draw text on screen + font used 
font_name = pygame.font.match_font('Times')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#Sprite groups 
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player() 
bullets = pygame.sprite.Group()
all_sprites.add(player)

# Spawn Enemies 
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
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                player.shoot()
    
    # Process input (Events)
    # Update 
    all_sprites.update()

    #Collision Enemy, Bullets
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits: 
        score += 100
        e = Enemy()
        all_sprites.add(e)
        enemies.add(e)
        explosion_sound.play()
        
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits: 
        running = False

    # Draw / Render
    #screen.fill(GREY)
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    pygame.display.update()
    #pygame.display.flip()

pygame.quit()
