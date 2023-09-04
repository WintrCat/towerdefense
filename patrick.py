from engine.structures import Colour

SPEED_X = SPEED_Y = 200

def ready(obj):
    print("bruh")

def update(obj, delta):
    global SPEED_X, SPEED_Y

    obj.x += SPEED_X * delta
    obj.y += SPEED_Y * delta

    if obj.x > (960 - obj.width()) or obj.x < 0:
        SPEED_X *= -1
        obj.scene.background_colour = Colour.random()
    elif obj.y > (640 - obj.height()) or obj.y < 0:
        SPEED_Y *= -1
        obj.scene.background_colour = Colour.random()

    