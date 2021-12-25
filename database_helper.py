import sqlite3


con = sqlite3.connect("saves_and_others.db")


def load_saves():
    cur = con.cursor()
    saves = cur.execute("SELECT * FROM saves").fetchall()
    return saves


def save_game(save_id, position, hero, health, level, floor, tools):
    cur = con.cursor()
    que = "UPDATE saves SET" + '\n'
    que += f"hero_class='{hero}', your_tools='{str(tools)}', level={level}, health={health}," \
           f" position='{' '.join(position)}', floor='{', '.join(floor)}'"
    que += "WHERE id = ?"
    cur.execute(que, (save_id,))
    con.commit()


def delete(save_id):
    cur = con.cursor()
    que = "UPDATE saves SET" + '\n'
    que += "hero_class='', your_tools='', level=0, health=0," \
           " position='', floor=''"
    que += "WHERE id = ?"
    cur.execute(que, (save_id,))
    con.commit()