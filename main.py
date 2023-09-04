from engine.project import Project
from engine.sprite import Sprite
from engine.structures import Colour

towerdefense = Project("Tower Defense", 960, 640)

main_menu = towerdefense.create_scene("main_menu")
towerdefense.create_scene("level_editor")

towerdefense.active_scene = main_menu

main_menu.background_colour = Colour.from_hex("#00ff00")

# add objects buttons stuff
patrick = Sprite(100, 100, "patrick.png")
patrick.scale_x = 0.3
patrick.scale_y = 0.3

import patrick as patricklib
patrick.add_script(patricklib)

main_menu.add_object(patrick)

towerdefense.run(True)