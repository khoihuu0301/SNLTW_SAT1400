import pygame
import math

pygame.init()
font = pygame.font.SysFont(None, 30)
WIDTH, HEIGHT = 500, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")


class Basket:
    def __init__(self):
         self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  
         self.color_index = 0
         self.width = 80
         self.height = 15
         self.x = WIDTH // 2 - self.width // 2
         self.y = HEIGHT - self.height - 10
         self.speed = 7
         self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self, surface):
        pygame.draw.rect(surface, "BLUE", (self.x, self.y, self.width, self.height))

    def change_color(self, color):
        if color == 'next':
            self.color_index = (self.color_index + 1) % len(self.colors)
        elif color == 'prev':
            self.color_index = (self.color_index - 1) % len(self.colors)
    def move(self, dx):
         self.x +=dx * self.speed
    def collide(self, circle_x,circle_y,circle_radius):
        dx= max(self.rect.left - circle_x, 0 , circle_x - self.rect.right)
        dy=max(self.rect.top - circle_y, 0 , circle_y - self.rect.bottom)
        distance= math.sqrt(dx**2 + dy**2)
        if distance <= circle_radius:
            return True 
        else:
            return False
        
    # def update(direction,self):
    #     if direction== "X vuong":
    #         self.y += self.speed
    #     if direction=="len":
    #         self.y -= self.speed
    #         self.x -= "trai"
    #         self.x += " phai"
            
# basket=Basket()
# x,y=0,0
# SQUARE_SIZE=50
# WIDTH=500
# speed=5
# running = True
# clock = pygame.time.Clock()

        
# win.fill((255, 255, 255))  
# basket.move(win)

    #Yvuong=Ytron + radius 
    # Xvuong + Xtron < Xvuong + radius
class Ball:
     def __init__(self,x,y,speed):
        self.radius = 10
        self.x = x
        self.y=y
        self.speed=speed     
     def draw(self, surface):
        pygame.draw.circle(surface, "RED", (self.x, self.y), self.radius)
     def move(self):
       self.y += self.speed
    #  def is_caught_by(self, basket: Basket):
    #     return (
    #         basket.y <= self.y + self.radius <= basket.y + basket.height and
    #         basket.x <= self.x <= basket.x + basket.width
    #     )

    #  def points (self):
    #     basket_rect= pygame.Rect(self.x,self.y,basket.size,basket.size )
    #     dist_x = abs(ball.x - basket_rect.centerx)
    #     dist_y = abs(ball.y - basket_rect.centery)
    #     if dist_x <= (basket.size // 2+ ball.size) and dist_y <= (basket.size // 2+ ball.size):
    #         font = pygame.font.SysFont(None, 48)
    #         text = font.render("Game Over!", True, (255,0,0))
basket = Basket()
ball = Ball()
score = 0
running = True
clock = pygame.time.Clock()

def draw_game():
    win.fill("WHITE")
    basket.draw(win)
    ball.draw(win)
    score_text = font.render(f"Điểm: {score}", True, "BLACK")
    win.blit(score_text, (10, 10))
    pygame.display.update()
    


while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            basket.move(keys)
            ball.move()
            
            
    if ball.is_caught_by(basket):
        score += 1
        ball.reset()

    if ball.y > HEIGHT:
        ball.reset()

    draw_game()
pygame.quit()
