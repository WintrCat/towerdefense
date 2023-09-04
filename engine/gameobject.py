class GameObject:
    scene = None
    scripts = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_script(self, module):
        self.scripts.append(module)
    
    def get_scripts(self):
        return self.scripts