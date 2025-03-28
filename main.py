

import pygame
from pygame import *
from ai_logic import move




def rasst(x1,y1,x2,y2):
    try:
        return ((x2-x1)**2+(y2-y1)**2)**0.5
    except ValueError:
        return False


bg_x=bg_y=0
W = 600
H = 600
pygame.init()
screen = pygame.display.set_mode((W, H))
FPS = 45
x = W // 2
y = H // 2
r = 25
speed=10
x_enemy=100
y_enemy=100
rect1=Rect((x_enemy, y_enemy, 50, 50))
clock = pygame.time.Clock()
running = True
BLACK = (0, 0, 0)
background_image = pygame.image.load("3d-background-with-white-cubes.jpg").convert()  # Убедитесь, что путь правильный
background_rect = background_image.get_rect()
# def spawn(self):
#     k=1
#     while k==1:
#         self.x=(player.x_spawn) - 600*randint(-1,1)
#         self.y=(player.y_spawn) - 400*randint(-1,1)
#         k=0
#         if self.enemy.x==player.x_spawn and self.enemy.y == player.y_spawn:
#             k=1

kolvo_bullet=[]
while running:
    screen.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed

    if x - r <= 0:  # Если игрок выходит за левую границу
        x = r  # Ограничиваем движение
    elif x + r >= W:  # Если игрок выходит за правую границу
        x = W - r  # Ограничиваем движение
    if y - r <= 0:  # Если игрок выходит за верхнюю границу
        y = r  # Ограничиваем движение
    elif y + r >= H:  # Если игрок выходит за нижнюю границу
        y = H - r  # Ограничиваем движение


    if x - r < 100:  # Игрок близко к левой границе
        bg_x = min(bg_x + speed, 0)  # Фон движется вправо
    elif x + r > W - 100:  # Игрок близко к правой границе
        bg_x = max(bg_x - speed, -(background_rect.width - W))  # Фон движется влево
    if y - r < 100:  # Игрок близко к верхней границе
        bg_y = min(bg_y + speed, 0)  # Фон движется вниз
    elif y + r > H - 100:  # Игрок близко к нижней границе
        bg_y = max(bg_y - speed, -(background_rect.height - H))  # Фон движется вверх

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = Rect(mouse_x, mouse_y, 20, 20)

        if Rect.colliderect(mouse_rect, rect1):
            print('1')







    if rasst(x_enemy, y_enemy, x, y)>r:
        x_enemy, y_enemy = move(x_enemy, y_enemy, x, y, 5)
        rect1 = Rect((x_enemy, y_enemy, 50, 50))


    screen.blit(background_image, (bg_x, bg_y))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    pygame.draw.rect(screen, (0, 255, 0), rect1)
    #pygame.draw.rect(screen, (0, 0, 255), bullet)
    pygame.display.update()
    clock.tick(FPS)
