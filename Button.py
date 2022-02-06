import pygame

# This button class will provide a clickable button on pygame; it can also be used to quickly set up text on any pygame surface
# the isButton parameter can be set to false so that the text does not change alpha value when hovered over; this is so this class can also be used as a quick way to draw text to a surface
class Button(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int], text="", textSize=30, color=(56,15,138), isButton=True):
        super().__init__()
        self.pos = position
        self.text = text
        self.textSize = textSize
        self.color = color
        self.isButton = isButton
        self.surface = pygame.font.Font("assets/Font/Quintessential-Regular.ttf", textSize).render(text, True, color).convert_alpha()
        self.defaultSurf = self.surface
        self.rect= self.surface.get_rect(midbottom = position)
        self.buttonPressed = False
    
    def setText(self, text: str):
        self.text = text
        self.surface = pygame.font.Font("assets/Font/Quintessential-Regular.ttf", self.textSize).render(text, True, self.color).convert_alpha()   
        self.rect = self.surface.get_rect(midbottom = self.pos)

    def setColor(self, color: tuple[int]):
        self.color = color
        self.surface = pygame.font.Font("assets/Font/Quintessential-Regular.ttf", self.textSize).render(self.text, True, color).convert_alpha()

    def getButtonPressed(self) -> bool:
        if self.buttonPressed:
            self.buttonPressed = False
            return True
        return self.buttonPressed

    def update(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        mouseClick = pygame.mouse.get_pressed()
        if mouseX <= self.rect.right and mouseX >= self.rect.left and mouseY <= self.rect.bottom and mouseY >= self.rect.top and self.isButton:
            self.surface.set_alpha(180)
        else:
            self.surface.set_alpha(255)
        if mouseX <= self.rect.right and mouseX >= self.rect.left and mouseY <= self.rect.bottom and mouseY >= self.rect.top and mouseClick[0]:
            self.buttonPressed = True