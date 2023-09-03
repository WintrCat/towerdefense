from pygame import image, surface, Rect

from engine.gameobject import GameObject

class Sprite(GameObject):
    scale_x: float = 1
    scale_y: float = 1
    opacity: float = 1

    def __init__(self, x: float, y: float, texture_path: str):
        super().__init__(x, y)
        self.__texture = image.load(texture_path)

    def draw(self, window: surface.Surface):
        window.blit(
            self.__texture, 
            Rect(
                self.x, 
                self.y, 
                self.__texture.get_width() * self.scale_x, 
                self.__texture.get_height() * self.scale_y
            )
        )
