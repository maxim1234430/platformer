from pytmx import load_pygame  # импрортировали метод load_pygame из библиотеки pytmx
class Tiled_map ():  #новый класс tiled_map
    def __init__(self, map_file): #передаём в конструктор класса файл с картой
        self.tmx_data = load_pygame(map_file)   #загружаем карту в параметр
        self.width = self.tmx_data.width*self.tmx_data.tilewidth #сохраняем ширину в пикселях
        self.height = self.tmx_data.height*self.tmx_data.tileheight #сохраняем высоту в пикселях
    def draw_map(self,surface): #метод отрисовки карты surface-поверхность на которой отрисовываем
        for layer in self.tmx_data.visible_layers: # с помощью цикла for проходимся по карте
            if hasattr(layer, "data"):   #если это тайл
                for x, y, gid in layer:    #получаем из тайла его координаты и номер по которому будем отрисововать
                    tile = self.tmx_data.get_tile_image_by_gid(gid) #сохраняем тайл в переменную указывая его номер
                    if tile:   #если мы сохранили тайл
                        surface.blit(tile, (x*self.tmx_data.tilewidth, y*self.tmx_data.tileheight))#отрисовывем на поверхности тайл с координатами







