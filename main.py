#Carter Belnap
#May 3rd 2023
#Space Invaders Program

#Imports
import pygame, sys, random
from player import Player, Alien, Barrier, Bullets

#Start Program
pygame.init()

# Window/FPS/Extra Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
move_alian = False
font = pygame.font.SysFont('Consolas', 70)

#Setup of Starting objects
player_group=pygame.sprite.Group()
alien_group=pygame.sprite.Group()
barrier_group=pygame.sprite.Group()
bulletp_group=pygame.sprite.Group()
bulleta_group=pygame.sprite.Group()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Space Invaders")


#Starting Locations- Player & Barriers
player_ship = Player(325,700,40,45,'image.png')
barrier1 = Barrier(100,650,80,50,'shields.png')
barrier2 = Barrier(300,650,80,50,'shields.png')
barrier3 = Barrier(500,650,80,50,'shields.png')

#Starting Locations- Aliens
alien1 = Alien(20,50,40,35,"alien.png")
alien2 = Alien(70,50,40,35,"alien.png")
alien3 = Alien(120,50,40,35,"alien.png")
alien4 = Alien(170,50,40,35,"alien.png")
alien5 = Alien(220,50,40,35,"alien.png")
alien6 = Alien(270,50,40,35,"alien.png")
alien7 = Alien(320,50,40,35,"alien.png")
alien8 = Alien(370,50,40,35,"alien.png")
alien9 = Alien(420,50,40,35,"alien.png")
alien10 = Alien(20,100,40,35,"alien.png")
alien11 = Alien(70,100,40,35,"alien.png")
alien12 = Alien(120,100,40,35,"alien.png")
alien13 = Alien(170,100,40,35,"alien.png")
alien14 = Alien(220,100,40,35,"alien.png")
alien15 = Alien(270,100,40,35,"alien.png")
alien16 = Alien(320,100,40,35,"alien.png")
alien17 = Alien(370,100,40,35,"alien.png")
alien18 = Alien(420,100,40,35,"alien.png")
alien19 = Alien(20,150,40,35,"alien.png")
alien20 = Alien(70,150,40,35,"alien.png")
alien21 = Alien(120,150,40,35,"alien.png")
alien22 = Alien(170,150,40,35,"alien.png")
alien23 = Alien(220,150,40,35,"alien.png")
alien24 = Alien(270,150,40,35,"alien.png")
alien25 = Alien(320,150,40,35,"alien.png")
alien26 = Alien(370,150,40,35,"alien.png")
alien27 = Alien(420,150,40,35,"alien.png")
wall_alien=pygame.draw.rect(window,(255,255,255),(100,600,1000,10))
player_group.add(player_ship)
barrier_group.add(barrier1,barrier2,barrier3)
alien_group.add(alien1,alien2,alien3,alien4,alien5,alien6,alien7,alien8,alien9,alien10,alien11,alien12,alien13,alien14,alien15,alien16,alien17,alien18,alien19,alien20,alien21,alien22,alien23,alien24,alien25,alien26,alien27)

def collision(object1, object2):
    return object1.colliderect(object2)

def alian_move():
  global move_alian
  if alien9.rect.x>650 or alien1.rect.x<10:  
    move_alian = True
  else:
    move_alian = False
  display() 

def alien_lose():
  global move_alian
  for group in alien_group:
     if collision(group.rect,wall_alien):
         window.blit(font.render("YOU LOSE", True, (255, 255, 255)), (200, 400))
         move_alian = False
         pygame.display.update()
         pygame.time.delay(100)

def alien_bullets():
   shot = random.choice(alien_group.sprites())
   bulleta_group.add(Bullets(shot.rect.x ,shot.rect.y,10,20,"bullet.png"))

def player_bullets():
   key_input = pygame.key.get_pressed() 
   if key_input[pygame.K_SPACE]:
      bulletp_group.add(Bullets(player_ship.rect.x + 15,player_ship.rect.y - 13,10,20,"bullet.png"))

def display():
    window.fill(0x000000)
    player_group.draw(window)
    alien_group.draw(window)
    barrier_group.draw(window)
    bulletp_group.draw(window)
    bulleta_group.draw(window)


      

while True:    
    alien_lose()
    alian_move()
    display()
    player_bullets()
    alien_bullets()
    player_ship.move()
    alien_group.update(move_alian)
    bulletp_group.update(3,-1)
    bulleta_group.update(3,1)
    
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Player Borders @ 0 & (700-playersize_x)
    if player_ship.rect.x<0:
        player_ship.rect.x=0
    elif player_ship.rect.x>660:
        player_ship.rect.x=660

        
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw