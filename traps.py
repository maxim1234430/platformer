import pygame as pg
class Moving_object():
    def __init__(self, rect,type):
        self.type = type
        self.speed = 1
        self.y = 0
        self.x = 0
        self.direction = 1
        self.min_cord=320
        self.max_cord=480
        self.rect = rect
    def moved_object(self):
        if self.rect.bottom <= self.max_cord  and self.rect.top>=self.min_cord :
            if self.direction == 1:
                self.rect.y += self.speed

            elif self.direction == -1:
                self.rect.y -= self.speed