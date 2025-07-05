# import pygame
# pygame.init()

# win=pygame.display.set_mode((400,300))
# pygame.display.set_caption("original rectangle switch")
# x=60
# y=60
# color= (0,128,255)
# done=False
# is_red=False
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done=True
#         pygame.draw.rect(win,color,pygame.Rect(x,y,90,90))
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             is_red = not is_red
#             if is_red:
#                 color=(255,0,0)
#             else:
#                 color=(0,128,255)
#         pygame.display.update()         
import pygame


pygame.init()

win = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Color Switch Car")


class Basket:
    def __init__(self):
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  
        self.color_index = 0
        self.x=0
        self.y=0

    def draw(self, surface):
        pygame.draw.rect(surface, self.colors[self.color_index], pygame.Rect(self.x, self.y, 50 , 50 ))

    def change_color(self, color):
        if color == 'next':
            self.color_index = (self.color_index + 1) % len(self.colors)
        elif color == 'prev':
            self.color_index = (self.color_index - 1) % len(self.colors)
    # def move(self,surface,mapping="arrow"):
    #     running = True
    #     if mapping == "arrow":
        
    #         while running:
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                     running = False
    #             # elif event.type == pygame.KEYDOWN:
    #             #     if event.key in [pygame.K_RIGHT, pygame.K_DOWN]:
    #             #         car.change_color('next')
    #             #     elif event.key in [pygame.K_LEFT, pygame.K_UP]:
    #             #         car.change_color('prev')
    #             keys = pygame.key.get_pressed()
    #             if keys [pygame.K_LEFT]:
    #                 self.x -= speed
    #             if keys [pygame.K_RIGHT]:
    #                 self.x += speed
    #             if keys [pygame.K_UP]:
    #                 self.y -= speed
    #             if keys [pygame.K_DOWN]:
    #                 self.y += speed 
    #             self.x= max(0, min(WIDTH - SQUARE_SIZE,self.x))
    #             self.Y=max(0, min(WIDTH - SQUARE_SIZE,self.y))    
    #             surface.fill((30,30,30))
    #             self.draw(surface)
    #             pygame.display.flip()
    #             clock.tick(60)
        def update(direction,self):
            if direction== "X vuong":
                self.y += speed
            if direction=="len":
                self.y -= speed
                self.x -= "trai"
                self.x += " phai"
            
basket=Basket()
x,y=0,0
SQUARE_SIZE=50
WIDTH=500
speed=5
running = True
clock = pygame.time.Clock()

        
win.fill((255, 255, 255))  
basket.move(win)

    #Yvuong=Ytron + radius 
    # Xvuong + Xtron < Xvuong + radius
class Ball:
     def __init__(self):
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  
        self.color_index = 0
        self.x=0
        self.y=0
        self.speed=5
        self.radius=25

     def draw(self, surface):
        pygame.draw.circle(surface, self.colors[self.color_index],(self.x,self.y),radius=25)     
     def move(self):
        self.y += self.speed
        self.x -= self.speed
     def is_caught_by(self, basket: Basket):
        return (
            basket.y <= self.y + self.radius <= basket.y + basket.height and
            basket.x <= self.x <= basket.x + basket.width
        )
     def points (self):
        basket_rect= pygame.Rect(self.x,self.y,basket.size,basket.size )
        dist_x = abs(ball.x - basket_rect.centerx)
        dist_y = abs(ball.y - basket_rect.centery)
        if dist_x <= (basket.size // 2+ ball.size) and dist_y <= (basket.size // 2+ ball.size):
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over!", True, (255,0,0))


running = True
clock = pygame.time.Clock()

basket = Basket()
ball = Ball()
pygame.display.update()
pygame.quit()
