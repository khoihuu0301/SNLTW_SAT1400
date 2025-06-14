import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 60
y = 60
color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
color_index = 0
done = False

class Car:
    def __init__(self, color, speed, x, y):
        self.color = color
        self.speed = speed
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, 90, 90))

Audi = Car(color_list[0], 999, x, y)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                color_index = (color_index + 1) % len(color_list)
            elif event.key == pygame.K_LEFT:
                color_index = (color_index - 1) % len(color_list)
    # Không di chuyển hình vuông nữa

    win.fill((255, 255, 255))  # Clear the screen with white
    Audi.x = x
    Audi.y = y
    Audi.color = color_list[color_index]
    Audi.draw()
    pygame.display.update()
