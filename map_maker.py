import pygame
import random
import math
from map import Map
from room import *
from tile import *

MAP_ROWS = 100 # number of rows in the map
MAP_COlUMNS = 100 # number of columns in the map

HORIZONTAL_OFFSET = 50 # horizontal offset of map on screen
VERTICAL_OFFSET = 50 # vertical offset of map on screen

WALL_SIZE = 1 # wall size. this will be added to room size

MAX_WIDTH = 30 # the max and min width for any room
MIN_WIDTH = 8

MAX_HEIGHT = 30 # the max and min height for any room
MIN_HEIGTH = 8

NBR_OF_ROOMS = 2 # number of rooms to create

# map should probz be a global variable

def initialize_map():
    # initializes a 2-dimensional array. this represents the map.
    _map = [[0 for x in range(MAP_COlUMNS)] for y in range(MAP_ROWS)]

    # adds an empty tile to each index in the map
    for row in range(MAP_ROWS):
        for column in range(MAP_COlUMNS):
            _map[row][column] = Tile(TileType.empty)
    
    return _map

def create_room():

    # figure out height and width of prospective room
    room_width = random.randint(MIN_WIDTH, (MAX_WIDTH + WALL_SIZE))
    room_height = random.randint(MIN_HEIGTH, (MAX_HEIGHT + WALL_SIZE))

    x = random.randint(0, (MAP_COlUMNS - room_width))
    y = random.randint(0, (MAP_ROWS - room_height)) 

    return Room(x, y, room_height, room_width) # room calculates x2 and y2

def add_room_to_map(room, _map):
    
    for row in range(MAP_ROWS):
            if row >= room.y1 and row <= room.y2:
                for column in range(MAP_COlUMNS):

                    if column >= room.x1 and column <= room.x2:
                        if row == room.y1 or row == room.y2:
                            _map[row][column] = Tile(TileType.wall)
                        elif column == room.x1 or column == room.x2:
                            _map[row][column] = Tile(TileType.wall)
                        else: 
                            _map[row][column] = Tile(TileType.floor)
    return _map

def create_corridor(_map, new_center, last_center):

    # SHOULD ACTUALLY CREATE A CORRIDOR OBJECT that can draw itself on the map.
    # it could have two properties, h_corridor and v_corridor
    if random.randint(0,1) == 1:
        _map = draw_h_corridor(_map, last_center.x, new_center.x, last_center.y)
        _map = draw_v_corridor(_map, last_center.y, new_center.y, new_center.x)
    else:
        _map = draw_v_corridor(_map, last_center.y, new_center.y, last_center.x)
        _map = draw_h_corridor(_map, last_center.x, new_center.x, new_center.y)

    return _map

def draw_v_corridor(_map, y1, y2, x):
    
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if _map[y][x].tile_type is not TileType.floor:
            _map[y][x] = Tile(TileType.floor)

    return _map

def draw_h_corridor(_map, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        if _map[x][y].tile_type is not TileType.floor:
            _map[y][x] = Tile(TileType.floor)
    return _map

def get_map():

    _map = initialize_map()
    
    rooms = []
    r = 0
    while r < NBR_OF_ROOMS:

    # get room
        new_room = create_room()

    # check if room intersects other rooms
        failed = False
        for room in rooms:
            failed = new_room.intersects_room(room)
            if failed == True:
                break # if so, don't incriment loop.
        
        if failed is False:          

            rooms.append(new_room)  # if not, add to rooms list  
            _map = add_room_to_map(new_room, _map) # draw room on map

            # draw corridors
            if len(rooms) > 1:
                last_room = rooms[len(rooms) - 2]
                _map = create_corridor(_map, new_room.get_center(), last_room.get_center())

            r+=1

    return Map(MAP_ROWS, MAP_COlUMNS, HORIZONTAL_OFFSET, VERTICAL_OFFSET, _map)
        


    