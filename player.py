import pygame
from database_helper import load_save, save_game, delete
from drawer import classes, saves

game_started = False
save_id = 0
current_pos = [0, 0, 0]


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
        global game_started
        classes(screen)
        x, y = mouse_pos[0], mouse_pos[1]
        if 300 <= x <= 700:
            if 200 <= y <= 300:
                self.hero_class = 'Воин'
            elif 350 <= y <= 450:
                self.hero_class = 'Охотница'
            elif 500 <= y <= 600:
                self.hero_class = 'Вор'
            elif 650 <= y <= 750:
                self.hero_class = 'Дриадна'
        print(self.hero_class)
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
        global save_id, current_pos
        self.save_id = save_id
        self.board = ['0' * width for _ in range(height)]
        self.current_pos = current_pos
        self.floor = ';'.join([' '.join((self.board[i]) for i in range(height))])
        self.width = width
        self.height = height
        self.left = 100
        self.top = 100
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen: pygame.Surface):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                x, y = column * self.cell_size + self.left, row * self.cell_size + self.top
                pygame.draw.rect(screen, 'white', (x, y, self.cell_size, self.cell_size), 1)
        pygame.draw.rect(screen, 'red', (900, 10, 75, 20))
        font = pygame.font.Font(None, 20)
        text = font.render('Выход', True, (255, 254, 254))
        screen.blit(text, (910, 10))

    def get_cell(self, mouse_pos):
        if 900 <= mouse_pos[0] <= 975 and 10 <= mouse_pos[1] <= 30:
            print('ok')
            save_game(self.save_id, )
        else:
            x, y = (mouse_pos[0] - self.top) // self.cell_size, (mouse_pos[1] - self.left) // self.cell_size
            if 0 <= x <= self.width and 0 <= y <= self.height:
                print(tuple([x, y]))
                return x, y
            else:
                print('None')
                return None

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


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
                # else:
                #     if not game_started:

        if game_started:
            screen.fill((0, 0, 0))
            board.render(screen)
        pygame.display.flip()
    pygame.display.flip()
