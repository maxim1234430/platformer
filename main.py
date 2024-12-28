import pygame
import pytmx
from pytmx.util_pygame import load_pygame

# Инициализация Pygame
pygame.init()

# Задаем параметры окна
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer with Tiled Map")
clock = pygame.time.Clock()

# Загрузка карты .tmx
tmx_file = 'map/map_platform.tmx'  # Путь к карте
tmx_data = load_pygame(tmx_file)

# Функция для отрисовки карты
def draw_map(surface, tmx_data):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):  # Проверяем, является ли слой тайловым
            for x, y, gid in layer:  # Проходим по каждой плитке слоя
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:  # Если тайл существует, отрисовываем его
                    surface.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отрисовка карты
    draw_map(screen, tmx_data)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS

pygame.quit()