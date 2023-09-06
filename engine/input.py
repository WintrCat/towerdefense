import pygame

class Input:
    def mouse_x():
        return pygame.mouse.get_pos()[0]
    
    def mouse_y():
        return pygame.mouse.get_pos()[1]
    
    def is_key_pressed(key: str):
        return pygame.key.get_pressed()[pygame.key.key_code(key)]

    def horizontal_axis():
        axis = 0
        if Input.is_key_pressed("d") or Input.is_key_pressed("right"):
            axis += 1
        if Input.is_key_pressed("a") or Input.is_key_pressed("left"):
            axis -= 1
        return axis

    def vertical_axis():
        axis = 0
        if Input.is_key_pressed("w") or Input.is_key_pressed("up"):
            axis += 1
        if Input.is_key_pressed("a") or Input.is_key_pressed("down"):
            axis -= 1
        return axis