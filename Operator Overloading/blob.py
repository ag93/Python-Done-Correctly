# -*- coding: utf-8 -*-
import random


class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4,8), movement_range=(-1,2)):
        self.size = random.randrange(size_range[0],size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.movement_range = movement_range
        
    def __add__(self, other_blob):
            if other_blob.color == (255, 0, 0):
                self.size -= other_blob.size
                other_blob.size -= self.size
                
            elif other_blob.color == (0, 255, 0):
                self.size += other_blob.size
                other_blob.size = 0
                
            elif other_blob.color == (0, 0, 255):
                # for now, nothing. Maybe later it does something more. 
                pass
            else:
                raise Exception('Tried to combine one or multiple blobs of unsupported colors!')
                
    def move(self):
        self.move_x = random.randrange(self.movement_range[0],self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0],self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary
        
        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
        
        