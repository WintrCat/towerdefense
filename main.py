from engine.project import Project
from engine.structures import Colour

towerdefense = Project("Tower Defense", 960, 640)

main_menu = towerdefense.create_scene("main_menu")
towerdefense.create_scene("level_editor")

towerdefense.active_scene = main_menu

towerdefense.get_scene("main_menu").background_colour = Colour.from_hex("#00ff00")

# add objects buttons stuff

towerdefense.run()