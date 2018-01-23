# -*- coding:utf-8 -*-
'''控制循环事件'''
import sys,pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from setting import Settings
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''响应按键的情况'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # elif event.key == pygame.K_UP:
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event,ship):
    '''响应松开按键的情况'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    # elif event.key == pygame.K_UP:
    #     ship.moving_up = False
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_bottom = False

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    #响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
                #向右移动飞船
                # ship.rect.centerx += 1
            #     ship.moving_right = True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''玩家点击start按钮时开始游戏'''
    #判断屏幕鼠标点击的x,y轴坐标是否在按钮的矩形中
    # 在矩形中状态为true开始游戏，反之游戏不启动
    # if play_button.rect.collidepoint(mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏的设置
        ai_settings.initialize_dynamic_settings()

        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏的统计信息
        stats.reset_stats()
        stats.game_active = True

        #情况外星人和子弹的列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并让飞船居中显示
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    '''更新屏幕图像，显示新屏幕图像'''
    # 每次循环都重新绘制屏幕
    # screen.fill(bg_color)
    screen.fill(ai_settings.bg_color)   #屏幕填充颜色
    #在飞船和外星人后面重绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()                       #绘制飞船
    aliens.draw(screen)                      #画外星人
    sb.show_score()

    #判断游戏是否激活，没有激活时显示开始按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最新绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''更新子弹的位置并消除已经消失的子弹'''
    #Update the position of the bullets
    bullets.update()

    #Delete disappeared（消失） in the bullets（子弹） of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))  # 测试子弹的数量

    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    '''控制显示子弹的数量'''
    # 创建一个子弹，并加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    '''计算一行中可以放外星人的个数'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    # 创建外星人并加入当前的行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人，计算一行中的个数'''
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    # 创建一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算容纳的行数'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return  number_rows

def update_alien(ai_settings,stats,screen,ship,aliens,bullets):
    '''更新所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检查外星人和飞船是否有重叠,有重叠减少飞船数量
    # if pygame.sprite.spritecollideany(ship,aliens):
    #     print('Ship hit!!!')
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
def check_fleet_edges(ai_settings,aliens):
    '''检测外星人是否到达边缘'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''外星人到达边缘之后更改移动方向，并向下移动'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    # 检查子弹是否击中外行星，如果击中，删除子弹和外星人
    # 遍历子弹组和外星人组，并对两个重合的矩形进行比较看是否重叠
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 如果外星人的组长度为0，重新创建一组外星人
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        bullets.empty()  # 删除编组中剩余的所有子弹
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应飞船被外星人撞到的情况'''
    if stats.ships_left > 0:
        stats.ships_left -= 1   #外星人和飞船发生重叠，飞船数量减1

        #清空子弹和外星人
        aliens.empty()
        bullets.empty()

        #创建新的外星人和飞船,并将飞船居中放置
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查外星人是否到达屏幕底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            '''如果外星人下降到屏幕底部超出屏幕底部，判断为飞船被撞，减少一个飞船数量'''
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break




