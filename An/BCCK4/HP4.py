import pygame
from car import Car, Car2
# from car2 import Car2

pygame.init()
win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
# x = 60
# y = 60
clock.tick(60)
R = (255, 0, 0)  # Màu đỏ
G = (0, 255, 0)  # Màu xanh lá
B = (0, 0, 255)  # Màu xanh dương

color_list = [R, G, B]

done = False   

# i = 0

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#         if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
#             i = i + 1
#             if i >= len(color_list):
#                 i = 0  # Reset i về 0 nếu vượt quá số màu trong color_list
#             Porsche.change_color(color_list[i])  # Thay đổi màu của Porsche
            
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
#             i = i - 1
#             if i < 0:  # Nếu i nhỏ hơn 0, reset lại về chỉ số cuối của color_list
#                 i = len(color_list) - 1
#             Porsche.change_color(color_list[i])  # Thay đổi màu của Porsche


    # # Vẽ lại màn hình và Porsche với màu mới
    # win.fill((255, 255, 255))  # Xóa màn hình (màu nền trắng)
    # pygame.draw.rect(win, Porsche.color, pygame.Rect(x, y, 90, 90))  # Vẽ Porsche với màu mới


BMW = Car2(surface=win, color=G, speed=1, size = 50, x= 30, y= 50)
Porsche = Car(color=R, speed=1, size = 50, x= 0, y= 0)
Porsche.move(win, mapping='arrow')



pygame.quit()
