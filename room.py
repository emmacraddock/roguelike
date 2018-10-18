import math
class Room(object):

    def __init__(self, x, y, height, width):
        self.x1 = x
        self.x2 = (x + width) - 1
        self.y1 = y
        self.y2 = (y + height) - 1

    def get_center(self):
            x = math.floor(self.x1 + ((self.x2 - self.x1) + 1) / 2 )
            y = math.floor(self.y1 + ((self.y2 - self.y1) + 1) / 2 )

            return Center(x, y)

    def intersects_room(self, room):
        return (self.x1 <= room.x2 and self.x2 >= room.x1
        and self.y1 <= room.y2 and self.y2 >= room.y1)
            
class Center(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y