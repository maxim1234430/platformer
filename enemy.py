import pygame


class Enemy():
    def __init__(self,map_width,map_height):
        # инициализация переменных для анимации
        self.frame_index_l = 0  # текущий кадр
        self.frame_index_r = 0
        self.frame_index_h_r = 0
        self.frame_index_h_l = 0
        self.animation_speed = 10  # скорость смены анимации
        self.frame_count_r = 0  # счётчик кадров
        self.frame_count_l = 0
        self.frame_count_h = 0
        self.frame_count_h_l = 0

        self.image = None
        self.rect = pygame.Rect(1000,200,100,50)
