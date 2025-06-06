import pygame as pg  #импортивали библиотеку pygame как pg
import pytmx
from map import Tiled_map
from main_character import Player
from traps import Moving_object
from screen_resise import Camera


pg.init()     #инициализировали библиотеку pygame
screen_width = 1600 #сохранили длину экрана в отдельную переменную
screen_height = 320 #сохранили высоту экрана в отдельную переменную

class Game():   #создали класс Game
    def __init__(self): #функция конструктора класса
        self.screen=pg.display.set_mode((screen_width,screen_height)) #сохранили экран как параметр класса с шириной и высотой
        pg.display.set_caption("Платформер")   #создаём заголовок экрана
        self.clock=pg.time.Clock()     #создаём переменную для отслеживания FPS
        self.running=False  #создаём параметр отвечающий за запуск и выключение программы
        self.player1 = Player(screen_width, screen_height)
        self.map1 = Tiled_map("new_map/map.tmx")
        self.map1.find_spisoks()
        self.moving_tiles , self.tile_image,self.moving_tiles2 , self.tile_image2 = self.map1.load_moving_tiles()
        print(self.moving_tiles,self.tile_image )
        self.molot = Moving_object(self.moving_tiles,self.tile_image , 100 , 1)
        self.platforma = Moving_object(self.moving_tiles2,self.tile_image2, 40, 2)
        self.camera = Camera(self.map1.width ,self.map1.height ,screen_width ,screen_height )


















    def event(self):   #создаём метод для работы с событиями
        for event in pg.event.get():  #получаем каждое событие





            if event.type == pg.QUIT :  #если мы получили событие выхода из программы
                self.running = False     #заканчиваем цикл while

    def update(self):
        keys = pg.key.get_pressed()

        self.map1.collisition(self.player1.rect, self.screen)
        self.molot.update()
        self.platforma.update()
        self.player1.move(keys,self.map1.is_on_floor )
        self.camera.player_center(self.player1.rect)    # вычесляем местоположение игрока чтобы он был в центре экрана

        self.player1.animation_r()
        self.player1.animation_l()


    def draw(self):   #создаём метод для отрисовки экрана
        self.screen.fill((135,206,250))      #закрашиваем экран светоголубым цветом

        for layer in self.map1.tmx_data.visible_layers: # с помощью цикла for проходимся по карте
            if hasattr(layer, "data") :   #если это слой тайлов
                for x, y, gid in layer:    #получаем из тайла его координаты и номер по которому будем отрисововать
                    tile = self.map1.tmx_data.get_tile_image_by_gid(gid) #сохраняем тайл в переменную указывая его айди
                    if tile:   #если мы сохранили тайл
                        orig_x = x * self.map1.tmx_data.tilewidth
                        orig_y = y * self.map1.tmx_data.tileheight
                        new_x,new_y = self.camera.new_tile_rect(orig_x,orig_y)


                        new_size = tile.width * self.camera.zoom
                        big_tile = pg.transform.scale(tile,(new_size,new_size))
                        self.screen.blit(big_tile,(new_x,new_y) )

        width, height = self.player1.image.get_size()
        new_size = (int(width * self.camera.zoom), int(height * self.camera.zoom))
        new_image = pg.transform.scale(self.player1.image, new_size)

        #self.map1.tiled_draw(self.screen)
        self.screen.blit(new_image ,(self.camera.new_player_rect(self.player1.rect ) ))


        pg.display.flip()   #обновляем экран



    def run(self):    #метод основного игрового цикла
        self.running=True  #изменяем переменную для отслеживания состояния игры
        while self.running:  #пока running==True основной цикл работает
            self.event()
            self.update()      #используем основные методы
            self.draw()

            self.clock.tick(120)



        pg.quit()     #если программа закрыта то условия while не проходит и мы завершаем работу модуля pygame
        quit()  #выходим из программы



if __name__=="__main__":    #проверяем что программа запущена из основного скрипта
    game=Game()         #создаём обьект класса
    game.run()          #используем метод класса