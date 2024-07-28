import GUI
import math
from Engine import Engine
import GameObjects
from random import randint


class Tank(GameObjects.GameObject):
    WIDTH = 40
    HEIGHT = 40

    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.color = "Black"
        self.doodleColor = "Black"
        self.bodyImage = None
        self.gunImage = None


class Player(Tank):
    SPEED = 4

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.bodyImage = GUI.gui.imageHandler.getImage("Player")
        self.gunImage = GUI.gui.imageHandler.getImage("Player Gun")
        self.color = "Blue"
        self.doodleColorFileName = "Player Doodle"
        self.angleFromMouse = 0
    
    def draw(self):
        GUI.gui.gameFrame.create_image(self.x, self.y, image=self.bodyImage)
        GUI.gui.gameFrame.create_image(self.x, self.y, image=self.gunImage)
    
    def move(self):
        keysPressed = list(Engine.keysPressed) # Create a copy of the list (for preformence boosting)
        if 'w' in keysPressed and not ("a" in keysPressed or "d" in keysPressed): # W
            self.y -= Player.SPEED
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 0)
        elif 'w' in keysPressed and 'a' in keysPressed: # W & A
            self.x -= math.sqrt(Player.SPEED)
            self.y -= math.sqrt(Player.SPEED)
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 45)
        elif 'w' in keysPressed and 'd' in keysPressed: # W & D
            self.x += math.sqrt(Player.SPEED)
            self.y -= math.sqrt(Player.SPEED)
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 315)
        elif 's' in keysPressed and not ("a" in keysPressed or "d" in keysPressed): # S
            self.y += Player.SPEED
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 180)
        elif 's' in keysPressed and "a" in keysPressed: # S & A
            self.y += math.sqrt(Player.SPEED)
            self.x -= math.sqrt(Player.SPEED)
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 125)
        elif 's' in keysPressed and "d" in keysPressed: # S & D
            self.y += math.sqrt(Player.SPEED)
            self.x += math.sqrt(Player.SPEED)
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 225)
        elif 'a' in keysPressed: # A
            self.x -= Player.SPEED
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 90)
        elif 'd' in keysPressed: # D
            self.x += Player.SPEED
            self.bodyImage = GUI.gui.imageHandler.rotateImage("Player", 270)
        
        if self.x < Tank.WIDTH/2: self.x = Tank.WIDTH/2
        if self.y < Tank.HEIGHT/2: self.y = Tank.HEIGHT/2
        if self.x > GUI.gui.gameFrame.winfo_width() - Tank.WIDTH/2: self.x = GUI.gui.gameFrame.winfo_width() - Tank.WIDTH/2
        if self.y > GUI.gui.gameFrame.winfo_height() - Tank.HEIGHT/2: self.y = GUI.gui.gameFrame.winfo_height() - Tank.HEIGHT/2
        
        if randint(0, 10) == 0:
            self.doodle()
    
    def update(self, mouseX, mouseY):
        self.move()

        self.angleFromMouse = (math.atan2(-(mouseY - self.y), mouseX - self.x) * (180/math.pi)) - 90
        self.gunImage = GUI.gui.imageHandler.rotateImage("Player Gun", self.angleFromMouse)
    
    def doodle(self):
        Engine.doodleBlobs.append( (self.x, self.y, self.doodleColorFileName) )

    def shoot(self):
        Engine.bullets.append(GameObjects.Bullet(self.x + 10, self.y + 10, self.angleFromMouse))





player: Player = None
enemyTanks: list[Tank] = []