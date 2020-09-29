import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_enents(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_bottom = True
    elif event.key == pygame.K_DOWN:
        ship.moving_top = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_bottom = False
    elif event.key == pygame.K_DOWN:
        ship.moving_top = False


def check_events(ai_settings, screen, ship, bullets):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_enents(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一个子弹并加入编组
    # if len(bullets) < ai_settings.bullet_allowed:
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullte()
    ship.blitme()
    # alien.blitme()l
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    # (len(bullets))
    # 删除发射过的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collsions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collsions(ai_settings, screen, ship, aliens, bullets):
    """响应外星人和子弹碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 外星人全部消失之后，重新生成外星人
    if len(aliens) == 0:
        bullets.empty()
        creat_alien_group(ai_settings, screen, ship, aliens)


def creat_alien_group(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，比计算一下一行可以容纳多少个外星人
    # 外星人之间间距为一个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_alien_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建一行外星人
    for row_number in range(int(number_rows)):
        for alien_number in range(int(number_aliens_x)):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = available_space_x / (2 * alien_width)
    return number_aliens_x


def get_alien_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = available_space_y/(2 * alien_height)
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number, number_rows):
    # 创建一个外星人，并加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_rows
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for align in aliens.sprites():
        if align.check_edges():
            check_fleet_direction(ai_settings, aliens)
            break


def check_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_speed
    ai_settings.alien_speed_factor *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    # 检查外形人是否到达边界
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应飞船被外星人撞毁"""
    if stats.ship_left > 0 :
        # 将ship_left 减1
        stats.ship_left -= 1
        # 清空子弹列表和外星人列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人,并将飞船放在屏幕底端
        creat_alien_group(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停0.5秒
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


























