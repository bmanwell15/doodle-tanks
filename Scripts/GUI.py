import Core
import tkinter as tk
from FontHandler import FontHandler
from GUIComponents import GUIComponents
from ImagesHandler import ImageHandler
from PIL import Image, ImageTk

class Window:

    def __init__(self, VERSION) -> None:
        self.window: tk.Tk = tk.Tk()
        self.window.title(f"Doodle Tanks {VERSION}")
        self.width: int = 726
        self.height: int = 408
        self.window.minsize(self.width, self.height)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.bind('<KeyPress>', Core.onKeyPress)
        self.window.bind('<KeyRelease>', Core.onKeyUp)

        self.window.attributes('-fullscreen', True)
        #self.window.geometry(f"{str(self.width)}x{str(self.height)}")

        self.window.bind('<Escape>', lambda e: self.window.attributes('-fullscreen', False))

        # Frame is the content holder for each page
        self.frame: tk.Frame = tk.Frame(self.window)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)

        self.imageHandler = ImageHandler()

        self.showMainPage()
    

    def showMainPage(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.window)
        self.frame.grid_columnconfigure(0, weight=1)

        title = tk.Label(self.frame, text="Doodle Tanks", font=FontHandler.Kalam_Bold(75))
        title.grid(row=0, column=0, sticky='new', pady=0)

        playButton = GUIComponents.MainscreenButton(self.frame, self.imageHandler.getImage("Play Button"), self.imageHandler.getFilePath("Play Button"))
        playButton.bind("<Button-1>", lambda e: self.startGame())
        #playButton.config(command=self.startGame)
        playButton.grid(row=1, column=0, sticky="n", pady=8)

        sandboxButton = GUIComponents.MainscreenButton(self.frame, self.imageHandler.getImage("Sandbox Button"), self.imageHandler.getFilePath("Sandbox Button"))
        sandboxButton.grid(row=2, column=0, sticky="n", pady=8)

        statsButton = GUIComponents.MainscreenButton(self.frame, self.imageHandler.getImage("Stats Button"), self.imageHandler.getFilePath("Stats Button"))
        statsButton.grid(row=3, column=0, sticky="n", pady=8)

        self.frame.grid(row=0, column=0, sticky="nsew")
    

    def showPlayPage(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.window)
        self.frame.grid_columnconfigure(0, weight=1)

        backgroundFrame = self.setBackground("./Assets/Images/Wood Background.jpg")

        self.gameFrame = tk.Canvas(backgroundFrame, width=720, height=800)
        self.gameFrame.bind('<Motion>', Core.onMouseMove)
        self.gameFrame.bind("<Button>", Core.onMouseClick)
        self.gameFrame.grid(row=0, column=0, padx=60, pady=50, sticky="new")

        self.frame.grid(row=0, column=0, sticky="nsew")
    

    def startGame(self):
        self.showPlayPage()
        Core.buildLevel(Core.level)
        Core.startEngine()

    

    def setBackground(self, imagePath):
    # Load the image
        bgImage = Image.open(imagePath)
        bgPhoto = ImageTk.PhotoImage(bgImage)

        # Create a canvas
        canvas = tk.Canvas(self.frame, width=self.width, height=self.height)
        canvas.pack(fill='both', expand=True)

        # Set the image on the canvas
        canvas.create_image(0, 0, image=bgPhoto, anchor='nw')
        canvas.grid_rowconfigure(0, weight=1)
        canvas.grid_columnconfigure(0, weight=1)

        # Keep a reference to the image
        canvas.image = bgPhoto

        return canvas

gui: Window = None