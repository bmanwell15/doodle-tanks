import tkinter as tk
from PIL import Image, ImageTk
from ImagesHandler import ImageHandler

class GUIComponents:

    def rotateImage(imagePath, angle) -> ImageTk.PhotoImage:
        image = Image.open(imagePath)
        width = image.width
        height = image.height
        rotatedImage = image.rotate(angle, expand=True, resample=Image.BICUBIC)
        return ImageTk.PhotoImage(rotatedImage, width=width, height=height)


    def MainscreenButton(master, image: tk.PhotoImage, imagePath: str) -> tk.Button:
        button = tk.Label(master, image=image, width=image.width(), height=70, relief='flat', cursor='hand2')
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(0, weight=1)

        hoverImage = GUIComponents.rotateImage(imagePath, -4)
        button.bind('<Enter>', lambda e: button.config(image=hoverImage))
        button.bind('<Leave>', lambda e: button.config(image=image))
        return button