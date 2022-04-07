import pygame


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def get_coordinates(self) -> tuple:
        return self.x, self.y