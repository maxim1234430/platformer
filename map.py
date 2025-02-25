import pytmx  # импрортировали метод load_pygame из библиотеки pytmx
import pygame as pg
class Tiled_map ():  #новый класс tiled_map
#ОРТОГАНАЛЬНАЯ ориентация карты (карта из квадратов)
    def __init__(self, map_file): #передаём в конструктор класса файл с картой
        self.tmx_data = pytmx.load_pygame(map_file)   #загружаем карту в параметр
        self.width = self.tmx_data.width*self.tmx_data.tilewidth #сохраняем ширину в пикселях
        self.height = self.tmx_data.height*self.tmx_data.tileheight #сохраняем высоту в пикселях
    def draw_map(self,surface): #метод отрисовки карты surface-поверхность на которой отрисовываем
        for layer in self.tmx_data.visible_layers: # с помощью цикла for проходимся по карте
            if hasattr(layer, "data"):   #если это слой тайлов
                for x, y, gid in layer:    #получаем из тайла его координаты и номер по которому будем отрисововать
                    tile = self.tmx_data.get_tile_image_by_gid(gid) #сохраняем тайл в переменную указывая его номер
                    if tile:   #если мы сохранили тайл
                        surface.blit(tile, (x*self.tmx_data.tilewidth, y*self.tmx_data.tileheight))#отрисовывем на поверхности тайл с координата


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
            if isinstance(layer,pytmx.TiledObjectGroup):
                if layer.name == "move_block":
                    # Для примера оставим телепорт. Пока только выводит print
                    for obj in layer:
                        rect1 = pg.Rect(obj.x, obj.y, obj.width, obj.height)
                        if block.colliderect(rect1):
                            print("teleport сработал!",rect1)
                            print(block)
            layer_index += 1









