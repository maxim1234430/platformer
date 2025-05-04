import pygame as pg
class Camera():
    def __init__(self,map_width,map_height,screen_width,screen_height):
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
        self.zoom = 4


    # вычисляем центр игрока
    def player_center(self, target):
        center_x = int(target.centerx)
        center_y = int(target.centery)


        self.offset_x = -(center_x * self.zoom) + self.screen_width//2
        self.offset_y = -(center_y * self.zoom) + self.screen_height//2




