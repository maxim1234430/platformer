import pygame as pg
import pygame.image


class Player(pg.sprite.Sprite ):  #создаём класс для игрока передаём который наследует класс Sprite
    def __init__(self,map_width,map_height):#создаём конструктор класса и передаём туда размеры карты,картинку персонажа
        super(Player,self ).__init__()  #класс Player наследует методы класса Sprite
                           #alpha каналы это прозрачные пиксели заполняющие фон картинки

        self.image = pg.image.load("images/state1.png"
                                   ).convert_alpha()  # сохраняем картинку в image и настраиваем alpha каналы
        self.image = pg.transform.scale(self.image, (32, 64))
        self.frame_index=0      #текущий кадр
        self.animation_speed=10  #скорость смены анимации
        self.frame_count=0      #счётчик кадров

        self.frames=[pygame.transform.scale(pygame.image.load("images/state1.png"),(32,64)),
            pygame.transform.scale(pygame.image.load("images/state2.png"),(32,64)),
            pygame.transform.scale(pygame.image.load("images/state3.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state4.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state5.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state6.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state7.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state8.png"), (32, 64))

        ]
        if self.frame_count%self.animation_speed==0:
            self.frame_count=0
            self.frame_index+=1
            if self.frame_index>=7:
                self.frame_index=0




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

        if self.rect.bottom >=self.map_height:    #self.bottom-нижняя точка обьекта
            self.rect.bottom =self.map_height
        #self.rect.y=self.rect.y+self.gravity
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
        self.frame_count+=1











