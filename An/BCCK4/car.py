import pygame
class Car:
    def __init__(self, color, speed, width, height, x, y,image_path=None):
        self.color = color
        self.speed = speed
        self.width = width
        self.height = height 
        self.x = x
        self.y = y

        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (height, height))
        else:
            self.image = None

    def draw( self, surface):
        # pygame.draw.rect(surface, (0, 200, 255), (self.x, self.y, self.size, self.size))
        # if self.image:
        #     surface.blit(self.image, (self.x, self.y))
        # else:
        #     pygame.draw.rect(surface, (0, 200, 255), (self.x + self.width // 2, self.y, self.width, self.height))
        surface.blit(self.image, (self.x, self.y - 15))    
        pygame.draw.rect(surface, (0, 200, 255), (self.x + self.width // 2, self.y, self.width - 5, self.height - 30), width=2)
    
    speed = 1




    def update(self, direction):
        if direction == "xuong":
            self.y += self.speed
        if direction == "len":
            self.y -= self.speed
        if direction == "trai":
            self.x -= self.speed
        if direction == "phai":
            self.x += self.speed
                



class Car2:
    def __init__(self, color, speed, width, height, x, y,image_path=None):
        self.color = color
        self.speed = speed
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # self.draw(surface)

        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (height, height))
        else:
            self.image = None

    def draw( self, surface):
        surface.blit(self.image, (self.x, self.y - 15))    
        pygame.draw.rect(surface, (0, 200, 255), (self.x + self.width // 2, self.y, self.width - 5, self.height - 30), width=2)
