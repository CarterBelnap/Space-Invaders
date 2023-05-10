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
    def __init__(self,startX,startY,width,height,load_path):
        super().__init__()
        img_load = pygame.image.load(load_path) 
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.alive=True
        self.pop =False
        self.count=20
        self.movex = 1    
        self.startx = startX
        self.starty = startY

    def update(self,move):

        if move == True:    
            self.movex = -self.movex
            self.rect.x += self.movex
            self.rect.y += 10
        if move == False:
                self.rect.x += self.movex 
        return self.rect.x, self.rect.y
    
class Bullets(pygame.sprite.Sprite):
    def __init__(self,startX,startY,width,height,load_path):
        super().__init__()
        img_load = pygame.image.load(load_path) 
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        #downson was not here :)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        

    def update(self,speed,direction):
        self.rect.y+=speed*direction

class Barrier(pygame.sprite.Sprite):
    def __init__(self,startX,startY,width,height,load_path):
        super().__init__()
        img_load = pygame.image.load(load_path) 
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        lives = 10