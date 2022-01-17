import pygame
import sqlite3
from enemy_generator import enemy_generator

enemy_sprites = pygame.sprite.Group()

con = sqlite3.connect('saves_and_others.db')
cur = con.cursor()

enemy = enemy_generator()
pic_location = cur.execute("SELECT pic_location FROM enemies WHERE name = ?", (enemy,)).fetchall()[0][0]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pic_location)
        self.rect = self.image.get_rect()
        self.width = 10  # ширина врага (Размер надо будет подогнать)
        self.height = 20  # высота врага
        self.health = cur.execute("SELECT health FROM enemies WHERE name = ?", (enemy,)).fetchall()[0][0]
        self.damage = cur.execute("SELECT damage FROM enemies WHERE name = ?", (enemy,)).fetchall()[0][0]
        self.cd_attack = 0
        self.all_attacks = []

    def move(self):
        pass


"""
    def attack(self):
        if not self.cd_attack:
            if enemy == "скелет-лучник":
                # он должен стрелять, так что с ним придется страдать отдельно
            else:
                # честно говоря, у меня вообще нет идей, как делать атаки за исключением столкновения спрайтов
                # но для этого надо допилить игрока
            
            

    def get_damage(self, weapon):
        if self.health <= 0:
            смэрт
        # weapon - оружие игрока
        if weapon_x >= self.x and weapon_x <= self.x + width:
            if weapon_y >= self.y and weapon_y <= self.y + height:
                self.health -= weapon_damage
        # эта хренатень максимально примерная, ибо игрока мы еще не запилили
"""


# print(enemy)
# print(cur.execute("SELECT health FROM enemies WHERE name = ?", (enemy,)).fetchall()[0][0])
# print(cur.execute("SELECT damage FROM enemies WHERE name = ?", (enemy,)).fetchall()[0][0])
