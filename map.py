from pytmx import load_pygame  # импрортировали метод load_pygame из библиотеки pytmx
class Tiled_map ():
    def __init__(self, map_file):
        self.tmx_data = load_pygame(map_file)
        self.width = self.tmx_data.width*self.tmx_data.tilewidth
        self.height = self.tmx_data.height*self.tmx_data.tileheight
    def draw_map(self,surface):
        for layer in self.tmx_data.visible_layers: # с помощью цикла for проходимся по карте
            if hasattr(layer,"data"):
                for x,y,gid in layer:    #получаем из тайла его координаты и номер по которому будем отрисововать
                    tile=self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile,
                                     x*self.tmx_data.tilewidth ,y*self.tmx_data.tileheight )







