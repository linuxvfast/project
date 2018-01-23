#-*- coding:utf-8-*-
import sys,pygame
from bullet import Bullet
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''响应按键的情况'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一个子弹并加入到编组中
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)


def check_keyup_events(event,ship):
    '''响应松开按键的情况'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    '''更新屏幕上的图像，显示最新的图像'''
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    '''更新子弹的位置，并删除已经消失的子弹'''
    #更新子弹的位置
    bullets.update()

    # 删除已经消失在屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))