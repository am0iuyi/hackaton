
from math import isqrt
import pygame
from pygame import *
from ai_logic import move




def rasst(x1,y1,x2,y2):
    try:
        return ((x2-x1)**2+(y2-y1**2))**0.5
    except ValueError:
        return False


a
W = 600
H = 600
pygame.init()
screen = pygame.display.set_mode((W, H))
FPS = 100
x = W // 2
y = H // 2
r = 50

x_enemy=100
y_enemy=100

clock = pygame.time.Clock()
running = True
BLACK = (0, 0, 0)

# def spawn(self):
#     k=1
#     while k==1:
#         self.x=(player.x_spawn) - 600*randint(-1,1)
#         self.y=(player.y_spawn) - 400*randint(-1,1)
#         k=0
#         if self.enemy.x==player.x_spawn and self.enemy.y == player.y_spawn:
#             k=1


while running:
    screen.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('вверх')
            elif event.key == pygame.K_s:
                print('вниз')
            elif event.key == pygame.K_a:
                print('влево')
            elif event.key == pygame.K_d:
                print('вправо')

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_rect = Rect(mouse_x, mouse_y, 20, 20)
            if Rect.colliderect(mouse_rect, rect1):
                print('good')
    # while type(rasst(x_enemy, y_enemy, x, y))==int:
    x_enemy, y_enemy = move(x_enemy, y_enemy, x, y, 5)
    rect1 = Rect((x_enemy, y_enemy, 50, 50))
    print(rasst(x_enemy, y_enemy, x, y))


    screen.fill(BLACK)
    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    pygame.draw.rect(screen, (0, 255, 0), rect1)
    pygame.display.update()
    clock.tick(FPS)
