import pygame

from engine.structures import Rectangle
from engine.gameobject import GameObject

class Sprite(GameObject):
    scale_x: float = 1
    scale_y: float = 1
    flip_x: bool = False
    flip_y: bool = False
    rotation: float = 0
    opacity: float = 1

    mask: Rectangle = None

    def __init__(self, x: float, y: float, texture_path: str):
        super().__init__(x, y)
        self.__texture = pygame.image.load(texture_path).convert_alpha()

    def draw(self, window: pygame.surface.Surface):
        mask_rect = None
        if self.mask != None:
            mask_rect = pygame.Rect(self.mask.x, self.mask.y, self.mask.width, self.mask.height)

        baked_texture = self.__texture

        baked_texture.set_alpha(self.opacity * 255)
        baked_texture = pygame.transform.flip(baked_texture, self.flip_x, self.flip_y)
        baked_texture = pygame.transform.scale(baked_texture, (
            self.__texture.get_width() * self.scale_x, 
            self.__texture.get_height() * self.scale_y
        ))
        baked_texture = pygame.transform.rotate(baked_texture, 360 - self.rotation)

        window.blit(baked_texture, (self.x, self.y), mask_rect)

    def width(self):
        return self.__texture.get_width() * self.scale_x
    
    def height(self):
        return self.__texture.get_height() * self.scale_y
