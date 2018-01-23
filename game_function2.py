# -*- coding:utf-8 -*-
import sys,pygame
from bullet2 import Bullet2
def check_keydown_events(event,setscreen,screen,xing,bullets):
    if event.key == pygame.K_RIGHT:
        xing.moving_right = True
    elif event.key == pygame.K_LEFT:
        xing.moving_left = True
    elif event.key == pygame.K_DOWN:
        xing.moving_down = True
    elif event.key == pygame.K_UP:
        xing.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire(setscreen,screen,xing,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event,xing):
    if event.key == pygame.K_RIGHT:
        xing.moving_right = False
    elif event.key == pygame.K_LEFT:
        xing.moving_left = False
    elif event.key == pygame.K_DOWN:
        xing.moving_down = False
    elif event.key == pygame.K_UP:
        xing.moving_up = False

def check_events(setscreen,screen,xing,bullets):
    '''监控鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,setscreen,screen,xing,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,xing)


def update_screen(setscreen,screen,xing,bullets):
    '''更新屏幕图像，显示新屏幕图像'''
    # 每次循环都重新绘制屏幕
    screen.fill(setscreen.bg_color)   #屏幕填充颜色
    #显示飞船
    xing.blitme()
    #显示子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最新绘制的屏幕可见
    pygame.display.flip()

def update_bullets(setscreen,bullets):
    #更新子弹的位置
    bullets.update()

    # 删除消失在屏幕的子弹
    for bullet in bullets.copy():  #从子弹编组的副本中操作
        if bullet.rect.right >= setscreen.screen_width:
            bullets.remove(bullet)
    # print(len(bullets))

def fire(setscreen,screen,xing,bullets):
    #子弹数量没有达到限制时，创建子弹并添加到编组中
    if len(bullets) < setscreen.bullet_allowed:
        new_bullet = Bullet2(setscreen, screen, xing)
        bullets.add(new_bullet)


# def get_number_aliens_x(ai_settings,stars_width):
#     '''计算一行中可以放外星人的个数'''
#     available_space_x = ai_settings.screen_width - 2 * stars_width
#     number_aliens_x = int(available_space_x / (2 * stars_width))
#     return number_aliens_x
#
# def create_alien(ai_settings,screen,stars,stars_number,row_number):
#     # 创建外星人并加入当前的行
#     stars = Stars(ai_settings, screen)
#     stars_width = stars.rect.width
#     stars.x = stars_width + 2 * stars_width * stars_number
#     stars.rect.x = stars.x
#     stars.rect.y = stars.rect.height + 2 * stars.rect.height * row_number
#     stars.add(stars)
#
# def create_fleet(ai_settings,screen,stars,stars_number):
#     '''创建外星人，计算一行中的个数'''
#     stars = Stars(ai_settings,screen)
#     number_aliens_x = get_number_aliens_x(ai_settings,stars.rect.width)
#     number_rows = get_number_rows(ai_settings,stars.rect.height,stars.rect.height)
#     # 创建一行外星人
#     for row_number in range(number_rows):
#         for alien_number in range(number_aliens_x):
#             create_alien(ai_settings,screen,stars,stars_number,row_number)
#
# def get_number_rows(ai_settings,stars_height):
#     '''计算容纳的行数'''
#     available_space_y = (ai_settings.screen_height - 15 * stars_height)
#     number_rows = int(available_space_y / (2 * stars_height))
#     return  number_rows