import pygame
import sqlite3
from database_helper import load_enemy
from enemy_generator import enemy_generator
import random

enemy_sprites = pygame.sprite.Group()

con = sqlite3.connect('saves_and_others.db')
cur = con.cursor()

enemy_type = enemy_generator()
pic_location = cur.execute("SELECT pic_location FROM enemies WHERE name = ?", (enemy_type,)).fetchall()[0][0]


def weapon(weapon_name):  # оружие игрока и его данные
    global con, cur
    weapon_range = cur.execute("SELECT range FROM tools WHERE name = ?", (weapon_name,)).fetchall()[0][0]
    weapon_damage = cur.execute("SELECT damage FROM tools WHERE name = ?", (weapon_name,)).fetchall()[0][0]
    return weapon_damage, weapon_range


class Enemy(pygame.sprite.Sprite):  # класс врага
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pic_location)
        self.rect = self.image.get_rect()
        self.health = load_enemy(enemy_type)['hp']
        self.damage = load_enemy(enemy_type)['damage']
        self.range = load_enemy(enemy_type)['range']
        self.rarity = load_enemy(enemy_type)['rarity']

    def spawn(self):  # корды спавна мобов
        enemy_pos = [random.randint(3, 15), random.randint(3, 15), 0]
        return enemy_pos

    def get_attacked(self, player_pos, weapon_name):  # получение урона от игрока
        enemy_pos = self.spawn()
        weapon_damage, weapon_range = weapon(weapon_name)
        if enemy_pos[0] - weapon_range <= player_pos[0] <= enemy_pos[0] + weapon_range and \
                enemy_pos[1] - weapon_range <= player_pos[1] <= enemy_pos[1] + weapon_range:
            self.health -= weapon_damage
