import pygame as pg

class Camera():
    def __init__(self, map_width, map_height, screen_width, screen_height):
        # Начальные координаты смещения камеры
        self.offset_x = 0
        self.offset_y = 0

        # Коэффициент плавности движения камеры
        self.smoothness = 0.2

        # Размеры карты и  экрана
        self.map_width = map_width
        self.map_height = map_height
        self.screen_width = screen_width
        self.screen_height = screen_height

        # зум
        self.zoom = 3

    # вычисляем центр игрока
    def player_center(self, target):
        # сохраняем центр игрока в переменную
        center_x = int(target.centerx)
        center_y = int(target.centery)

        # вычисляем следующую позицию игрока
        next_position_x = -(center_x * self.zoom) + self.screen_width // 2
        next_position_y = -(center_y * self.zoom) + self.screen_height // 2

        # плавно перемещаем камеру к позиции
        self.offset_x += (next_position_x - self.offset_x) * self.smoothness
        self.offset_y += (next_position_y - self.offset_y) * self.smoothness

        # округляем до целого значения
        self.offset_x = int(self.offset_x)
        self.offset_y = int(self.offset_y)

        # не допускаем выход камеры за карту
        if self.offset_x > 0:
            self.offset_x = 0
        if self.offset_y > 0:
            self.offset_y = 0

    # метод отвечает за увеличенныq объект на экране
    def new_player_rect(self, rect):

        zoom_width = int(rect.width * self.zoom)
        zoom_height = int(rect.height * self.zoom)

        zoom_x = int(rect.x * self.zoom + self.offset_x)
        zoom_y = int(rect.y * self.zoom + self.offset_y)

        return (pg.Rect(zoom_x, zoom_y, zoom_width, zoom_height))


    def new_tile_rect(self,x,y):


        zoom_x = int(x * self.zoom + self.offset_x)
        zoom_y = int(y * self.zoom + self.offset_y)

        return (zoom_x, zoom_y)


