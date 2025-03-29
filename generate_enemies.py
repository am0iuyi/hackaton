import pygame
import random

#инициализация PyGame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Управление врагами")
clock = pygame.time.Clock()

#глобальные переменные
enemies = []
spawn_count = 5
enemy_size_range = 40
enemy_color = (255, 50, 50)

# Функция создания врагов
def spawn_enemies(count=1):
    return [
        {
            'x': random.randint(0, 800 - size),
            'y': random.randint(0, 600 - size),
            'width': size,
            'height': size,
            'color': enemy_color,
            'speed': [random.uniform(-2, 2), random.uniform(-2, 2)]
        }
        for size in [random.randint(enemy_size_range,enemy_size_range) for _ in range(count)]
    ]

#функция отрисовки врагов
def render_enemies():
    for enemy in enemies:
        pygame.draw.rect(
            screen, 
            enemy['color'], 
            (enemy['x'], enemy['y'], enemy['width'], enemy['height'])
        )


#основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #добавление врага по нажатию ЛКМ
                enemies.extend(spawn_enemies(1))
            
    #Обновление позиций врагов
    for enemy in enemies:
        enemy['x'] += enemy['speed'][0]
        enemy['y'] += enemy['speed'][1]
        if enemy['x'] < 0 or enemy['x'] + enemy['width'] > 800:
            enemy['speed'][0] *= -1
        if enemy['y'] < 0 or enemy['y'] + enemy['height'] > 600:
            enemy['speed'][1] *= -1
    
    #отрисовка
    screen.fill((0, 0, 0))
    render_enemies()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()