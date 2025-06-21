import pygame
class Car:
    def __init__(self, color, speed, size, x, y):
        self.color = color
        self.speed = speed
        self.size = size
        self.x = 0
        self.y = 0
    def draw( self, surface):
        pygame.draw.rect(surface, (0, 200, 255), (self.x, self.y, self.size, self.size))
    
    speed = 1 
    x,y =0,0


    def move(self, surface, mapping='arrow'):
        running = True
        if mapping ==  'arrow':
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.x -= self.speed
                if keys[pygame.K_RIGHT]:
                    self.x += self.speed
                if keys[pygame.K_UP]:
                    self.y -= self.speed
                if keys[pygame.K_DOWN]:
                    self.y += self.speed

                self.x = max(0, min(500 - 50, self.x))
                self.y = max(0, min(500 - 50, self.y))

                surface.fill((30, 30, 30))
                self.draw(surface)
                pygame.display.flip()
                

                pygame.display.update()


    # def change_color(self, new_color):
    #     self.color = new_color
