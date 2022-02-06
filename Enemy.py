import pygame
from random import randint
from Player import Player

# This enemy class will be a super class to all of the enemies in the game. It will draw, animate, and can update the enemy as the player class does but has different attributes
# The classes that inherit from this class will only set up the animations and some stats depending on the type of enemy. This class will do most of the work
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player: Player):
        super().__init__()
        self.health = 1
        self.speed = 1
        self.image = pygame.Surface((64,64))
        self.stand = self.image
        self.walk = []
        self.walkIndex = 0
        self.rect = pygame.Rect(randint(810,1100),randint(100,500),64,64)
        self.die = []
        self.dieIndex = 0
        self.attack = []
        self.attackIndex = 0
        self.player = player
        self.damage = 1
        self.dieSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-1.wav")
        self.dieSoundEffect.set_volume(.25)
        self.attackSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-10.wav")
        self.attackSoundEffect.set_volume(.25)
        self.dRectBool = True
        self.hitSound = pygame.mixer.Sound("audio/SoundEffect/hit/hit.flac")
        self.hitSound.set_volume(.10)
    
    def walkAnimation(self):
        self.image = self.walk[int(self.walkIndex)]
        self.walkIndex += .2
        if self.walkIndex >= len(self.walk):
            self.walkIndex = 0

    def playDieSound(self):
        if self.dieIndex == 0:
            self.dieSoundEffect.play()

    def setDeathRect(self):
        if self.dRectBool:
            self.dRectBool = False
            self.rect.update(self.rect.left, self.rect.top, 0, 0)    

    def deathAnimation(self):
        self.playDieSound()
        self.setDeathRect()
        self.image = self.die[int(self.dieIndex)]
        self.dieIndex += .2
        if self.dieIndex >= len(self.die):
            self.kill()

    def playAttackSound(self):
        if self.attackIndex < 6 and self.attackIndex > 5.9:
            self.attackSoundEffect.play()

    def attackAnimation(self):
        self.playAttackSound()
        self.image = self.attack[int(self.attackIndex)]
        self.attackIndex += .1
        if self.attackIndex >= len(self.attack):
            self.attackIndex = 0

    def takeDamage(self):
        self.hitSound.play()
        self.health -= 1
    
    def move(self):
        self.rect.left -= self.speed

    def dealDamage(self):
        if self.attackIndex > len(self.attack) - 7 and self.attackIndex < len(self.attack) - 6.9:
            self.player.health -= self.damage

    def update(self, takeDamage=False):
        if takeDamage:
            self.takeDamage()
        if self.health <= 0:
            self.deathAnimation()
        elif self.rect.left <= 175:
            self.attackAnimation()
            self.dealDamage()
        else:
            self.walkAnimation()
            self.move()
         
class Imp(Enemy):
    def __init__(self, player: Player):
        super().__init__(player)
        self.speed = 2
        self.image = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile000.png").convert_alpha()), True, False)
        self.stand = self.image
        self.walk = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile020.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile021.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile022.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile023.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile024.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile025.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile026.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile027.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile028.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile029.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile030.png").convert_alpha()), True, False)]
        self.die = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile040.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile041.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile042.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile043.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile044.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile045.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile046.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile047.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile048.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile049.png").convert_alpha()), True, False)]
        self.attack = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile030.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile031.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile032.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile033.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile034.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile035.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile036.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile037.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile038.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile039.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Imp/tile040.png").convert_alpha()), True, False)]
        self.dieSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-5.wav")
        self.dieSoundEffect.set_volume(.25)
        self.attackSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-17.wav")
        self.attackSoundEffect.set_volume(.25)

class Thief(Enemy):
    def __init__(self, player: Player):
        super().__init__(player)
        self.image = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile000.png").convert_alpha()), True, False)
        self.stand = self.image
        self.walk = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile020.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile021.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile022.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile023.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile024.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile025.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile026.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile027.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile028.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile029.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile030.png").convert_alpha()), True, False)]
        self.die = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile040.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile041.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile042.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile043.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile044.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile045.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile046.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile047.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile048.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile049.png").convert_alpha()), True, False)]
        self.attack = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile030.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile031.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile032.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile033.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile034.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile035.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile036.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile037.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile038.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile039.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Thief/tile040.png").convert_alpha()), True, False)]
        self.dieSoundEffect = pygame.mixer.Sound("audio/SoundEffect/human/die1.wav")
        self.dieSoundEffect.set_volume(.25)
        self.attackSoundEffect = pygame.mixer.Sound("audio/SoundEffect/human/sword - StarNinjas/sword.6.ogg")
        self.attackSoundEffect.set_volume(.20)

