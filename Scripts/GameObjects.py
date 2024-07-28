import GUI
import math
import Engine


class GameObject:
    def __init__(self) -> None:
        pass

    def draw():
        pass

    def update():
        pass

class Bullet(GameObject):
    WIDTH = 3
    HEIGHT = 10
    SPEED = 10

    def __init__(self, x: int, y: int, angle: float) -> None:
        self.x = x
        self.y = y
        self.angle = angle
        self.hasBounced = False
        self.image = GUI.gui.imageHandler.rotateImage("Bullet", self.angle)
    
    def draw(self):
        GUI.gui.gameFrame.create_image(self.x, self.y, image=self.image)
    
    def update(self):
        self.x -= Bullet.SPEED * math.sin(self.angle * math.pi / 180)
        self.y -= Bullet.SPEED * math.cos(self.angle * math.pi / 180)

        if self.x < 0 or self.y < 0 or self.x > GUI.gui.gameFrame.winfo_width() or self.y > GUI.gui.gameFrame.winfo_height():
            Engine.Engine.bullets.remove(self)