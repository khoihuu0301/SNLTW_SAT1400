import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_icon(pygame.image.load("C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\game.png"))
pygame.display.set_caption("Hello World")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.update()
