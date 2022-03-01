import pygame
from random import randint

class Map(pygame.surface.Surface):
    def __init__(self):
        # sets up the ground
        super().__init__((800, 600))
        grass = pygame.transform.scale2x(pygame.image.load("assets/Land/Tiles/tile000.png").convert_alpha())
        grass1 = pygame.transform.scale2x(pygame.image.load("assets/Land/Tiles/tile001.png").convert_alpha())
        grass2 = pygame.transform.scale2x(pygame.image.load("assets/Land/Tiles/tile002.png").convert_alpha())
        flower = pygame.transform.scale2x(pygame.image.load("assets/Land/Tiles/tile013.png").convert_alpha())
        flower2 = pygame.transform.scale2x(pygame.image.load("assets/Land/Tiles/tile026.png").convert_alpha())
        for i in range(30):
            for j in range(20):
                num = randint(1, 100)
                if num <= 70:
                    self.blit(grass, (i * 32, j * 32))
                elif num < 80:
                    self.blit(grass1, (i * 32, j * 32))
                elif num < 90:
                    self.blit(grass2, (i * 32, j * 32))
                elif num < 95:
                    self.blit(flower, (i * 32, j * 32))
                elif num <= 100:
                    self.blit(flower2, (i * 32, j * 32))
        
        #sets up the wall
        wall = pygame.transform.scale2x(pygame.image.load("assets/Walls/wall.jpg").convert_alpha())
        wall = pygame.transform.rotate(wall, 90)
        for i in range(20):    
            self.blit(wall, (150, i * 30))