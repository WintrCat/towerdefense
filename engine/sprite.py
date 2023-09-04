import pygame

from engine.structures import Rectangle
from engine.gameobject import GameObject

class Sprite(GameObject):
    scale_x: float = 1
    scale_y: float = 1
    flip_x: bool = False
    flip_y: bool = False
    opacity: float = 1

    mask: Rectangle = None

    def __init__(self, x: float, y: float, texture_path: str):
        super().__init__(x, y)
        self.__texture = pygame.image.load(texture_path).convert_alpha()

    def draw(self, window: pygame.surface.Surface):
        mask_rect = None
        if self.mask != None:
            mask_rect = pygame.Rect(self.mask.x, self.mask.y, self.mask.width, self.mask.height)

        self.__texture.set_alpha(self.opacity * 255)
        window.blit(
            pygame.transform.flip(
                pygame.transform.scale(self.__texture, (
                    self.__texture.get_width() * self.scale_x, 
                    self.__texture.get_height() * self.scale_y
                )), 
                self.flip_x, 
                self.flip_y
            ),
            (self.x, self.y),
            mask_rect
        )

    def width(self):
        return self.__texture.get_width() * self.scale_x
    
    def height(self):
        return self.__texture.get_height() * self.scale_y
