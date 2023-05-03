#Carter Belnap
#May 3rd 2023
#Space Invaders Program
import pygame, sys
from player import Player


pygame.init()
font = pygame.font.SysFont('Consolas', 70)

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800


#Setup of Starting objects
player_group=pygame.sprite.Group()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Space Invaders")
player_ship = Player(325,700,30,35,'image.png')
player_group.add(player_ship)
def collision(object1, object2):
    return 

def display():
    window.fill(0x000000)
    player_group.draw(window)

    
 
while True:
    display()
    player_ship.move()

    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Player Borders @ 0 & (700-playersize_x)
    if player_ship.rect.x<0:
        player_ship.rect.x=0
    elif player_ship.rect.x>670:
        player_ship.rect.x=670

    #if pygame.sprite.spritecollide(player_ship, Wallgroup, False, collided=pygame.sprite.collide_mask):
    #    player_ship.collide()
        
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw