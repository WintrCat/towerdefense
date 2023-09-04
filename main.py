from engine.project import Project
from engine.sprite import Sprite
from engine.structures import Colour

towerdefense = Project("Tower Defense", 960, 640)

main_menu = towerdefense.create_scene("main_menu")
towerdefense.create_scene("level_editor")

towerdefense.active_scene = main_menu

towerdefense.get_scene("main_menu").background_colour = Colour.from_hex("#00ff00")

# add objects buttons stuff
patrick = Sprite(50, 50, "patrick.png")
towerdefense.active_scene.objects.append(patrick)

towerdefense.run()