import pygame
from pygame import gfxdraw
from sys import exit
from Player import *
from Enemy import *
from Button import Button
from Map import Map
from random import choice, randint

# set up pygame and screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((17, 16, 18))
pygame.display.set_caption("Last Stand")

# sets up a clock
clock = pygame.time.Clock()

# set up player
play = Player()
player = pygame.sprite.GroupSingle()
player.add(play)
kills = 0
gold = 0

# set up player arrows
arrows = pygame.sprite.Group()
arrowTimer = 0

# set up enemies
enemies = pygame.sprite.Group()
blood = pygame.sprite.Group()

# enemy event timer
enemyTimer = pygame.USEREVENT + 1
enemyTime = 2200
pygame.time.set_timer(enemyTimer, enemyTime)

moreEnemiesTimer = pygame.USEREVENT + 2
pygame.time.set_timer(moreEnemiesTimer, 20000)

# set up map
map = Map()

# set up game loop 
isPlaying = False

# set up menu/buttons
titleText = Button((400, 150), "The Last Stand", 60, (138, 34, 26), False)
playButton = Button((400,350), "Play", 50, (138, 34, 26))
retreatButton = Button((60, 600), "Retreat!", 30, (138, 34, 26))
healthText = Button((75, 60), f"Health: {play.health}", 30, (0, 0, 0), False)
killsText = Button((700, 60), f"Kills: {kills}", 30, (138, 34, 26), False)
controlsText = Button((400, 500), "CONTROLS: Hold and release mouse to fire arrows. Use WASD to move.", 20, (138, 34, 26), False)

# set up music
bgMusic = pygame.mixer.Sound("audio/Music/bosstheme.mp3")
bgMusic.set_volume(.15)
bgMusic.play(loops=-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == enemyTimer:
            enemies.add(choice([Imp(play), Thief(play), Orc(play), Death(play), Minotaur(play)]))
        if event.type == pygame.MOUSEBUTTONUP:
            if arrowTimer >= 3 and player.sprites():
                arrows.add(Arrow((player.sprites()[0].rect.centerx, player.sprites()[0].rect.centery - 15), 8, pygame.mouse.get_pos()))
            arrowTimer = 0
        if event.type == moreEnemiesTimer:
            enemyTime -= 200
            pygame.time.set_timer(enemyTimer, enemyTime)

    if isPlaying:
        ########################## Terrain/Ground Stuff #############################
        screen.blit(map, (0,0))
        
        ######################### Arrow Stuff ###############################
        keys = pygame.mouse.get_pressed()
        if keys[0]:
            arrowTimer += .15

        arrows.draw(screen)
        arrows.update()

        ################################ Enemy Stuff ######################################
        for e in enemies: # enemy shadows
            if e.health <= 0:
                if isinstance(e, Imp): 
                    gfxdraw.filled_circle(screen, e.rect.centerx + 32, e.rect.centery + 64, 12, (105,105,105,180))
                elif isinstance(e, Minotaur):
                    gfxdraw.filled_circle(screen, e.rect.centerx + 45, e.rect.centery + 70, 18, (105,105,105,180))
                else:
                    gfxdraw.filled_circle(screen, e.rect.centerx + 32, e.rect.centery + 64, 15, (105,105,105,180))
            else:
                if isinstance(e, Imp): 
                    gfxdraw.filled_circle(screen, e.rect.centerx, e.rect.centery + 32, 12, (105,105,105,180))
                elif isinstance(e, Minotaur):
                    gfxdraw.filled_circle(screen, e.rect.centerx + 5, e.rect.centery + 28, 18, (105,105,105,180))
                else:
                    gfxdraw.filled_circle(screen, e.rect.centerx, e.rect.centery + 32, 15, (105,105,105,180))

        enemies.draw(screen)
        enemies.update()

        for arrow in arrows:
            for i in range(len(enemies)):
                if arrow.rect.colliderect(enemies.sprites()[i].rect):
                    blood.add(Blood(enemies.sprites()[i].rect.centerx, enemies.sprites()[i].rect.centery))
                    enemies.sprites()[i].update(True)
                    if enemies.sprites()[i].health <= 0:
                        kills += 1
                        gold += 1
                    arrow.kill()
        
        blood.update()
        blood.draw(screen)
        
        ##################### Player Stuff #################################
        if not player.sprites():
            enemies.empty()
            kills = 0
            gold = 0
            titleText.setText("You Died Valiantly...")
            playButton.setText("Try Again")
            play.health = 100
            isPlaying = False

        for p in player:
            gfxdraw.filled_circle(screen, p.rect.centerx, p.rect.centery + 32, 15, (105,105,105,180))   # player shadows

        player.draw(screen)
        player.update()

        ########################## Button Stuff #################################
        screen.blit(killsText.surface, killsText.rect)
        killsText.setText(f"Kills: {kills}")
        killsText.update()
        healthText.setText(f"Health: {play.health}")
        healthText.update()
        screen.blit(healthText.surface, healthText.rect)
        retreatButton.update()
        screen.blit(retreatButton.surface, retreatButton.rect)
        if retreatButton.getButtonPressed():
            enemies.empty()
            arrows.empty()
            blood.empty()
            titleText.setText("You must return to the fight!")
            playButton.setText("Return")
            isPlaying = False
    else:
        ##################### Menu Stuff #######################
        screen.fill((17, 16, 18))
        screen.blit(titleText.surface, titleText.rect)
        screen.blit(controlsText.surface, controlsText.rect)
        screen.blit(playButton.surface, playButton.rect)
        playButton.update()
        if playButton.getButtonPressed():
            player.add(play)
            isPlaying = True
    
    ##################### pygame clock stuff ###########################
    pygame.display.update()
    clock.tick(60)


