from engine.structures import Colour
from engine.gameobject import GameObject

class Scene:
    background_colour = Colour(0, 0, 0)
    
    objects: list[GameObject] = []

    def __init__(self, name: str):
        self.name = name