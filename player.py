import pygame
from database_helper import load_tool, load_hero, load_enemy
from drawer import classes, bottom_text, up_text, up_text2
from level_functions import load_image
import random
from enemies import Enemy

game_started = False
save_id = 1
hero = 'Охотница'
current_pos = [0, 0, 0]
all_loot = ['Пузырек яда'] * 20 + ['Зелье исцеления'] * 20
enemy_types = ['Серая крыса', 'Черная крыса', 'Летучая мышь']

class Menu:
    def __init__(self):
        self.first_click = True
        # self.save_chosen = False
        self.class_choosing = True
        self.question = False
        self.hero_class = ''

    def continue_question(self, screen, mouse_pos, text):
        x, y = mouse_pos[0], mouse_pos[1]
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

    def class_buttons(self, mouse_pos):
        global game_started, hero
        classes(screen)
        if not self.first_click:
            x, y = mouse_pos[0], mouse_pos[1]
            if 300 <= x <= 700:
                if 200 <= y <= 300:
                    self.hero_class = 'Воин'
                    hero = self.hero_class
                    game_started = True
                elif 350 <= y <= 450:
                    self.hero_class = 'Охотница'
                    hero = self.hero_class
                    game_started = True
                elif 500 <= y <= 600:
                    self.hero_class = 'Вор'
                    hero = self.hero_class
                    game_started = True
                elif 650 <= y <= 750:
                    self.hero_class = 'Дриадна'
                    hero = self.hero_class
                    game_started = True
        else:
            self.first_click = False

    def get_click(self, mouse_pos):
        if self.class_choosing:
            self.class_buttons(mouse_pos)


