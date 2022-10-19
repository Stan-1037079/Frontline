#Frontline 
import pygame
import random 
import os 

WIDTH = 1000
HEIGHT = 800 
FPS = 60 

#Colors 
Grey = (192, 192, 192)
Red = (255, 0, 0)

#Pygame initialiser, Music, Screen ratio, Title game, 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frontline')
clock = pygame.time.Clock 

running = True
while running:



