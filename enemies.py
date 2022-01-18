import pygame
import sqlite3
from database_helper import load_enemy
from enemy_generator import enemy_generator
import random
from level_functions import load_image

enemy_sprites = pygame.sprite.Group()

con = sqlite3.connect('saves_and_others.db')
cur = con.cursor()
screen = pygame.surface.Surface((1000, 1000))

enemy_type = enemy_generator()
pic_location = load_enemy(enemy_type)['picture']
enemies = []

def weapon(weapon_name):  # оружие игрока и его данные
    global con, cur
    weapon_range = cur.execute("SELECT range FROM tools WHERE name = ?", (weapon_name,)).fetchall()[0][0]
    weapon_damage = cur.execute("SELECT damage FROM tools WHERE name = ?", (weapon_name,)).fetchall()[0][0]
    return weapon_damage, weapon_range


class Enemy(pygame.sprite.Sprite):  # класс врага
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(pic_location)
        self.rect = self.image.get_rect()
        self.health = load_enemy(enemy_type)['hp']
        self.damage = load_enemy(enemy_type)['damage']
        self.range = load_enemy(enemy_type)['range']
        self.rarity = load_enemy(enemy_type)['rarity']

    def spawn(self):  # корды спавна мобов
        enemy_pos = [random.randint(3, 15), random.randint(3, 15), 0]
        return enemy_pos

    def get_attacked(self, player_pos, weapon_name):  # получение урона от игрока
        self.enemy_pos = self.spawn()
        weapon_damage, weapon_range = weapon(weapon_name)
        if self.enemy_pos[0] - weapon_range <= player_pos[0] <= self.enemy_pos[0] + weapon_range and \
                self.enemy_pos[1] - weapon_range <= player_pos[1] <= self.enemy_pos[1] + weapon_range:
            self.health -= weapon_damage
        if self.health <= 0:
            enemies.remove(self)


    def attack(self, player_pos):
        print('ok')


for i in range(10):
    e = Enemy()
    enemies.append(e)