class Orc(Enemy):
    def __init__(self, player: Player):
        super().__init__(player)
        self.health = 2
        self.damage = 2
        self.image = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile000.png").convert_alpha()), True, False)
        self.stand = self.image
        self.walk = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile020.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile021.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile022.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile023.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile024.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile025.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile026.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile027.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile028.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile029.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile030.png").convert_alpha()), True, False)]
        self.die = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile040.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile041.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile042.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile043.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile044.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile045.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile046.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile047.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile048.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile049.png").convert_alpha()), True, False)]
        self.attack = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile030.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile031.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile032.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile033.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile034.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile035.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile036.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile037.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile038.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile039.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Orc/tile040.png").convert_alpha()), True, False)]
        self.dieSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-6.wav")
        self.dieSoundEffect.set_volume(.25)
        self.attackSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-9.wav")
        self.attackSoundEffect.set_volume(.25)

class Minotaur(Enemy):
    def __init__(self, player: Player):
        super().__init__(player)
        self.health = 3
        self.damage = 3
        self.speed = .5
        self.image = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile000.png").convert_alpha()), True, False)
        self.rect = self.image.get_rect(midbottom = (randint(810,1000),randint(100,500)))
        self.stand = self.image
        self.walk = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile020.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile021.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile022.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile023.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile024.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile025.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile026.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile027.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile028.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile029.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile030.png").convert_alpha()), True, False)]
        self.die = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile040.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile041.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile042.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile043.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile044.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile045.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile046.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile047.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile048.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile049.png").convert_alpha()), True, False)]
        self.attack = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile030.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile031.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile032.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile033.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile034.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile035.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile036.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile037.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile038.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile039.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Minotaur/tile040.png").convert_alpha()), True, False)]

class Death(Enemy):
    def __init__(self, player: Player):
        super().__init__(player)
        self.health = 2
        self.speed = 2
        self.image = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile000.png").convert_alpha()), True, False)
        self.stand = self.image
        self.walk = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile020.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile021.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile022.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile023.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile024.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile025.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile026.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile027.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile028.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile029.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile030.png").convert_alpha()), True, False)]
        self.die = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile040.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile041.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile042.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile043.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile044.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile045.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile046.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile047.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile048.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile049.png").convert_alpha()), True, False)]
        self.attack = [pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile030.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile031.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile032.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile033.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile034.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile035.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile036.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile037.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile038.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile039.png").convert_alpha()), True, False),
                pygame.transform.flip(pygame.transform.scale2x(pygame.image.load("assets/Death/tile040.png").convert_alpha()), True, False)]
        self.dieSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-11.wav")
        self.dieSoundEffect.set_volume(.25)
        self.attackSoundEffect = pygame.mixer.Sound("audio/SoundEffect/monster/monster-6.wav")
        self.attackSoundEffect.set_volume(.25)



class Blood(pygame.sprite.Sprite):
        def __init__(self, xCoord, yCoord):
                super().__init__()
                self.blood = [pygame.transform.scale(pygame.image.load("assets/Blood/tile000.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile001.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile002.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile003.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile004.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile005.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile006.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile007.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile008.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile009.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile010.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile011.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile012.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile013.png").convert_alpha(), (35, 35)),
                pygame.transform.scale(pygame.image.load("assets/Blood/tile014.png").convert_alpha(), (35, 35))]
                self.bloodIndex = 0
                self.rect = self.blood[0].get_rect()
                self.rect.centerx = xCoord
                self.rect.centery = yCoord
                self.image = self.blood[0]
        
        def playAnimation(self):
                self.bloodIndex += .2
                if self.bloodIndex >= len(self.blood):
                        self.kill()
                        self.bloodIndex = 0
                self.image = self.blood[int(self.bloodIndex)]
                
        def update(self):
                self.playAnimation()