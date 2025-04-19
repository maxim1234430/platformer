import pytmx  # импрортировали метод load_pygame из библиотеки pytmx
import pygame as pg
class Tiled_map ():  #новый класс tiled_map
#ОРТОГАНАЛЬНАЯ ориентация карты (карта из квадратов)
    def __init__(self, map_file): #передаём в конструктор класса файл с картой
        self.tmx_data = pytmx.load_pygame(map_file)   #загружаем карту в параметр
        self.width = self.tmx_data.width*self.tmx_data.tilewidth #сохраняем ширину в пикселях
        self.height = self.tmx_data.height*self.tmx_data.tileheight #сохраняем высоту в пикселях
        self.spisok_floor_block = []
        self.spisok_seiling_block = []
        self.spisok_r_block = []
        self.spisok_l_block = []
        self.spisok_moving_block = []
        self.spisok_k=[]





        self.st=True
        self.wall_collistion=False

    def draw_map(self,surface): #метод отрисовки карты surface-поверхность на которой отрисовываем
        for layer in self.tmx_data.visible_layers: # с помощью цикла for проходимся по карте
            if hasattr(layer, "data") :   #если это слой тайлов
                for x, y, gid in layer:    #получаем из тайла его координаты и номер по которому будем отрисововать
                    tile = self.tmx_data.get_tile_image_by_gid(gid) #сохраняем тайл в переменную указывая его айди
                    if tile:   #если мы сохранили тайл
                        surface.blit(tile, (x*self.tmx_data.tilewidth, y*self.tmx_data.tileheight))#отрисовывем на поверхности тайл с координата




    def find_spisoks(self):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "floor":
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)

                        self.spisok_floor_block.append(rect1)
                if layer.name == "ceiling":
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.spisok_seiling_block.append(rect1)
                if layer.name == "l_wall":
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)

                        self.spisok_l_block.append(rect1)
                if layer.name == "r_wall":
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.spisok_r_block.append(rect1)




        print(str(self.spisok_floor_block) + " пол")
        print(str(self.spisok_r_block) + " правые стены")
        print(str(self.spisok_l_block) + " левые стены")


    def collisition(self,block,surface):


        self.col_stolk = 0

        self.is_on_floor = False

        self.is_on_left_wall = False

        self.is_on_right_wall = False

        for rect1 in self.spisok_floor_block :


            if block.colliderect(rect1):
                self.col_stolk += 1

                if abs(block.bottom - rect1.top) < 10:
                    block.bottom = rect1.top
                    self.is_on_floor = True

        for rect1 in self.spisok_seiling_block  :


            if block.colliderect(rect1):
                self.col_stolk += 1

                if abs(block.top - rect1.bottom) < 10:
                    block.top = rect1.bottom




        for rect1 in self.spisok_l_block  :

            if block.colliderect(rect1):
                self.col_stolk+=1

                if abs(block.right - rect1.left)<10:

                    block.right=rect1.left
                    self.is_on_left_wall  =True


        for rect1 in self.spisok_r_block  :

            if block.colliderect(rect1):
                self.col_stolk+=1

                if abs(block.left - rect1.right)<10:

                    block.left=rect1.right
                    self.is_on_right_wall  =True







