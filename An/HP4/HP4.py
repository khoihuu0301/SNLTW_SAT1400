import pygame
from car import Car

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 60
y = 60

R = (255, 0, 0)  # Màu đỏ
G = (0, 255, 0)  # Màu xanh lá
B = (0, 0, 255)  # Màu xanh dương

color_list = [R, G, B]

# Khởi tạo đối tượng Porsche (Car) với màu ban đầu là màu đỏ
Porsche = Car(R, 225)

done = False
i = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            i = i + 1
            if i >= len(color_list):
                i = 0  # Reset i về 0 nếu vượt quá số màu trong color_list
            Porsche.change_color(color_list[i])  # Thay đổi màu của Porsche
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            i = i - 1
            if i < 0:  # Nếu i nhỏ hơn 0, reset lại về chỉ số cuối của color_list
                i = len(color_list) - 1
            Porsche.change_color(color_list[i])  # Thay đổi màu của Porsche


    # Vẽ lại màn hình và Porsche với màu mới
    win.fill((255, 255, 255))  # Xóa màn hình (màu nền trắng)
    pygame.draw.rect(win, Porsche.color, pygame.Rect(x, y, 90, 90))  # Vẽ Porsche với màu mới

    pygame.display.update()

pygame.quit()
