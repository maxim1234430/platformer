import pytmx  # импрортировали метод load_pygame из библиотеки pytmx
import pygame as pg


class Tiled_map ():  #новый класс tiled_map
#ОРТОГАНАЛЬНАЯ ориентация карты (карта из квадратов)
    tmx_data = pytmx.load_pygame("map/map_platform.tmx")
    spisok_floor_block=[]
    spisok_l_block=[]
    spisok_floor_block=[]
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledObjectGroup):
            if layer.name == "floor":
                # Для примера оставим телепорт. Пока только выводит print
                for obj in layer:
                    rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                    spisok_floor_block.append(rect1)
            elif layer.name == "l_wall":
                # Для примера оставим телепорт. Пока только выводит print
                for obj in layer:
                    rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                    spisok_l_block.append(rect1)
            elif layer.name == "r_wall":
                # Для примера оставим телепорт. Пока только выводит print
                for obj in layer:
                    rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                    spisok_floor_block.append(rect1)
    def __init__(self, map_file): #передаём в конструктор класса файл с картой
        self.tmx_data = pytmx.load_pygame(map_file)   #загружаем карту в параметр
        self.width = self.tmx_data.width*self.tmx_data.tilewidth #сохраняем ширину в пикселях
        self.height = self.tmx_data.height*self.tmx_data.tileheight #сохраняем высоту в пикселях
        self.spisok_floor_block=[]
        self.spisok_r_block = []
        self.spisok_l_block = []

        self.st=True
        self.gravity=0
        self.col_stolk=0
        self.is_on_floor=False
        self.is_on_left_wall=False
        self.is_on_right_wall=False
        self.wall_collistion=False



    def draw_map(self,surface): #метод отрисовки карты surface-поверхность на которой отрисовываем
            for layer in self.tmx_data.visible_layers: # с помощью цикла for проходимся по карте
                if hasattr(layer, "data"):   #если это слой тайлов
                    for x, y, gid in layer:    #получаем из тайла его координаты и номер по которому будем отрисововать
                        tile = self.tmx_data.get_tile_image_by_gid(gid) #сохраняем тайл в переменную указывая его номер
                        if tile:   #если мы сохранили тайл
                            surface.blit(tile, (x*self.tmx_data.tilewidth, y*self.tmx_data.tileheight))



    def collisition(self,block,surface):
        layer_index = 0
        for layer in self.tmx_data.visible_layers:    #проходим по всем ВИДИМЫМ слоям
            if isinstance(layer,pytmx.TiledTileLayer):
                for x in range(0, 64):
                    for y in range(0, 50):
                        image = self.tmx_data .get_tile_image(x, y, layer_index)
                        if image:
                            surface.blit(image, (16 * x, 16 * y))
            # Если есть объектный слой — проверяем столкновения
            elif isinstance(layer,pytmx.TiledObjectGroup):
                if layer.name == "floor":
                    # Для примера оставим телепорт. Пока только выводит print
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.spisok_floor_block.append(rect1)


                        if block.colliderect(rect1):
                            self.col_stolk+=1
                            print("низшая"+str(block.bottom),"высшая"+str(block.top),"левая"+str(block.left),"правая"+str(block.right))

                            if abs(block.bottom - rect1.top) < 10 :
                                block.bottom=rect1.top
                if layer.name == "l_wall":
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.spisok_l_block.append(rect1)
                if layer.name == "r_wall":
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.spisok_r_block.append(rect1)


                layer_index += 1
                self.st=False
                print("список правых стен "+ str(self.spisok_r_block))
                print("список левых стен " + str(self.spisok_l_block))
                print("список полов " + str(self.spisok_floor_block))
                if self.col_stolk==0:
                    self.gravity=1
                else:
                    self.gravity=0
                self.col_stolk=0










