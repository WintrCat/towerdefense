from engine.structures import Colour
from engine.gameobject import GameObject

class Scene:
    project = None

    background_colour = Colour(0, 0, 0)

    objects: list[GameObject] = []

    def __init__(self, name: str):
        self.name = name

    def add_object(self, obj: GameObject):
        obj.scene = self
        self.objects.append(obj)

    def remove_object(self, obj: GameObject):
        self.objects.remove(obj)

    def get_objects(self):
        return self.objects