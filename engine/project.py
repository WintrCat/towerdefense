import pygame

from engine.scene import Scene
from engine.sprite import Sprite

class Project:
    __scenes: list[Scene] = []
    
    active_scene: Scene = None

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

        self.__window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)

    # manage scenes
    def create_scene(self, name: str):
        for scene in self.__scenes:
            if scene.name == name:
                raise Exception(f"Scene with name '{name}' already exists.")
            
        self.__scenes.append(Scene(name))
        return self.__scenes[-1]

    def delete_scene(self, name: str):
        for scene in self.__scenes:
            if scene.name == name:
                self.__scenes.remove(scene)
                break

    def get_scenes(self):
        return self.__scenes

    def get_scene(self, name: str):
        for scene in self.__scenes:
            if scene.name == name:
                return scene
            
    # start application
    def run(self):
        if self.active_scene == None:
            raise Exception("This project does not have an active scene.")
        
        pygame.init()
        while True:
            # clear frame
            self.__window.fill(self.active_scene.background_colour.to_tuple())

            # draw scene objects
            for obj in self.active_scene.objects:
                if isinstance(obj, Sprite):
                    obj.draw(self.__window)

            # check for events
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
            
    
# engine by wilson