import pygame
from level_functions import load_image
from database_helper import load_tool, load_hero


def classes(screen):
    screen.fill('black')
    all_classes = ['Воин', 'Охотница', 'Вор', 'Дриадна']
    pygame.draw.rect(screen, 'blue', (250, 125, 500, 750), 0)
    font = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 20)
    text = font.render('Выберите класс героя', True, (255, 255, 255))
    screen.blit(text, (300, 125))
    for i in range(len(all_classes)):
        pygame.draw.rect(screen, 'white', (300, 200 + i * 150, 400, 100), 0)
        text = font.render(all_classes[i], True, (0, 0, 0))
        screen.blit(text, (300, 200 + i * 150))
        img = load_image(load_hero(all_classes[i])['pic'], color_key=-1)
        img = pygame.transform.scale(img, (75, 100))
        screen.blit(img, (625, 200 + i * 150))
        loot = load_hero(all_classes[i])['start_loot']
        loot_desc = '\n'.join(load_tool(loot)['desc'].split('&'))
        text2 = f'Начинает с "{loot}"'
        text2 = font2.render(text2, True, 'red')
        screen.blit(text2, (300, 275 + i * 150))


def saves(screen):
    pygame.draw.rect(screen, 'blue', (250, 125, 500, 750), 0)
    font = pygame.font.Font(None, 50)
    text = font.render('Выберите номер сохранения', True, (255, 255, 255))
    screen.blit(text, (250, 125))
    pygame.draw.rect(screen, 'white', (300, 200, 400, 100), 0)
    pygame.draw.rect(screen, 'white', (300, 350, 400, 100), 0)
    pygame.draw.rect(screen, 'white', (300, 500, 400, 100), 0)
    pygame.draw.rect(screen, 'white', (300, 650, 400, 100), 0)
    text = font.render('1', True, (0, 0, 0))
    screen.blit(text, (300, 200))
    text = font.render('2', True, (0, 0, 0))
    screen.blit(text, (300, 350))
    text = font.render('3', True, (0, 0, 0))
    screen.blit(text, (300, 500))
    text = font.render('4', True, (0, 0, 0))
    screen.blit(text, (300, 650))


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


def bottom_text(screen, text):
    font = pygame.font.Font(None, 25)
    text = font.render(text, True, 'white')
    screen.blit(text, (0, 800))


def up_text(screen, text):
    font = pygame.font.Font(None, 15)
    text = font.render(text, True, 'white')
    screen.blit(text, (25, 50))


def up_text2(screen, text):
    font = pygame.font.Font(None, 15)
    text = font.render(text, True, 'white')
    screen.blit(text, (25, 75))