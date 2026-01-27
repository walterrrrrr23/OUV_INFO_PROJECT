import pygame
from settings import ZOOM
TILE_SIZE = 64      
TILE_SIZE *= ZOOM



def load_tiles(path):
    tilesheet = pygame.image.load(path).convert_alpha()
    
    tile_width = tilesheet.get_width() // 2
    tile_height = tilesheet.get_height()
    
    tile1 = pygame.transform.scale(tilesheet.subsurface((0,0,tile_width,tile_height)),
                                   (tile_width*ZOOM, tile_height*ZOOM))
    tile2 = pygame.transform.scale(tilesheet.subsurface((tile_width,0,tile_width,tile_height)),
                                   (tile_width*ZOOM, tile_height*ZOOM))
    return tile1, tile2


def draw_checker_map(screen, camera, tile1, tile2):
    TILE_SIZE = tile1.get_width() 

  
    start_x = int(camera.offset.x // TILE_SIZE) * TILE_SIZE
    start_y = int(camera.offset.y // TILE_SIZE) * TILE_SIZE

  
    tiles_x = (screen.get_width() // TILE_SIZE) + 2
    tiles_y = (screen.get_height() // TILE_SIZE) + 2

    for y in range(tiles_y):
        for x in range(tiles_x):
            world_x = start_x + x * TILE_SIZE
            world_y = start_y + y * TILE_SIZE

           
            if ((world_x // TILE_SIZE) + (world_y // TILE_SIZE)) % 2 == 0:
                tile = tile1
            else:
                tile = tile2

           
            screen.blit(tile, (world_x - camera.offset.x, world_y - camera.offset.y))
