import pygame as pg
import pygame.image


class Player(pg.sprite.Sprite ):  #создаём класс для игрока передаём который наследует класс Sprite
    def __init__(self,map_width,map_height,):#создаём конструктор класса и передаём туда размеры карты,картинку персонажа
        super(Player,self ).__init__()  #класс Player наследует методы класса Sprite

        #инициализация переменных для анимации
        self.frame_index_l = 0  # текущий кадр
        self.frame_index_r = 0
        self.animation_speed = 10  # скорость смены анимации
        self.frame_count = 0  # счётчик кадров

        # загрузка изображений для анимации
        self.frames_r=[pygame.transform.scale(pygame.image.load("images/state1.png"),(32,64)),
            pygame.transform.scale(pygame.image.load("images/state2.png"),(32,64)),
            pygame.transform.scale(pygame.image.load("images/state3.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state4.png"), (32, 64)),

        ]
        self.frames_l= [pygame.transform.scale(pygame.image.load("images/state5.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state6.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state7.png"), (32, 64)),
            pygame.transform.scale(pygame.image.load("images/state8.png"), (32, 64))]


        #начальное изображение
        self.image=self.frames_r[self.frame_index_r]
        self.rect= self.image.get_rect()  #сохраняем в переменную параметр содержащий картинку
        self.rect.x=50
        self.rect.y=400




        #общие парраметры объекта#гравитация
        self.is_jumping=False#состояние прыжка
        self.is_running_l=False
        self.is_running_r=False
        self.map_width=map_width#размеры карты чтобы персонаж не мог выйти за них
        self.map_height=map_height

    def move(self, keys, gravity):

        if self.rect.bottom >=self.map_height:    #self.bottom-нижняя точка обьекта
            self.rect.bottom =self.map_height
        self.rect.y=self.rect.y+gravity
        # Если нажата клавиша A, двигаем игрока влево
        if keys[pg.K_a]:
            new_x = self.rect.x - 1
            self.is_running_l=True
            if new_x >= 0 and new_x <=self.map_width:
                self.rect.x = new_x


        else:
            self.is_running_l=False





        if keys[pg.K_d]:
            new_x =self.rect.x+1
            self.is_running_r=True
            if new_x >= 0 and new_x<=self.map_width:
                self.rect.x = new_x


        else :
            self.is_running_r=False




        if keys[pg.K_w]:
            new_y = self.rect.y - 1
            if new_y >= 0 and new_y <= self.map_height:
                self.rect.y = new_y

        elif keys[pg.K_s]:
            new_y = self.rect.y + 1
            if new_y >= 0 and new_y <= self.map_height:
                self.rect.y = new_y
        self.frame_count+=1

    def animation_r(self):
        if self.is_running_r:
            if self.frame_count%self.animation_speed==0:
                self.frame_count=0
                self.frame_index_r+=1
            self.image=self.frames_r[self.frame_index_r]
            if self.frame_index_r>=len(self.frames_r):
                self.frame_index=0
    def animation_l(self):
        if self.is_running_l:
            if self.frame_count%self.animation_speed==0:
                self.frame_count=0
                self.frame_index_l+=1
            self.image=self.frames_l[self.frame_index_l]
            print("анимация сменилась")
            if self.frame_index_l==3:
                self.frame_index_l=0


















