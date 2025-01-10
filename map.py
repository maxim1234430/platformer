from pytmx import load_pygame
class Tiled_map():
    def __init__(self,map_file):
        self.tmx_data=load_pygame(map_file )
        self.widhth=self.tmx_data.width*self.tmx_data.tilewidth
        self.heigth=self.tmx_data.height*self.tmx_data.tileheight
