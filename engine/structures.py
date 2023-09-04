from random import randint

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Colour:
    def __init__(self, red: int, green: int, blue: int):
        if red < 0 or red > 255 or green < 0 or green > 255 or blue < 0 or blue > 255:
            raise Exception("Invalid RGB values specified for colour.")

        self.red = red
        self.green = green
        self.blue = blue

    def to_tuple(self):
        return (self.red, self.green, self.blue)

    def from_rgb(red: int, green: int, blue: int):
        return Colour(red, green, blue)
    
    def from_hex(hex_code: str):
        hex_code = hex_code.lstrip("#")
        if len(hex_code) != 6:
            raise Exception("Invalid colour hex code specified.")
        return Colour(int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16))
    
    def random():
        return Colour(randint(0, 255), randint(0, 255), randint(0, 255))
    
    def invert(self):
        return Colour(255 - self.red, 255 - self.green, 255 - self.blue)
    
class Rectangle:
    def __init__(self, x: float, y: float, width: float = 0, height: float = 0):
        self.x = x
        self.y = y
        self.width = width if width > 0 else 2 ** 16
        self.height = height if height > 0 else 2 ** 16