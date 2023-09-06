import pygame
from time import sleep

from engine.input import Input
from engine.scene import Scene
from engine.sprite import Sprite

class Project:
    __scenes: list[Scene] = []
    active_scene: Scene = None

    target_fps = 30

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

        pygame.init()
        pygame.mixer.init()

        self.__window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)

    # set window icon
    def set_icon(self, icon_path: str):
        icon_image = pygame.image.load(icon_path)
        pygame.display.set_icon(icon_image)

    # manage scenes
    def create_scene(self, name: str):
        for scene in self.__scenes:
            if scene.name == name:
                raise Exception(f"Scene with name '{name}' already exists.")
            
        new_scene = Scene(name)
        new_scene.project = self
            
        self.__scenes.append(new_scene)
        return new_scene

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
    def run(self, debug=False):
        if self.active_scene == None:
            raise Exception("This project does not have an active scene.")
        
        debugFont = pygame.font.SysFont("Arial", 16)

        # run all ready scripts on objects
        for obj in self.active_scene.objects:
            for script in obj.scripts:
                script.ready(obj)
        
        while True:
            # calculate delta time
            deltaTime = 1 / self.target_fps

            # clear frame
            self.__window.fill(self.active_scene.background_colour.to_tuple())

            # draw scene objects
            for obj in self.active_scene.objects:
                for script in obj.scripts:
                    script.update(obj, deltaTime)

                if isinstance(obj, Sprite):
                    obj.draw(self.__window)

            # draw debug information
            if debug:
                self.__window.blit(
                    debugFont.render(
                        f"X: {Input.mouse_x()}, Y: {Input.mouse_y()}", 
                        False, 
                        self.active_scene.background_colour.invert().to_tuple()
                    ),
                    (5, 5)
                )

            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
            sleep(deltaTime)
            
    
# engine by wilson