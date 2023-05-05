import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self,startX,startY,width,height,load_path):
        super().__init__()
        img_load = pygame.image.load(load_path) 
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        
    def move(self):
        t_f_list = {True : 1, False: 0}
        key_input = pygame.key.get_pressed() 
        self.movex = (t_f_list[key_input[pygame.K_a]] * -5) + (t_f_list[key_input[pygame.K_d]] * 5)
        self.rect.x += self.movex
   
    def collide(self):
        self.rect.x -= self.movex

class Alien(pygame.sprite.Sprite):
    alien = pygame.image.load('alien.png') #with .png or .jpb included in the name
    alien = pygame.transform.scale(alien, (35, 30))  #resize image Where 35 ,35 is the size, (x,y)