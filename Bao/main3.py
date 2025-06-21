import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

WIDTH = 500
HEIGHT = 500
SQUARE_SIZE = 50
x = 60
y = 60
color = (0, 128, 255)
done = False
is_red = False
speed = 5
size = 90
clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
# pygame.draw.rect(win , color, pygame.Rect(x, y, 90, 90))
     

class car:
    def __init__(self, x, y):
        self.speed = speed
        self.size = size
        self.color = (0, 128, 255)
        self.x = 0
        self.y = 0
        
    
    def draw(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, 90, 90))           

    def move(self, surface , mapping = "arrow"):
        running = True
        if mapping == "arrow":
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

                self.x = max(0, min(WIDTH - self.size, self.x))
                self.y = max(0, min(HEIGHT - self.size, self.y))
                
                surface.fill((30, 30, 30))
                self.draw()
                pygame.display.flip()
                clock.tick(60)
                
car2 = car(speed, SQUARE_SIZE)
car2.move(win, mapping="arrow")
pygame.display.update()