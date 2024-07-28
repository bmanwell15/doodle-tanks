import Tanks
import json
import base64
from Engine import *


level = 1

mouseX = 0
mouseY = 0



def buildLevel(whichLevel):
    levelFile = open(f"./Assets/Levels/Level_{whichLevel}.json", "r")
    levelData = levelFile.readlines()
    levelFile.close()

    levelDataString = ''.join(levelData)
    levelData = json.loads(levelDataString)

    playerPos = levelData["tanks"]["player"]["position"].split(",")
    Tanks.player = Tanks.Player(int(playerPos[0]), int(playerPos[1]))

    bytess = base64.b64encode(levelDataString.encode("ascii"))
    print(str(bytess).removeprefix("b'").removesuffix("'"))
    string = base64.b64decode(bytess)
    string = json.loads(string)
    print(string)


def startEngine():
    Engine.start()


def onKeyPress(event):
    if not event.keysym in Engine.keysPressed:
        Engine.keysPressed.append(event.keysym)

def onKeyUp(event):
    if event.keysym in Engine.keysPressed:
        Engine.keysPressed.remove(event.keysym)

def onMouseMove(event):
    Core.mouseX = event.x
    Core.mouseY = event.y

def onMouseClick(event):
    Tanks.player.shoot()