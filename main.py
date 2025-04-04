import random
from const import *
import pygame
from pygame import *

pygame.init()
from ai_logic import move
TIMER_ONE = USEREVENT + 1
TIMER_TWO = USEREVENT + 2
player_state = 'default'
mob_state = 'mob_default'


move_dict = {
    'right': [pygame.image.load('animations_girl/right/right_1.png'),
              pygame.image.load('animations_girl/right/right_2.png'),
              pygame.image.load('animations_girl/right/right_3.png'),
              pygame.image.load('animations_girl/right/right_4.png')]*2,

    'left': [pygame.image.load('animations_girl/left/left_1.png'),
             pygame.image.load('animations_girl/left/left_2.png'),
             pygame.image.load('animations_girl/left/left_3.png'),
             pygame.image.load('animations_girl/left/left_4.png')]*2,

    'up': [pygame.image.load('animations_girl/up/up_1.png'),
           pygame.image.load('animations_girl/up/up_2.png'),
           pygame.image.load('animations_girl/up/up_3.png'),
           pygame.image.load('animations_girl/up/up_4.png')]*2,

    'down': [pygame.image.load('animations_girl/down/down_1.png'),
             pygame.image.load('animations_girl/down/down_2.png'),
             pygame.image.load('animations_girl/down/down_3.png'),
             pygame.image.load('animations_girl/down/down_4.png')]*2,

    'default': [pygame.image.load('animations_girl/down/down_1.png')] * 8,


    'mob_attak_down': [pygame.image.load('animations_mob/attak/orc1_attack_down.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_down1.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_down2.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_down3.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_down4.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_down5.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_down6.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_down7.png')],


    'mob_default': [pygame.image.load('animations_mob/attak/orc1_attack_down.png')]*8,

    'mob_attak_up': [pygame.image.load('animations_mob/attak/orc1_attack_up.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_up1.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_up2.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_up3.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_up4.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_up5.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_up6.png'),
                  pygame.image.load('animations_mob/attak/orc1_attack_up7.png')],

    'mob_damage':[pygame.image.load('animations_mob/damage/orc1_hurt_down.png'),
                  pygame.image.load('animations_mob/damage/orc1_hurt_down1.png'),
                  pygame.image.load('animations_mob/damage/orc1_hurt_down2.png'),
                  pygame.image.load('animations_mob/damage/orc1_hurt_down3.png'),
                  pygame.image.load('animations_mob/damage/orc1_hurt_down4.png'),
                  pygame.image.load('animations_mob/damage/orc1_hurt_down5.png'),
                  pygame.image.load('animations_mob/damage/orc1_hurt_down6.png'),
                  pygame.image.load('animations_mob/damage/orc1_hurt_down7.png')],

    'mob_death': [pygame.image.load('animations_mob/death/orc1_death_down.png'),
                  pygame.image.load('animations_mob/death/orc1_death_down1.png'),
                  pygame.image.load('animations_mob/death/orc1_death_down2.png'),
                  pygame.image.load('animations_mob/death/orc1_death_down3.png'),
                  pygame.image.load('animations_mob/death/orc1_death_down4.png'),
                  pygame.image.load('animations_mob/death/orc1_death_down5.png'),
                  pygame.image.load('animations_mob/death/orc1_death_down6.png'),
                  pygame.image.load('animations_mob/death/orc1_death_down7.png')],

    'girl_damage': [pygame.image.load('animations_girl/damage/down_1_red.gif')]*8,

    # [pygame.image.load('animations_girl/damage/down_1.png'),
    #                 pygame.image.load('animations_girl/damage/down_1_red.gif'),
    #                 pygame.image.load('animations_girl/damage/down_2.png'),
    #                 pygame.image.load('animations_girl/damage/down_2_red.gif'),
    #                 pygame.image.load('animations_girl/damage/down_3.png'),
    #                 pygame.image.load('animations_girl/damage/down_3_red.gif'),
    #                 pygame.image.load('animations_girl/damage/down_4.png'),
    #                 pygame.image.load('animations_girl/damage/down_4_red.gif'),]

    'mob_l': [pygame.image.load('animations_mob/l/orc1_run_left.png'),
              pygame.image.load('animations_mob/l/orc1_run_left1.png'),
              pygame.image.load('animations_mob/l/orc1_run_left2.png'),
              pygame.image.load('animations_mob/l/orc1_run_left3.png'),
              pygame.image.load('animations_mob/l/orc1_run_left4.png'),
              pygame.image.load('animations_mob/l/orc1_run_left5.png'),
              pygame.image.load('animations_mob/l/orc1_run_left6.png'),
              pygame.image.load('animations_mob/l/orc1_run_left7.png')],

    'mob_r': [pygame.image.load('animations_mob/r/orc1_run_right.png'),
              pygame.image.load('animations_mob/r/orc1_run_right1.png'),
              pygame.image.load('animations_mob/r/orc1_run_right2.png'),
              pygame.image.load('animations_mob/r/orc1_run_right3.png'),
              pygame.image.load('animations_mob/r/orc1_run_right4.png'),
              pygame.image.load('animations_mob/r/orc1_run_right5.png'),
              pygame.image.load('animations_mob/r/orc1_run_right6.png'),
              pygame.image.load('animations_mob/r/orc1_run_right7.png')],

    'mob_up': [pygame.image.load('animations_mob/up/orc1_run_up.png'),
              pygame.image.load('animations_mob/up/orc1_run_up1.png'),
              pygame.image.load('animations_mob/up/orc1_run_up2.png'),
              pygame.image.load('animations_mob/up/orc1_run_up3.png'),
              pygame.image.load('animations_mob/up/orc1_run_up4.png'),
              pygame.image.load('animations_mob/up/orc1_run_up5.png'),
              pygame.image.load('animations_mob/up/orc1_run_up6.png'),
              pygame.image.load('animations_mob/up/orc1_run_up7.png')],

    'mob_down': [pygame.image.load('animations_mob/down/orc1_run_down.png'),
              pygame.image.load('animations_mob/down/orc1_run_down1.png'),
              pygame.image.load('animations_mob/down/orc1_run_down2.png'),
              pygame.image.load('animations_mob/down/orc1_run_down3.png'),
              pygame.image.load('animations_mob/down/orc1_run_down4.png'),
              pygame.image.load('animations_mob/down/orc1_run_down5.png'),
              pygame.image.load('animations_mob/down/orc1_run_down6.png'),
              pygame.image.load('animations_mob/down/orc1_run_down7.png')],

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
            'state': 'mob_default',
            'damage': False,
            'death': False,
            'move':False
        }
    ]


