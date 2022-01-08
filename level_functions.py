import os
import sys

import pygame


def load_image(name, color_key=None):  # функция для получения изображения
    fullname = os.path.join('data', name)
    # проверка
    if not os.path.isfile(fullname):
        print(f"Файл не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if color_key is not None:  # еще одна проверка
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


tile_sprites = {
    'wall': load_image('idkthenameofthis.png'),
    'empty_tile': load_image('idkthenameofthis2.png')
}
# подгрузка пикч к тайлам, сюда можно добавить остальные
tile_width = tile_height = 10  # размеры тайла


def load_level(filename):  # функция для чтения уровня в виде txt файла
    filename = os.path.join("data", filename)
    # путь до файла с уровнем без перевода строки
    with open(filename) as map_file:
        level_map = [line.strip() for line in map_file]
    # читаем уровень

    max_width = max(map(len, level_map))
    # достраиваем уровень если он неполный (а я ленивая жопа)
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):  # класс для тайлов
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)  # группы тайлов, я их пока не сделал
        self.image = tile_sprites[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
    # сюда можно дописывать тайлы
    # игрока сюда тоже можно присобачить
    # возврат размера поля в клетках
    return x, y
