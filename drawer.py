import pygame


def classes(screen):
    pygame.draw.rect(screen, 'blue', (250, 125, 500, 750), 0)
    font = pygame.font.Font(None, 50)
    text = font.render('Выберите класс героя', True, (255, 255, 255))
    screen.blit(text, (300, 125))
    pygame.draw.rect(screen, 'green', (300, 200, 400, 100), 0)
    pygame.draw.rect(screen, 'green', (300, 350, 400, 100), 0)
    pygame.draw.rect(screen, 'green', (300, 500, 400, 100), 0)
    pygame.draw.rect(screen, 'green', (300, 650, 400, 100), 0)
    text = font.render('Воин', True, (0, 0, 0))
    screen.blit(text, (300, 200))
    text = font.render('Охотница', True, (0, 0, 0))
    screen.blit(text, (300, 350))
    text = font.render('Вор', True, (0, 0, 0))
    screen.blit(text, (300, 500))
    text = font.render('Дриадна', True, (0, 0, 0))
    screen.blit(text, (300, 650))


def saves(screen):
    pygame.draw.rect(screen, 'blue', (250, 125, 500, 750), 0)
    font = pygame.font.Font(None, 50)
    text = font.render('Выберите номер сохранения', True, (255, 255, 255))
    screen.blit(text, (250, 125))
    pygame.draw.rect(screen, 'green', (300, 200, 400, 100), 0)
    pygame.draw.rect(screen, 'green', (300, 350, 400, 100), 0)
    pygame.draw.rect(screen, 'green', (300, 500, 400, 100), 0)
    pygame.draw.rect(screen, 'green', (300, 650, 400, 100), 0)
    text = font.render('1', True, (0, 0, 0))
    screen.blit(text, (300, 200))
    text = font.render('2', True, (0, 0, 0))
    screen.blit(text, (300, 350))
    text = font.render('3', True, (0, 0, 0))
    screen.blit(text, (300, 500))
    text = font.render('4', True, (0, 0, 0))
    screen.blit(text, (300, 650))