class Board:
    def __init__(self, width, height):
        global save_id, current_pos, hero
        self.boss_health = 100
        self.save_id = save_id
        self.target_choosing = False
        self.width = width
        self.height = height
        self.left = 100
        self.top = 100
        self.cell_size = 50
        self.text = ''
        self.tick = 0
        self.text2 = 'Нажмите правой кнопкой мыши на клетку или предмет из инвенторя, чтобы получить описание. Нажатие на пробел для взаимодейсвия с сундуком или предметом на поле'
        self.text3 = 'Ходите при помощи клавиш WSDA, выбирайте предмет, который хотите использовать или клетку, которую хотите атаковать правой кнопкой мыши'
        self.board = [['0' for i in range(width)] for _ in range(height)]
        self.current_pos = current_pos
        for i in range(15):
            m = random.randint(0, self.height - 1)
            n = random.randint(0, self.width - 1)
            self.board[m][n] = '1'
        self.board[self.width - 1][self.height - 1] = 'exit'
        self.current_loot = []
        self.current_loot.append(load_hero(hero)['start_loot'])
        self.health = int(load_hero(hero)['health'])
        self.item = self.current_loot[0]
        for i in range(10):
            e = Enemy()
            e.spawn(self.board, enemy_types)
            # m = random.randint(3, self.height - 1)
            # n = random.randint(3, self.width - 1)
            # if self.board[m][n] != '1' and self.board[m][n] != 'exit':
            #     enemy = random.choice(enemy_types)
            #     hp = load_enemy(enemy)['hp']
            #     self.board[m][n] = f'{enemy}, {hp}'

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        if game_started:
            pygame.draw.rect(screen, 'white', (25, 25, load_hero(hero)['health'] * 5, 20))
            pygame.draw.rect(screen, 'red', (25, 25, self.health * 5, 20))
            for row in range(len(self.board)):
                for column in range(len(self.board[row])):
                    x, y = column * self.cell_size + self.left, row * self.cell_size + self.top
                    floor_img = load_image('floor.png')
                    floor_img = pygame.transform.scale(floor_img, (50, 50))
                    screen.blit(floor_img, (x, y))
                    if self.board[column][row] == '1':
                        chest_img = load_image('Chest.png')
                        chest_img = pygame.transform.scale(chest_img, (50, 50))
                        screen.blit(chest_img, (100 + column * self.cell_size, 100 + row * self.cell_size))
                    elif self.board[column][row] != '0' and self.board[column][row] != 'exit' and \
                            self.board[column][row].split(', ')[0] not in enemy_types and self.board[column][row].split(', ')[0] != 'boss' and\
                            self.board[column][row].split(', ')[0] != 'ghost':
                        img = load_image(str(load_tool(self.board[column][row])['pic']), color_key=-1)
                        img = pygame.transform.scale(img, (50, 50))
                        screen.blit(img, (100 + column * self.cell_size, 100 + row * self.cell_size))
                    elif self.board[column][row] == 'exit':
                        exit_img = load_image('exit.png')
                        exit_img = pygame.transform.scale(exit_img, (50, 50))
                        screen.blit(exit_img, (100 + column * self.cell_size, 100 + row * self.cell_size))
                    elif column == 0 and row == 0:
                        entrance_img = load_image('entrance.png')
                        entrance_img = pygame.transform.scale(entrance_img, (50, 50))
                        screen.blit(entrance_img, (100 + column * self.cell_size, 100 + row * self.cell_size))
                    elif self.board[column][row].split(', ')[0] in enemy_types:
                        enemy = self.board[column][row].split(', ')[0]
                        if self.tick % 2 == 0:
                            enemy_img = load_image(load_enemy(enemy)['picture'], color_key=-1)
                            enemy_img = pygame.transform.scale(enemy_img, (50, 50))
                            screen.blit(enemy_img, (100 + column * self.cell_size, 100 + row * self.cell_size))
                            self.tick += 1
                        else:
                            s = load_enemy(enemy)['picture']
                            s = '2.'.join(s.split('.'))
                            enemy_img = load_image(s, color_key=-1)
                            enemy_img = pygame.transform.scale(enemy_img, (50, 50))
                            screen.blit(enemy_img, (100 + column * self.cell_size, 100 + row * self.cell_size))
                            self.tick += 1
                        if self.current_pos[0] - load_enemy(enemy)['range'] <= column <= self.current_pos[0] + \
                                load_enemy(enemy)['range'] and \
                                self.current_pos[1] - load_enemy(enemy)['range'] <= row <= self.current_pos[1] + \
                                load_enemy(enemy)['range']:
                            self.get_attacked(self.board[column][row].split(', ')[0])
                    elif self.board[column][row].split(', ')[0] == 'boss':
                        boss_img = load_image('boss.png', color_key=-1)
                        boss_img = pygame.transform.scale(boss_img, (50, 50))
                        screen.blit(boss_img, (100 + column * self.cell_size, 100 + row * self.cell_size))
                        self.boss_attack([column, row])
                    elif self.board[column][row].split(', ')[0] == 'ghost':
                        ghost_img = load_image('ghost.png', color_key=-1)
                        ghost_img = pygame.transform.scale(ghost_img, (50, 50))
                        screen.blit(ghost_img, (100 + column * self.cell_size, 100 + row * self.cell_size))

                s = set()
                for elem in self.current_loot:
                    s.add(elem)
                self.loot2 = []
                self.loot2.extend(s)
                pygame.draw.rect(screen, (54, 11, 204), (900, 250, 75, 300))
                for i in range(len(self.loot2)):
                    pygame.draw.rect(screen, (255, 255, 255), (901, 251 + i * 75, 74, 74))
                    img = load_image(str(load_tool(self.loot2[i])['pic']), color_key=-1)
                    img = pygame.transform.scale(img, (75, 75))
                    screen.blit(img, (900, 250 + i * 75))
                    text = str(self.current_loot.count(self.loot2[i]))
                    font = pygame.font.Font(None, 50)
                    text = font.render(text, True, (0, 0, 0))
                    screen.blit(text, (960, 300 + i * 75))
                pygame.draw.rect(screen, 'red', (900, 10, 75, 20))
                font = pygame.font.Font(None, 20)
                text = font.render('Выход', True, (255, 254, 254))
                screen.blit(text, (910, 10))
                if len(self.current_loot) == 1:
                    self.current_loot = []
                    self.current_loot.append(load_hero(hero)['start_loot'])
                hero_img = load_image(load_hero(hero)['pic'], color_key=-1)
                hero_img = pygame.transform.scale(hero_img, (50, 50))
                screen.blit(hero_img, (100 + self.current_pos[0] * self.cell_size, 100 + self.current_pos[1] * self.cell_size))
                font = pygame.font.Font(None, 25)
                text = font.render(f'Вы находитесь на этаже {current_pos[2]}', True, 'white')
                screen.blit(text, (10, 5))
                pygame.draw.rect(screen, 'white', (25, 25, load_hero(hero)['health'] * 5, 20))
                pygame.draw.rect(screen, 'red', (25, 25, self.health * 5, 20))
                font = pygame.font.Font(None, 20)
                text = font.render(str(self.health), True, (255, 254, 254))
                screen.blit(text, (25, 25))
                bottom_text(screen, self.text)
                up_text(screen, self.text2)
                up_text2(screen, self.text3)
        else:
            s = set()
            for elem in self.current_loot:
                s.add(elem)
            self.loot2 = []
            self.loot2.extend(s)
            pygame.draw.rect(screen, (54, 11, 204), (900, 250, 75, 300))
            for i in range(len(self.loot2)):
                if self.item != self.loot2[i]:
                    pygame.draw.rect(screen, (255, 255, 255), (901, 251 + i * 75, 74, 74))
                elif self.target_choosing and self.item == self.loot2[i]:
                    pygame.draw.rect(screen, 'green', (901, 251 + i * 75, 74, 74))
                img = load_image(str(load_tool(self.loot2[i])['pic']), color_key=-1)
                img = pygame.transform.scale(img, (75, 75))
                screen.blit(img, (900, 250 + i * 75))
                text = str(self.current_loot.count(self.loot2[i]))
                font = pygame.font.Font(None, 50)
                text = font.render(text, True, (0, 0, 0))
                screen.blit(text, (960, 300 + i * 75))
            pygame.draw.rect(screen, 'red', (900, 10, 75, 20))
            font = pygame.font.Font(None, 20)
            text = font.render('Выход', True, (255, 254, 254))
            screen.blit(text, (910, 10))
            if len(self.current_loot) == 1:
                self.current_loot = []
                self.current_loot.append(load_hero(hero)['start_loot'])
            hero_img = load_image(load_hero(hero)['pic'], color_key=-1)
            hero_img = pygame.transform.scale(hero_img, (50, 50))
            screen.blit(hero_img,
                        (100 + self.current_pos[0] * self.cell_size, 100 + self.current_pos[1] * self.cell_size))
            font = pygame.font.Font(None, 25)
            text = font.render(f'Вы находитесь на этаже {current_pos[2]}', True, 'white')
            screen.blit(text, (10, 5))
            pygame.draw.rect(screen, 'white', (25, 25, load_hero(hero)['health'] * 5, 20))
            pygame.draw.rect(screen, 'red', (25, 25, self.health * 5, 20))
            font = pygame.font.Font(None, 20)
            text = font.render(str(self.health), True, (255, 254, 254))
            screen.blit(text, (25, 25))
            bottom_text(screen, self.text)
            up_text(screen, self.text2)
            up_text2(screen, self.text3)

    def get_cell(self, mouse_pos):
        if 900 <= mouse_pos[0] <= 975 and 10 <= mouse_pos[1] <= 30:
            self.exit('Заходите поиграть еще)')
            return 0, 0
        elif 900 <= mouse_pos[0] <= 975 and 250 < mouse_pos[1] <= 325:
            self.active_item(0)
            return 16, 16
        elif 900 <= mouse_pos[0] <= 975 and 325 < mouse_pos[1] <= 400 and len(self.loot2) >= 1:
            self.active_item(1)
            return 17, 17
        elif 900 <= mouse_pos[0] <= 975 and 400 < mouse_pos[1] <= 475 and len(self.loot2) >= 2:
            self.active_item(2)
            return 18, 18
        elif 900 <= mouse_pos[0] <= 975 and 550 < mouse_pos[1] <= 625 and len(self.loot2) >= 3:
            self.active_item(3)
            return 19, 19
        else:
            x, y = (mouse_pos[0] - self.top) // self.cell_size, (mouse_pos[1] - self.left) // self.cell_size
            if 0 <= x <= self.width and 0 <= y <= self.height:
                return x, y
            else:
                return tuple([16, 16])

    def boss_attack(self, pos):
        if pos[0] - 3 <= current_pos[0] <= pos[0] + 3 and pos[1] - 3 <= current_pos[1] <= pos[1] + 3:
            boss_move = random.randint(1, 5)
            if boss_move == 1:
                self.board[random.randint(0, 14)][random.randint(0, 14)] = f'ghost, {1}'
            elif boss_move == 2:
                self.board[random.randint(0, 14)][random.randint(0, 14)] = f'boss, {self.boss_health}'
                self.board[pos[0]][pos[1]] = '0'
            elif boss_move == 3:
                self.health -= 6
                if self.health <= 0:
                    self.exit('Жаль, а ведь Вы были так близко(')
            else:
                pass

    def on_click(self, cell_coords):
        x, y = cell_coords[0], cell_coords[1]
        if 'atc' in load_tool(self.item)['abilities'].split(', '):
            if self.target_choosing and self.current_pos[0] - load_tool(self.item)['range'] <= x <= self.current_pos[0] + load_tool(self.item)['range'] and\
                    self.current_pos[1] - load_tool(self.item)['range'] <= y <= self.current_pos[1] + load_tool(self.item)['range']:
                if self.board[x][y].split(', ')[0] in enemy_types or self.board[x][y].split(', ')[0] == 'boss' or\
                        self.board[x][y].split(', ')[0] == 'ghost':
                    enemy_01 = self.board[x][y].split(', ')
                    your_damage = load_tool(self.item)['ability_num']
                    if int(enemy_01[1]) <= your_damage and enemy_01[0] != 'boss':
                        self.board[x][y] = '0'
                    elif int(enemy_01[1]) <= your_damage:
                        self.exit(f'Невероятно!!! Вы прошли игру за класс {hero}, попробуйте теперь за другой')
                    else:
                        self.board[x][y] = f'{enemy_01[0]}, {int(enemy_01[1]) - your_damage}'
                    if load_tool(self.item)['rarity'] != 1:
                        self.target_choosing = False
                        self.current_loot.remove(self.item)
                else:
                    if load_tool(self.item)['rarity'] != 1:
                        self.target_choosing = False
                        self.current_loot.remove(self.item)
            else:
                pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def active_item(self, item_num):
        if 'atc' in load_tool(self.loot2[item_num])['abilities'].split(', '):
            self.target_choosing = True
            self.item = self.loot2[item_num]
        if 'heal' in load_tool(self.loot2[item_num])['abilities'].split(', '):
            self.item = self.loot2[item_num]
            if self.health + load_tool(self.loot2[item_num])['ability_num'] <= int(load_hero(hero)['health']):
                self.health += load_tool(self.loot2[item_num])['ability_num']
                if load_tool(self.item)['rarity'] != 1:
                    self.current_loot.remove(self.item)
            elif self.health != int(load_hero(hero)['health']):
                self.health = int(load_hero(hero)['health'])
                if load_tool(self.item)['rarity'] != 1:
                    self.current_loot.remove(self.item)
            else:
                print('ваше здоровье и так максимальное')
        if 'end' in load_tool(self.loot2[item_num])['abilities'].split(', '):
            exit()

    def new_level(self):
        global current_pos
        if current_pos[2] != 8:
            self.board = [['0' for i in range(self.width)] for _ in range(self.height)]
            for i in range(15):
                m = random.randint(0, self.height - 1)
                n = random.randint(0, self.width - 1)
                self.board[m][n] = '1'
            self.board[self.height - 1][self.width - 1] = 'exit'
            for i in range(10):
                e = Enemy()
                e.spawn(self.board, enemy_types)
        else:
            self.board = [['0' for i in range(self.width)] for _ in range(self.height)]
            self.board[7][7] = f'boss, {self.boss_health}'
        self.current_pos = [0, 0, current_pos[2] + 1]
        current_pos = [0, 0, current_pos[2] + 1]

    def exit(self, text):
        global running
        print(text)
        running = False

    def get_attacked(self, enemy_type):
        self.health -= load_enemy(enemy_type)['damage']
        if self.health <= 0:
            self.exit('Похоже Вы умерли(((')

    def get_button(self, unicod):
        if unicod == 's':
            if self.current_pos[1] != 14:
                current_pos[1] += 1
        elif unicod == 'w':
            if self.current_pos[1] != 0:
                current_pos[1] -= 1
        elif unicod == 'a':
            if self.current_pos[0] != 0:
                current_pos[0] -= 1
        elif unicod == 'd':
            if self.current_pos[0] != 14:
                current_pos[0] += 1
        elif unicod == ' ':
            if self.board[current_pos[0]][current_pos[1]] == '1':
                self.board[current_pos[0]][current_pos[1]] = random.choice(all_loot)
            elif self.board[current_pos[0]][current_pos[1]] == 'exit':
                self.new_level()
            elif self.board[current_pos[0]][current_pos[1]] != '0':
                self.current_loot.append(self.board[current_pos[0]][current_pos[1]])
                self.board[current_pos[0]][current_pos[1]] = '0'
        self.current_pos = current_pos

    def on_r_click(self, cell_coords):
        x, y = cell_coords[0], cell_coords[1]
        if x <= 15 and y <= 15:
            if self.board[x][y] == '0':
                self.text = 'Покрытый плесенью и грязью пол'
            elif self.board[x][y].split(', ')[0] in enemy_types or self.board[x][y].split(', ')[0] == 'boss' or self.board[x][y].split(', ')[0] == 'ghost':
                e = self.board[x][y].split(', ')
                if e[0] in enemy_types:
                    e_start = load_enemy(e[0])['hp']
                else:
                    e_start = 100
                self.text = f'{e[0]}, здоровье {e[1]} из {e_start}'
            elif self.board[x][y] == '1':
                self.text = 'Сундук. Может быть в нем будет что-то полезное'
        elif x > 15:
            self.text = '\n'.join(load_tool(self.loot2[x - 16])['desc'].split('&'))

    def get_right_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_r_click(cell)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    start_screen = load_image('start_screen.png')
    start_screen = pygame.transform.scale(start_screen, (1000, 1000))
    screen.blit(start_screen, (0, 0))
    menu = Menu()
    board = Board(15, 15)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 3:
                    if game_started:
                        board.get_click(event.pos)
                    else:
                        menu.get_click(event.pos)
                else:
                    if game_started:
                        board.get_right_click(event.pos)
            if event.type == pygame.KEYDOWN:
                board.get_button(event.unicode)
        if game_started:
            screen.fill((0, 0, 0))
            board.render(screen)
        pygame.display.flip()
    pygame.display.flip()
