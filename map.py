import pygame
from tile import TileType

class Map(object):
    def __init__(self, map_rows, map_columns, x_offset, y_offset, _map):
        
        self.rows = map_rows
        self.columns = map_columns
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.map = _map

    def draw_map(self, screen):
        
        tile_size_y = 0

        for row in range(self.rows):
            
            tile_size_x = 0
            
            for column in range(self.columns):

                tile = self.map[row][column]

                x = column + self.x_offset + tile_size_x
                y = row + self.y_offset + tile_size_y
                
                tile_size_x += 8 # the width of the tile in pixels
                
                rect = pygame.Rect(x, y, 8, 8)
                
                if tile.tile_type == TileType.wall:
                    color = (255, 255, 255) # white
                    pygame.draw.rect(screen, color, rect)

                elif tile.tile_type == TileType.floor:
                    color = (47,79,79) # grey
                    pygame.draw.rect(screen, color, rect)

            tile_size_y += 8    # the height of the tile in pixels