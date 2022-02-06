import pygame
from pygame import gfxdraw
import math

# The player class will make the playable character sprite for this game; it takes in input to perform actions, animates itself, and kills itself.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # images
        self.image = pygame.transform.scale2x(pygame.image.load("assets/archer/tile000.png").convert_alpha())
        self.stand = self.image
        self.fire = [pygame.transform.scale2x(pygame.image.load("assets/archer/tile033.png").convert_alpha()), 
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile034.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile035.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile036.png").convert_alpha())]
        self.fireIndex = 0
        self.walk = [pygame.transform.scale2x(pygame.image.load("assets/archer/tile020.png").convert_alpha()), 
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile021.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile022.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile023.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile024.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile025.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile026.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile027.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile028.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile029.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile030.png").convert_alpha())]
        self.walkIndex = 0
        self.isWalking = False
        self.die = [pygame.transform.scale2x(pygame.image.load("assets/archer/tile040.png").convert_alpha()), 
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile041.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile042.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile043.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile044.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile045.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile046.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile047.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile048.png").convert_alpha()),
                    pygame.transform.scale2x(pygame.image.load("assets/archer/tile049.png").convert_alpha())]
        self.dieIndex = 0
        # the player rectangle 
        self.rect = self.image.get_rect(midbottom = (80,330))
        #set player health
        self.health = 100
        self.isFiring = False  
        self.dieSound = pygame.mixer.Sound("audio/SoundEffect/human/die1.wav")
        self.dieSound.set_volume(.3)

    def playerInput(self):
        if pygame.mouse.get_pressed()[0]:
            self.isWalking = False
            self.isFiring = True
        else:
            self.isFiring = False
            self.fireIndex = 0
            if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s] and not pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]:
                self.isWalking = False
            else:
                self.isWalking = True
                if pygame.key.get_pressed()[pygame.K_w] and self.rect.top > 0:
                    self.rect.centery -= 2
                if pygame.key.get_pressed()[pygame.K_s] and self.rect.bottom < 600:
                    self.rect.centery += 2
                if pygame.key.get_pressed()[pygame.K_d] and self.rect.right < 150:
                    self.rect.right += 2
                if pygame.key.get_pressed()[pygame.K_a] and self.rect.left > 0:
                    self.rect.left -= 2
            
    def walkAnimation(self):
        self.walkIndex += .2
        if self.walkIndex >= len(self.walk):
            self.walkIndex = 0
        self.image = self.walk[int(self.walkIndex)]

    def fireAnimation(self):
        self.fireIndex += .15
        if self.fireIndex >= len(self.fire):
            self.fireIndex = len(self.fire) - 1 
        self.image = self.fire[int(self.fireIndex)]

    def playDieSound(self):
        if self.dieIndex == 0:
            self.dieSound.play()

    def dieAnimation(self):
        self.playDieSound()
        self.dieIndex += .2
        if self.dieIndex >= len(self.die):
            self.kill()
            self.dieIndex = len(self.die) - 1
        self.image = self.die[int(self.dieIndex)]

    def animationState(self):
        if not self.isFiring and not self.isWalking:
            self.image = self.stand
        elif self.isWalking:
            self.walkAnimation()
        elif self.isFiring: 
            self.fireAnimation()

    def update(self, damage=0):
        self.health -= damage
        if self.health <= 0:
            self.dieAnimation()
        else:
            self.playerInput()
            self.animationState()

# The arrow class makes an arrow sprite that can be drawn to any surface in pygame. it will take in a start position and a target position along with a velocity and "shoot" the arrow accordingly
class Arrow(pygame.sprite.Sprite):
    def __init__(self, startPos, velocity, targetPos):
        super().__init__()
        self.pos = startPos
        self.direction = (targetPos[0] - self.pos[0], targetPos[1] - self.pos[1])
        length = math.hypot(*self.direction)
        if length == 0:
            self.direction = (0, -1)
        else:
            self.direction = (self.direction[0] / length, self.direction[1] / length)
        self.velocity = velocity
        self.rect = pygame.rect.Rect(startPos[0],startPos[1],10,1)
        self.angle = math.degrees(math.atan2(-self.direction[1], self.direction[0]))
        self.image = pygame.transform.rotate(pygame.image.load("assets/Arrow/tile000.png").convert_alpha(), self.angle + 90)
        self.images = [self.image, 
                    pygame.transform.rotate(pygame.image.load("assets/Arrow/tile001.png").convert_alpha(), self.angle + 90),
                    pygame.transform.rotate(pygame.image.load("assets/Arrow/tile002.png").convert_alpha(), self.angle + 90),
                    pygame.transform.rotate(pygame.image.load("assets/Arrow/tile003.png").convert_alpha(), self.angle + 90)]
        self.imageIndex = 0
        self.soundEffect = pygame.mixer.Sound("audio/SoundEffect/shoot.ogg")
        self.soundEffect.set_volume(.25)
        self.soundEffectPlay = True
    
    def arrowAnimation(self):
        self.imageIndex += .1
        if self.imageIndex >= len(self.images):
            self.imageIndex = 0
        self.image = self.images[int(self.imageIndex)]

    def playSoundEffect(self):
        if self.soundEffectPlay:
            self.soundEffect.play()
            self.soundEffectPlay = False

    def update(self):
        self.pos = (self.pos[0] + self.direction[0] * self.velocity, self.pos[1] + self.direction[1] * self.velocity)
        self.rect.center = self.pos
        if self.rect.x > 800 or self.rect.x < 0 or self.rect.y > 600 or self.rect.y < 0:
            self.kill()
        self.arrowAnimation()
        self.playSoundEffect()
        