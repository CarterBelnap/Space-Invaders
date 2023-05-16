#Carter Belnap
#May 3rd 2023
#Space Invaders Program


#Imports
import pygame, sys, random, time
from player import Player, Alien, Barrier, Bullets


#Start Program
pygame.init()
pygame.mixer.init()


# Window/FPS/Extra Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
move_alian = False
win_check = False
alien_shot_time = 15
player_shot_time = 25
barrier_count = 3
score = 0
alien_lives = 27  
font = pygame.font.SysFont('Consolas', 70)
score_font = pygame.font.SysFont('Consolas', 40)
win_sound = pygame.mixer.Sound("win.mp3")
shoot_sound = pygame.mixer.Sound("zap.mp3")


#Setup of Starting objects
player_group=pygame.sprite.Group()
alien_group=pygame.sprite.Group()
barrier_group=pygame.sprite.Group()
bulletp_group=pygame.sprite.Group()
bulleta_group=pygame.sprite.Group()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Space Invaders")



def player_reset():
  global player_ship
  #Starting Locations- Player & Barriers
  player_ship = Player(325,700,40,45,'image.png')
  barrier1 = Barrier(100,650,80,50,'shields.png')
  barrier2 = Barrier(300,650,80,50,'shields.png')
  barrier3 = Barrier(500,650,80,50,'shields.png')
  player_group.add(player_ship)
  barrier_group.add(barrier1,barrier2,barrier3)
def alien_reset():
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
  alien_group.add(alien1,alien2,alien3,alien4,alien5,alien6,alien7,alien8,alien9,alien10,alien11,alien12,alien13,alien14,alien15,alien16,alien17,alien18,alien19,alien20,alien21,alien22,alien23,alien24,alien25,alien26,alien27)

def display():
    global wall_alien
    wall_alien=pygame.draw.rect(window,(0xFFFFFF),(100,600,1000,10))
    window.fill(0x000000)
    player_group.draw(window)
    alien_group.draw(window)
    barrier_group.draw(window)
    bulletp_group.draw(window)
    bulleta_group.draw(window)
    window.blit(score_font.render(f"SCORE:{score}", True, (255, 255, 255)), (30,750))


def collision(object1, object2):
    return object1.colliderect(object2)


def alian_move():
  global move_alian
  for group in alien_group:
    if group.rect.x>650 or group.rect.x<10:  
      move_alian = True
      break
    else:
      move_alian = False
    display()


def alien_lose():
  global wall_alien
  for group in alien_group:
     if collision(group.rect,wall_alien):
        lose()


def lose():
  global score, barrier_count
  window.fill(0x000000)
  window.blit(font.render("YOU LOSE", True, (255, 255, 255)), (200, 400))
  window.blit(score_font.render(f"SCORE:{score}", True, (255, 255, 255)), (225,500))
  window.blit(font.render("PRESS SPACE", True, (255, 255, 255)), (140, 600))
  window.blit(font.render("TO QUIT", True, (255, 255, 255)), (190, 670))
  pygame.display.update()
  pygame.time.delay(100)
  key_input = pygame.key.get_pressed()
  if key_input[pygame.K_ESCAPE]:
    score = 0
    barrier_count = 3
    player_group.empty()
    alien_group.empty()
    barrier_group.empty()
    alien_reset()
    player_reset()
    display()




def win():      
  global win_check, score, barrier_count       
  player_group.empty()
  alien_group.empty()
  barrier_group.empty() 
  bulleta_group.empty()
  bulletp_group.empty()     

  window.blit(font.render("YOU WIN", True, (255, 255, 255)), (200, 400))
  window.blit(score_font.render(f"SCORE:{score}", True, (255, 255, 255)), (225,500))
  window.blit(font.render("PRESS ESC", True, (255, 255, 255)), (140, 600))
  window.blit(font.render("TO QUIT", True, (255, 255, 255)), (180, 670))
  key_input = pygame.key.get_pressed()
  if key_input[pygame.K_ESCAPE]:
    score = 0
    barrier_count = 3
    win_check = False
  pygame.display.update()
  pygame.time.delay(100)   
def alien_bullets():
   global alien_shot_time, alien_group
   alien_shot_time -=1
   shot = random.choice(alien_group.sprites())
   if alien_shot_time<0:
    try:
        pygame.mixer.find_channel().play(shoot_sound)
    except:
        pass
    bulleta_group.add(Bullets(shot.rect.x ,shot.rect.y,10,20,"bullet.png"))
    alien_shot_time = 15


def player_bullets():
   global player_shot_time, player_ship
   player_shot_time -=1
   key_input = pygame.key.get_pressed()
   if player_shot_time<0 and key_input[pygame.K_SPACE]:
      try:
        pygame.mixer.find_channel().play(shoot_sound)
      except:
        pass
      bulletp_group.add(Bullets(player_ship.rect.x + 15,player_ship.rect.y - 13,10,20,"bullet.png"))
      player_shot_time = 25


def bullet_hits():
  global barrier_count, score, alien_lives
  for pgroup in bulletp_group:
    if pygame.sprite.spritecollide(pgroup, alien_group, True, collided=pygame.sprite.collide_mask):
      pgroup.kill()
      score += 100
      alien_lives -= 1
  for bgroup in barrier_group:
    if pygame.sprite.spritecollide(bgroup, bulleta_group, True, collided=pygame.sprite.collide_mask) or pygame.sprite.spritecollide(bgroup, bulletp_group, True, collided=pygame.sprite.collide_mask):
      bgroup.lives-=1
      barrier_group.update()
      if bgroup.lives ==0:
        bgroup.kill()
  for agroup in bulleta_group:
     if pygame.sprite.spritecollide(agroup, player_group, False, collided=pygame.sprite.collide_mask):
      score -=20
      agroup.kill()





while True:
  player_reset()
  alien_reset()
  while win_check == False:    
      display()
      alien_lose()
      alian_move()
      player_bullets()
      alien_bullets()
      bullet_hits()
      
      player_ship.move()
      alien_group.update(move_alian)
      bulletp_group.update(3,-1)
      bulleta_group.update(3,1)
    
      if alien_lives == 0:
        try:
          pygame.mixer.find_channel().play(win_sound)
        except:
          pass
        win_check = True

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


  while win_check == True:
      win()
      for event in pygame.event.get():
        # if user  QUIT then the screen will close
          if event.type == pygame.QUIT:
              sys.exit()
            
      pygame.display.update() #update the display
      fpsClock.tick(fps) #speed of redraw