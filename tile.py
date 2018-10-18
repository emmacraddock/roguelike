class Tile:
    def __init__(self, tile_type, is_walkable = False, is_visible = False):
        self.tile_type = tile_type
        self.is_walkable = is_walkable
        self.is_visible = is_visible
            

class TileType:
     empty = 0
     dirt = 1
     wall = 2
     floor = 3