import pygame
from database_helper import load_save, save_game, delete, load_tool, load_hero, load_enemy
from drawer import classes, saves
from level_functions import load_image
import random

game_started = False
save_id = 0
hero = 'Охотница'
current_pos = [0, 0, 0]
# all_sprites = pygame.sprite.Group()
all_loot = ['Пузырек яда'] * 20 + ['Зелье исцеления'] * 20
enemy_list = []

class Menu:
    def __init__(self):
        self.first_click = True
        self.save_chosen = False
        self.class_choosing = False
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


    def choose_save(self, mouse_pos):
        global save_id
        if self.first_click:
            self.first_click = False
            saves(screen)
        else:
            saves(screen)
            x, y = mouse_pos[0], mouse_pos[1]
            if 300 <= x <= 700:
                if 200 <= y <= 300:
                    save_id = 1
                    self.save_chosen = True
                    self.class_choosing = True
                    classes(screen)
                elif 350 <= y <= 450:
                    save_id = 2
                    self.save_chosen = True
                    self.class_choosing = True
                    classes(screen)
                elif 500 <= y <= 600:
                    save_id = 3
                    self.save_chosen = True
                    self.class_choosing = True
                    classes(screen)
                elif 650 <= y <= 750:
                    save_id = 4
                    self.save_chosen = True
                    self.class_choosing = True
                    classes(screen)
            if self.save_chosen:
                if load_save(save_id)[1]:
                    self.question = True
                    print(load_save(save_id))

    def class_buttons(self, mouse_pos):
        global game_started, hero
        classes(screen)
        x, y = mouse_pos[0], mouse_pos[1]
        if 300 <= x <= 700:
            if 200 <= y <= 300:
                self.hero_class = 'Воин'
                print(self.hero_class)
                hero = self.hero_class
                print(hero)
                game_started = True
            elif 350 <= y <= 450:
                self.hero_class = 'Охотница'
                print(self.hero_class)
                hero = self.hero_class
                print(hero)
                game_started = True
            elif 500 <= y <= 600:
                self.hero_class = 'Вор'
                print(self.hero_class)
                hero = self.hero_class
                print(hero)
                game_started = True
            elif 650 <= y <= 750:
                self.hero_class = 'Дриадна'
                print(self.hero_class)
                hero = self.hero_class
                print(hero)
                game_started = True


    def get_click(self, mouse_pos):
        if not self.save_chosen:
            self.choose_save(mouse_pos)
        elif self.class_choosing:
            self.class_buttons(mouse_pos)

    # def right_b_click(self, mouse_pos):
    #



class Board:
    def __init__(self, width, height):
        global save_id, current_pos, hero
        self.save_id = save_id
        self.board = [['0' for i in range(width)] for _ in range(height)]
        self.current_pos = current_pos
