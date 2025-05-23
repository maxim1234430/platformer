import pygame as pg
import pygame.image


class Player(pg.sprite.Sprite ):  #создаём класс для игрока передаём который наследует класс Sprite
    def __init__(self,map_width,map_height,):#создаём конструктор класса и передаём туда размеры карты,картинку персонажа
        super(Player,self ).__init__()  #класс Player наследует методы класса Sprite

        #инициализация переменных для анимации
        self.frame_index_l = 0  # текущий кадр
        self.frame_index_r = 0
        self.animation_speed = 10  # скорость смены анимации
        self.frame_count_r = 0  # счётчик кадров
        self.frame_count_l = 0

        # загрузка изображений для анимации
        self.frames_r=[pygame.transform.scale(pygame.image.load("images/state1.png"),(16,32)),
            pygame.transform.scale(pygame.image.load("images/state2.png"),(16,32)),
            pygame.transform.scale(pygame.image.load("images/state3.png"), (16,32)),
            pygame.transform.scale(pygame.image.load("images/state4.png"), (16,32)),

        ]
        self.frames_l= [pygame.transform.scale(pygame.image.load("images/state5.png"), (16,32)),
            pygame.transform.scale(pygame.image.load("images/state6.png"), (16,32)),
            pygame.transform.scale(pygame.image.load("images/state7.png"), (16,32)),
            pygame.transform.scale(pygame.image.load("images/state8.png"), (16,32))]


        #начальное изображение
        self.image=self.frames_r[self.frame_index_r]
        self.rect = self.image.get_rect()  #сохраняем в переменную параметр содержащий картинку
        self.rect.x = 1000
        self.rect.y = 200
        print(self.rect.centerx)




        #общие парраметры объекта#гравитация
        self.is_jumping = False#состояние прыжка
        self.is_running_l = False#касание левой стены
        self.is_running_r = False#касание правой стены
        self.map_width = map_width#размеры карты чтобы персонаж не мог выйти за них
        self.map_height = map_height
        self.jump_speed = -3#скорость с которой игрок прыгает
        self.vert_speed = 0#скорость движения игрока по вертикали состоит из гравитации и прыжка
        self.high_jump = 10#максимальная высота на которую мы можем прыгнуть

    #метод для движения игрока
    def move(self, keys, is_on_floor):
        #проверка чтобы игрок оставался на полу
        if self.rect.bottom >=self.map_height:#self.bottom-нижняя точка обьекта,если игрок на полу или ниже
            self.rect.bottom =self.map_height#то игрока отбрасывет до верхней точки пола
            self.is_jumping = False#состояние прыжка меняется
            self.vert_speed = 0#вертикальная скорость ноль потому что мы на полу
        #условие для прыжка
        if is_on_floor:
            self.is_jumping = False#состояние прыжка меняется
            self.vert_speed = 0#вертикальная скорость ноль потому что мы на полу
            #можем прыгать если только находимся на полу
            if keys[pg.K_w] or keys [pg.K_SPACE ] and not self.is_jumping:#если нажата кнопка прыжка и мы ещё не прыгаем то
                self.vert_speed = self.jump_speed#вертикальная скорость равна скорости прыжка
                self.is_jumping = True#состояние прыжка True

        else:#если мы не на полу то на нас действует гравитация
            self.vert_speed += 0.1#вертикальная скорость увеличивается на один невелируя прыжок


        #на перрсонажа действует гравитация
        self.rect.y=self.rect.y+self.vert_speed

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
            if new_x >= 0 and new_x<self.map_width-30:
                self.rect.x = new_x


        else :
            self.is_running_r=False








    def animation_r(self):
        if self.is_running_r:
            if self.frame_count_r % self.animation_speed == 0:
                self.frame_count_r = 0
                self.frame_index_r += 1
            if self.frame_index_r >= len(self.frames_r):
                self.frame_index_r = 0
            self.image=self.frames_r[self.frame_index_r]
        elif not self.is_running_r and self.image in self.frames_r:
            self.frame_count_r = 0
            self.frame_index_r = 0
            self.image = self.frames_r[0]

    def animation_l(self):
        if self.is_running_l:
            if self.frame_count_l%self.animation_speed==0:
                self.frame_count_l=0
                self.frame_index_l+=1
            self.image=self.frames_l[self.frame_index_l]
            if self.frame_index_l==3:
                self.frame_index_l=0
        elif not self.is_running_l and self.image in self.frames_l :
            self.frame_count_l = 0
            self.frame_index_l = 0
            self.image = self.frames_l[0]