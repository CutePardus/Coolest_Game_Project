import sqlite3
import random

con = sqlite3.connect('saves_and_others.db')
cur = con.cursor()


def enemy_generator():
    rarity = random.randint(1, 4)
    possible_enemies = cur.execute('SELECT name FROM enemies WHERE rarity = ?', (rarity,)).fetchall()
    enemy = random.choice(possible_enemies)[0]
    return enemy
