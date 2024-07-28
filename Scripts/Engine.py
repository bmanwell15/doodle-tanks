import threading
import Tanks
import Core
import GUI
from GameObjects import *



class Engine:
    keysPressed = []
    bullets = []
    doodleBlobs = []

    def start():
        engineThread = threading.Thread(target=Engine.loop, daemon=True)
        engineThread.start()
    
    def loop():
        GUI.gui.gameFrame.delete("all")

        for doodle in Engine.doodleBlobs:
            doodleImage = GUI.gui.imageHandler.getImage(doodle[2])
            GUI.gui.gameFrame.create_image(doodle[0] + 10, doodle[1] + 10, image=doodleImage)
        
        for bullet in Engine.bullets:
            bullet.draw() # Draw before update incase bullet deletes inside update
            bullet.update()

        Tanks.player.update(Core.mouseX, Core.mouseY)
        Tanks.player.draw()


        GUI.gui.window.after(20, Engine.loop)