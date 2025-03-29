import random
from const import *
import pygame
from pygame import *

pygame.init()
from ai_logic import move

player_state = 'default'
move_dict = {
    'right': [pygame.image.load('animations_girl/right/right_1.png'),
              pygame.image.load('animations_girl/right/right_2.png'),
              pygame.image.load('animations_girl/right/right_3.png'),
              pygame.image.load('animations_girl/right/right_4.png')],

    'left': [pygame.image.load('animations_girl/left/left_1.png'),
             pygame.image.load('animations_girl/left/left_2.png'),
             pygame.image.load('animations_girl/left/left_3.png'),
             pygame.image.load('animations_girl/left/left_4.png')],

    'up': [pygame.image.load('animations_girl/up/up_1.png'),
           pygame.image.load('animations_girl/up/up_2.png'),
           pygame.image.load('animations_girl/up/up_3.png'),
           pygame.image.load('animations_girl/up/up_4.png')],

    'down': [pygame.image.load('animations_girl/down/down_1.png'),
             pygame.image.load('animations_girl/down/down_2.png'),
             pygame.image.load('animations_girl/down/down_3.png'),
             pygame.image.load('animations_girl/down/down_4.png')],

    'default': [pygame.image.load('animations_girl/down/down_1.png')] * 4
}

enemies = []
last_time = pygame.time.get_ticks()


def rasst(x1, y1, x2, y2):
    try:
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    except ValueError:
        return False


def spawn_enemies(count=1):
    return [
        {
            'x': random.randint(0, H - enemy_size),
            'y': random.randint(0, W - enemy_size),
            'width': enemy_size,
            'height': enemy_size,
            'color': enemy_color,
            'speed': enemy_speed,
            'hp': enemy_hp,
            'damage': None
        }
    ]


font = pygame.font.Font('alagard-12px-unicode.ttf', 26)

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
running = True
background_image = pygame.image.load("background.png").convert()
background_rect = background_image.get_rect()

kolvo_bullet = []
while running:
    screen.fill(BLACK)
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYUP:
        move_r = False
        move_l = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
        player_state = 'up'
    elif keys[pygame.K_s]:
        y += speed
        player_state = 'down'
    elif keys[pygame.K_a]:
        x -= speed
        player_state = 'left'
    elif keys[pygame.K_d]:
        x += speed
        player_state = 'right'
    else:
        player_state = 'default'

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_rect = Rect(mouse_x, mouse_y, 40, 40)
            for enemy in enemies:
                enm_rect = Rect((enemy['x'], enemy['y'], enemy['width'], enemy['height']))
                if Rect.colliderect(mouse_rect, enm_rect):
                    dmg = random.randint(15, 25)
                    if enemy['hp'] - dmg > 1:
                        enemy['hp'] -= dmg
                        enemy['damage'] = dmg
                    else:

                        enemies.remove(enemy)

    if current_time - last_time > interval:
        while enemy_kol != enemy_max:
            enemy = spawn_enemies(1)
            if rasst(enemy[0].get('x'), enemy[0].get('y'), x, y) > 200:
                enemies.extend(enemy)
                last_time = current_time
                enemy_kol += 1

    for i, enemy in enumerate(enemies):
        if rasst(enemy['x'], enemy['y'], x, y) > r:#убрать
            temp_x, temp_y = move(enemy['x'], enemy['y'], x, y, 5)
            for j, other_enemy in enumerate(enemies):
                if (other_enemy is not enemy
                        and other_enemy['x'] <= temp_x <= other_enemy['x'] + other_enemy["width"]
                        and other_enemy['y'] <= temp_y <= other_enemy['y'] + other_enemy["height"]):
                    break
                # if pygame.Rect(enemy['x']).colliderect(pygame.Rect()):
                #     break
            else:
                enemy['x'] = temp_x
                enemy['y'] = temp_y

    if x - r <= 0:
        x = r
    elif x + r >= W:
        x = W - r
    if y - r <= 0:
        y = r
    elif y + r >= H:
        y = H - r

    if x - r < len_move_fone:

        bg_x = min(bg_x + speed, 0)
    elif x + r > W - len_move_fone:
        bg_x = max(bg_x - speed, -(background_rect.width - W))
    if y - r < len_move_fone:
        bg_y = min(bg_y + speed, 0)
    elif y + r > H - len_move_fone:  #
        bg_y = max(bg_y - speed, -(background_rect.height - H))

    # if move_l:
    #     value_l+=1
    # else:
    #     if value_l%2!=0:
    #         value_l+=1
    # if value_l>=4:
    #     value_l=0
    # image_l = girl_move_l[value_l]
    # image_l = pygame.transform.scale(image_l, (60, 76))

    # if move_r:
    #     value+=1
    # else:
    #     if value%2!=0:
    #         value+=1
    # if value>=4:
    #     value=0
    image = move_dict[player_state][pygame.time.get_ticks() % 4]
    image = pygame.transform.scale(image, (64, 64))

    screen.blit(background_image, (bg_x, bg_y))
    # pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    # pygame.draw.rect(screen, (0, 255, 0), rect1)
    # pygame.draw.rect(screen, (0, 0, 255), bullet)

    for enemy in enemies:
        pygame.draw.rect(
            screen,
            enemy['color'],
            (enemy['x'], enemy['y'], enemy['width'], enemy['height'])
        )
        text = font.render(f'{enemy['hp']}/100', True, RED)
        textRect = text.get_rect()
        textRect.center = (enemy['x'] + enemy_size // 2, enemy['y'] - 20)
        screen.blit(text, textRect)

    screen.blit(image, (x, y))
    # screen.blit(image_l, (x, y))

    pygame.display.update()
    clock.tick(FPS)
