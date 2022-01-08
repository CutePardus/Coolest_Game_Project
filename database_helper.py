import sqlite3
import pygame


con = sqlite3.connect("saves_and_others.db")


def question(screen, text):
    pygame.draw.rect(screen, 'blue', (250, 250, 500, 125), 0)
    font = pygame.font.Font(None, 50)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (250, 250))
    pygame.draw.rect(screen, 'red', (325, 300, 100, 50), 0)
    pygame.draw.rect(screen, 'green', (575, 300, 100, 50), 0)
    no_text = font.render('Нет', True, (255, 255, 255))
    yes_text = font.render('Да', True, (255, 255, 255))
    screen.blit(no_text, (325, 300))
    screen.blit(yes_text, (575, 300))


def load_save(save_id):
    cur = con.cursor()
    save = cur.execute("SELECT * FROM saves WHERE id=?", (int(save_id),)).fetchone()
    return save


def save_game(save_id, position, hero, health, level, floor, tools):
    cur = con.cursor()
    que = "UPDATE saves SET" + '\n'
    que += f"hero_class='{hero}', your_tools='{str(tools)}', level={level}, health={health}," \
           f" position='{' '.join(position)}', floor='{', '.join(floor)}'"
    que += "WHERE id = ?"
    cur.execute(que, (save_id,))
    con.commit()


def delete(save_id):
    question(screen, f'Удалить сейв №{save_id}?')
    cur = con.cursor()
    que = "UPDATE saves SET" + '\n'
    que += "hero_class='', your_tools='', level=0, health=0," \
           " position='', floor=''"
    que += "WHERE id = ?"
    cur.execute(que, (save_id,))
    con.commit()
