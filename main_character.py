import pygame as pg
class Player(pg.sprite.Sprite ):  #создаём класс для игрока передаём который наследует класс Sprite
    def __init__(self,map_width,map_height,image_path=None):#создаём конструктор класса и передаём туда размеры карты,картинку персонажа
        super(Player,self ).__init__()  #класс Player наследует методы класса Sprite


        if image_path:                                           #alpha каналы это прозрачные пиксели заполняющие фон картинки
            self.image=pg.image.load(image_path ).convert_alpha()#сохраняем картинку в image и настраиваем alpha каналы
            self.image=pg.transform.scale(self.image,(16,16))
        else:#если картинки нет то сохраняем в картинку квадрат 50 на 50 устанавливаем карсный цвет
            self.image=pg.Surface((16,16))
            self.image.fill("red")

        self.rect= self.image.get_rect()  #сохраняем в переменную параметр содержащий картинку
        self.rect.x=50
        self.rect.y=749
        print(self.rect)

        self.speed=0#параметр скорость по x
        self.velocity_y=0#скорость по Y
        self.gravity=1#гравитация
        self.is_jumping=False#состояние прыжка
        self.is_running_l=False
        self.is_running_r=False
        self.map_width=map_width#размеры карты чтобы персонаж не мог выйти за них
        self.map_height=map_height

    def move(self, keys):
        new_y=self.rect.y+1
        if new_x
        # Если нажата клавиша A, двигаем игрока влево
        if keys[pg.K_a]:
            new_x = self.rect.x - 1
            if new_x >= 0 and new_x <=self.map_width:
                self.rect.x = new_x

        elif keys[pg.K_d]:
            new_x =self.rect.x+1
            if new_x >= 0 and new_x<=self.map_width:
                self.rect.x = new_x

        elif keys[pg.K_w]:
            new_y = self.rect.y - 1
            if new_y >= 0 and new_y <= self.map_height:
                self.rect.y = new_y

        elif keys[pg.K_s]:
            new_y = self.rect.y + 1
            if new_y >= 0 and new_y <= self.map_height:
                self.rect.y = new_y