font = pygame.font.Font('alagard-12px-unicode.ttf', 20)

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

background_image = pygame.image.load("1c6d07c2225068915f8d8ad8131f4198 (1).jpg").convert()
background_rect = background_image.get_rect()

heart=pygame.image.load('HB/heart.png')
heart=transform.scale(heart,(32,32))



exp=pygame.image.load('HB/experience.png')

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
        player_move=True
    elif keys[pygame.K_s]:
        y += speed
        player_state = 'down'
        player_move = True
    elif keys[pygame.K_a]:
        x -= speed
        player_state = 'left'
        player_move = True
    elif keys[pygame.K_d]:
        x += speed
        player_state = 'right'
        player_move = True
    else:
        player_state = 'default'
        player_move = False


    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_rect = Rect(mouse_x, mouse_y, 40, 40)
            for enemy in enemies:
                enm_rect = Rect((enemy['x'], enemy['y'], 128,128))
                if Rect.colliderect(mouse_rect, enm_rect):
                    dmg = random.randint(15, 25)
                    if enemy['hp'] - dmg > 1:
                        enemy['hp'] -= dmg
                        enemy['damage']=True
                    else:
                        enemy['damage']=False
                        enemy['death']=True
                        time.set_timer(TIMER_ONE,300)
                        # enemies.remove(enemy)
    elif event.type == pygame.MOUSEBUTTONUP:
        for enemy in enemies:
            enemy['damage']=False



    if current_time - last_time > interval:
        while enemy_kol != enemy_max:
            enemy = spawn_enemies(1)
            if rasst(enemy[0].get('x'), enemy[0].get('y'), x, y) > 200:
                enemies.extend(enemy)
                last_time = current_time
                enemy_kol += 1

    for enemy in enemies:
        if enemy['damage']:
            enemy['state'] = 'mob_damage'
        elif enemy['death']:
            enemy['state'] = 'mob_death'
            if event.type== TIMER_ONE:
                enemies.remove(enemy)
                kill_count+=1
                enemy['death']=False
        elif rasst(enemy['x'] // 2, enemy['y'] // 2, x // 2, y // 2) > 48:
            enemy['x'], enemy['y'],enemy['state'],enemy['move'] = move(
                enemy['x'],
                enemy['y'],
                x,
                y,
                enemy['speed'],
                [e for e in enemies if e is not enemy]
            )
            # enemy['state'] = 'mob_default'
        else:
            if enemy['y']+128<y+96:
                enemy['state']='mob_attak_down'
                if k%10==0:
                    player_state='girl_damage'
                    player_hp-=10
            else:
                enemy['state'] = 'mob_attak_up'
                if k % 10 == 0:
                    player_state = 'girl_damage'
                    player_hp -= 10





        # for j, other_enemy in enumerate(enemies):
        #     if Rect.colliderect(Rect(temp_x,temp_y,enemy['height'],enemy['width']),
        #                           Rect(enemy['x'],enemy['y'],enemy['height'],enemy['width'])):
        #         break
        #             # if (other_enemy is not enemy
        #             #         and other_enemy['x'] <= temp_x <= other_enemy['x'] + other_enemy["width"]
        #             #         and other_enemy['y'] <= temp_y <= other_enemy['y'] + other_enemy["height"]):
        #             #     break
        #
        # else:
        #     enemy['x'] = temp_x
        #     enemy['y'] = temp_y

    if x <= 0:
        x = 0
    elif x + 64 >= W:
        x = W - 64
    if y  <= 0:
        y = 0
    elif y + 96 >= H:
        y = H - 96


    if player_move:
        if x < len_move_fone:
            bg_x = min(bg_x + speed, 0)
        elif x  > W - len_move_fone:
            bg_x = max(bg_x - speed, -(background_rect.width - W))
        if y < len_move_fone:
            bg_y = min(bg_y + speed, 0)
        elif y > H - len_move_fone:  #
            bg_y = max(bg_y - speed, -(background_rect.height - H))


    if kill_count*10 == enemy_max*10:
        print('kards')

    if player_hp<=0:
        print('you lose')
    image = move_dict[player_state][pygame.time.get_ticks() % 8]
    k+=1
    image = pygame.transform.scale(image, (64, 96))
    screen.blit(background_image, (bg_x, bg_y))
    screen.blit(heart,(10,10))
    screen.blit(exp,(170,10))

    for enemy in enemies:
        if enemy['move']:
            image_mob_attak = move_dict[enemy['state']][pygame.time.get_ticks() % 32//4]
            image_mob_attak = pygame.transform.scale(image_mob_attak, (128, 128))

            screen.blit(image_mob_attak, (enemy['x'], enemy['y']))

    # for enemy in enemies:
    #     screen.blit(image_mob_attak, (enemy['x'], enemy['y']))
        # pygame.draw.rect(
        #     screen,
        #     enemy['color'],
        #     (enemy['x'], enemy['y'], enemy['width'], enemy['height'])
        # )
        text = font.render(f'{enemy['hp']}/{enemy_hp}hp', True, RED)
        textRect = text.get_rect()
        textRect.center = (enemy['x'] +82, enemy['y']-30)
        screen.blit(text, textRect)
    text_player_hp = font.render(f'{player_hp}/500hp',True,YELLOW)
    text_exp = font.render(f'{kill_count*10}/{enemy_max*10} exp',True,YELLOW)
    screen.blit(text_player_hp,(52,10))
    screen.blit(text_exp,(212,10))
    screen.blit(image, (x, y))




    pygame.display.update()

    clock.tick(FPS)
