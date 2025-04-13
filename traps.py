import pygame as pg
class Moving_object():
    def __init__(self , rects , image, max_moved , speed):
        self.direction = 1
        self.rects = rects
        self.image = image
        self.max_moved = max_moved
        self.speed = speed
        self.moved_distance = 0.0
        self.fractional_movement = 0.0

    def update(self):
        self.fractional_movement = self.speed * self.direction
        move_step = int(self.fractional_movement)

        if move_step!=0:
            for rect in self.rects:
                rect.y += move_step
            self.fractional_movement -= move_step
        self.moved_distance += abs(move_step)

        if self.moved_distance >= self.max_moved:
            self.direction *= -1
            self.moved_distance = 0.0

    def draw(self,screen):
        for i in range(len(self.rects )):
            screen.blit(self.image[i],(self.rects[i].x,self.rects[i].y))




