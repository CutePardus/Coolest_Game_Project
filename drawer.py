import pygame
from level_functions import load_image
from database_helper import load_tool


def classes(screen):
    pygame.draw.rect(screen, 'blue', (250, 125, 500, 750), 0)
    font = pygame.font.Font(None, 50)
    text = font.render('Выберите класс героя', True, (255, 255, 255))
    screen.blit(text, (300, 125))
    pygame.draw.rect(screen, 'white', (300, 200, 400, 100), 0)
    pygame.draw.rect(screen, 'white', (300, 350, 400, 100), 0)
    pygame.draw.rect(screen, 'white', (300, 500, 400, 100), 0)
    pygame.draw.rect(screen, 'white', (300, 650, 400, 100), 0)
    text = font.render('Воин', True, (0, 0, 0))
    screen.blit(text, (300, 200))
    w_img = load_image('warior.png', color_key=-1)
    w_img = pygame.transform.scale(w_img, (75, 100))
    screen.blit(w_img, (625, 200))
    text = font.render('Охотница', True, (0, 0, 0))
    screen.blit(text, (300, 350))
    h_img = load_image('hunter.png', color_key=-1)
    h_img = pygame.transform.scale(h_img, (75, 100))
    screen.blit(h_img, (625, 350))
    text = font.render('Вор', True, (0, 0, 0))
    screen.blit(text, (300, 500))
    t_img = load_image('thief.png', color_key=-1)
    t_img = pygame.transform.scale(t_img, (75, 100))
    screen.blit(t_img, (625, 500))
    text = font.render('Дриадна', True, (0, 0, 0))
    screen.blit(text, (300, 650))
    d_img = load_image('driade.png', color_key=-1)
    d_img = pygame.transform.scale(d_img, (75, 100))
    screen.blit(d_img, (625, 650))


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
