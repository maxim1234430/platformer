import pygame as pg
class moving_object():
    def __init__(self):

        self.speed = 1
        self.y = 0
        self.x = 0
        self.direction = 1
        self.rect = pg.Rect((self.x,self.y))
    def moved_object(self):
        if self.direction == 1:
            self.rect.y += self.speed

        elif self.direction == -1:
            self.rect.y -= self.speed











