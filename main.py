import pygame as pg  #импортивали библиотеку pygame как pg

from map import Tiled_map
from main_character import Player
from traps import Moving_object


pg.init()     #инициализировали библиотеку pygame
screen_width= 1024 #сохранили длину экрана в отдельную переменную
screen_height= 800 #сохранили высоту экрана в отдельную переменную

class Game():   #создали класс Game
    def __init__(self): #функция конструктора класса
        self.screen=pg.display.set_mode((screen_width,screen_height)) #сохранили экран как параметр класса с шириной и высотой
        pg.display.set_caption("Платформер")   #создаём заголовок экрана
        self.clock=pg.time.Clock()     #создаём переменную для отслеживания FPS
        self.running=False  #создаём параметр отвечающий за запуск и выключение программы
        self.player1 = Player(screen_width, screen_height)
        self.map1 = Tiled_map("map/map_platform.tmx")
        self.map1.find_spisoks()



    def event(self):   #создаём метод для работы с событиями
        for event in pg.event.get():  #получаем каждое событие





            if event.type == pg.QUIT :  #если мы получили событие выхода из программы
                self.running = False     #заканчиваем цикл while

    def update(self):
        keys = pg.key.get_pressed()
        self.map1.collisition(self.player1.rect, self.screen)
        self.player1.move(keys,self.map1.is_on_floor )

        # Обновление движущихся объектов
        for moving_object in self.map1.spisok_moving_block:
            moving_object.moved_object()

        self.player1.animation_r()
        self.player1.animation_l()


    def draw(self):   #создаём метод для отрисовки экрана
        self.screen.fill((135,206,250))      #закрашиваем экран светоголубым цветом
        self.map1.draw_map(self.screen)
        #self.map1.tiled_draw(self.screen)
        self.screen.blit(self.player1.image,(self.player1.rect))
        pg.display.flip()   #обновляем экран



    def run(self):    #метод основного игрового цикла
        self.running=True  #изменяем переменную для отслеживания состояния игры
        while self.running:  #пока running==True основной цикл работает
            self.event()
            self.update()      #используем основные методы
            self.draw()

            self.clock.tick()



        pg.quit()     #если программа закрыта то условия while не проходит и мы завершаем работу модуля pygame
        quit()  #выходим из программы



if __name__=="__main__":    #проверяем что программа запущена из основного скрипта
    game=Game()         #создаём обьект класса
    game.run()          #используем метод класса