#        self.floor = ';'.join([' '.join((self.board[i]) for i in range(height))])
        self.width = width
        self.height = height
        self.left = 100
        self.top = 100
        self.cell_size = 50
        for i in range(15):
            m = random.randint(0, self.height - 1)
            n = random.randint(0, self.width - 1)
            self.board[m][n] = '1'
        self.board[self.width - 1][self.height - 1] = 'exit'
        self.current_loot = []
        self.current_loot.append(load_hero(hero)['start_loot'])
        self.health = int(load_hero(hero)['health'])
        self.target_choosing = False
        self.item = self.current_loot[0]
        # if hero != 'Охотница':
        #     self.current_loot = []
        #     self.current_loot.append(load_hero(hero)['start_loot'])
        #     print(self.current_loot)
        print(self.current_loot)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        if game_started:
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
                    elif self.board[column][row] != '0' and self.board[column][row] != 'exit':
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
            pygame.draw.rect(screen, 'white', (25, 25, load_hero(hero)['health'] * 5, 20))
            pygame.draw.rect(screen, 'red', (25, 25, self.health * 5, 20))
            font = pygame.font.Font(None, 20)
            text = font.render(str(self.health), True, (255, 254, 254))
            screen.blit(text, (25, 10))

    def get_cell(self, mouse_pos):
        if 900 <= mouse_pos[0] <= 975 and 10 <= mouse_pos[1] <= 30:
            print('ok')
            # save_game(self.save_id, )
            return tuple([16, 16])
        elif 900 <= mouse_pos[0] <= 975 and 250 < mouse_pos[1] <= 325:
            self.active_item(0)
            return 16, 16
        elif 900 <= mouse_pos[0] <= 975 and 325 < mouse_pos[1] <= 400 and len(self.loot2) >= 1:
            self.active_item(1)
            return 16, 16
        elif 900 <= mouse_pos[0] <= 975 and 400 < mouse_pos[1] <= 475 and len(self.loot2) >= 2:
            self.active_item(2)
            return 16, 16
        elif 900 <= mouse_pos[0] <= 975 and 550 < mouse_pos[1] <= 625 and len(self.loot2) >= 3:
            self.active_item(3)
            return 16, 16
        else:
            x, y = (mouse_pos[0] - self.top) // self.cell_size, (mouse_pos[1] - self.left) // self.cell_size
            if 0 <= x <= self.width and 0 <= y <= self.height:
                return x, y
            else:
                print('None')
                return tuple([16, 16])

    def on_click(self, cell_coords):
        x, y = cell_coords[0], cell_coords[1]
        if self.target_choosing and self.current_pos[0] - load_tool(self.item)['range'] <= x <= self.current_pos[0] + load_tool(self.item)['range'] and\
                self.current_pos[1] - load_tool(self.item)['range'] <= y <= self.current_pos[1] + load_tool(self.item)['range']:
            if self.board[x][y] in enemy_list:
                if load_tool(self.item)['rarity'] != 1:
                    self.target_choosing = False
                    self.current_loot.remove(self.item)
            else:
                print(self.item)
                if load_tool(self.item)['rarity'] != 1:
                    self.target_choosing = False
                    self.current_loot.remove(self.item)
        else:
            print('you can not attack this spot')

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def active_item(self, item_num):
        if 'atc' in load_tool(self.loot2[item_num])['abilities'].split(', '):
            self.target_choosing = True
            self.item = self.loot2[item_num]
            print(item_num)
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

    def new_level(self):
        global current_pos
        self.board = [['0' for i in range(self.width)] for _ in range(self.height)]
        for i in range(15):
            m = random.randint(0, self.height - 1)
            n = random.randint(0, self.width - 1)
            self.board[m][n] = '1'
        self.board[self.height - 1][self.width - 1] = 'exit'
        self.current_pos = [0, 0, current_pos[2] + 1]
        current_pos = [0, 0, current_pos[2] + 1]
        print(self.board)

    def exit(self):
        global running
        running = False

    def get_attacked(self, enemy_type, enemy_pos):
        if self.current_pos[0] - load_enemy(enemy_type)['range'] <= enemy_pos[0] <= self.current_pos[0] + load_enemy(enemy_type)['range'] and\
                self.current_pos[1] - load_enemy(enemy_type)['range'] <= enemy_pos[1] <= self.current_pos[1] + load_enemy(enemy_type)['range']:
            self.health -= load_enemy(enemy_type)['damage']

    def get_button(self, unicod):
        if unicod == 's':
            if self.current_pos[1] != 14:
                self.current_pos[1] += 1
                current_pos[1] += 1
        elif unicod == 'w':
            if self.current_pos[1] != 0:
                self.current_pos[1] -= 1
                current_pos[1] -= 1
        elif unicod == 'a':
            if self.current_pos[0] != 0:
                self.current_pos[0] -= 1
                current_pos[0] -= 1
        elif unicod == 'd':
            if self.current_pos[0] != 14:
                self.current_pos[0] += 1
                current_pos[0] += 1
        elif unicod == ' ':
            if self.board[current_pos[0]][current_pos[1]] == '1':
                self.board[current_pos[0]][current_pos[1]] = random.choice(all_loot)
            elif self.board[current_pos[0]][current_pos[1]] == 'exit':
                print(current_pos)
                self.new_level()
            elif self.board[current_pos[0]][current_pos[1]] != '0':
                self.current_loot.append(self.board[current_pos[0]][current_pos[1]])
                print(self.current_loot)
                self.board[current_pos[0]][current_pos[1]] = '0'


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
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
            if event.type == pygame.KEYDOWN:
                board.get_button(event.unicode)
        if game_started:
            screen.fill((0, 0, 0))
            board.render(screen)
        pygame.display.flip()
    pygame.display.flip()
