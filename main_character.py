import pygame as pg
class Player(pg.sprite.Sprite ):  #создаём класс для игрока передаём который наследует класс Sprite
    def __init__(self,map_width,map_height,image_path=None):#создаём конструктор класса и передаём туда размеры карты,картинку персонажа
        super(Player,self ).__init__()  #класс Player наследует методы класса Sprite


        if image_path:                                           #alpha каналы это прозрачные пиксели заполняющие фон картинки
            self.image=pg.image.load(image_path ).convert_alpha()#сохраняем картинку в image и настраиваем alpha каналы
            self.image=pg.transform.scale(self.image,(50,50))
        else:#если картинки нет то сохраняем в картинку квадрат 50 на 50 устанавливаем карсный цвет
            self.image=pg.Surface((50,50))
            self.image.fill("red")

        self.rect= self.image.get_rect()  #сохраняем в переменную параметр содержащий картинку
        print(self.rect)

        self.velocity_x=0#параметр скорость по x
        self.velocity_y=0#скорость по Y
        self.gravity=0#гравитация
        self.is_jumping=False#состояние прыжка
        self.is_running_l=False
        self.is_running_r=False
        self.map_width=map_width#размеры карты чтобы персонаж не мог выйти за них
        self.map_height=map_height

    def get_keys(self):  #создаём метод отвечающий за получение нажатий кнопок и действий
        keys = pg.key.get_pressed()#получаем кнопки которые были нажаты
        if keys[pg.K_LEFT ]:#если нажата стрелка влево то задаём скорость -10
            self.is_running_l=True
        else:
            self.is_running_l=False

        if keys[pg.K_RIGHT  ]:#если нажата стрелка вправо задаём скорость 10
            self.is_running_r=True
        else:
            self.is_running_r=False

        if self.is_running_r:
            self.velocity_x=5
        else:
            self.velocity_x=0
        new_x=self.rect.x+self.velocity_x  #сохраняем новое положение персонажа отнасительно его скорости
        if 0<new_x<self.map_width :#если он не выходит за размеры карты
            self.rect.x=new_x#изменяем положение персонажа










