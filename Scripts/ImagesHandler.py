from PIL import Image, ImageTk
import os
import GUI

class ImageHandler:
    def __init__(self) -> None:
        self._filePaths = ImageHandler._getAllFiles()

        self._images = []

        for path in self._filePaths:
            pil_image = Image.open(path)  # Open with Pillow
            tk_image = ImageTk.PhotoImage(pil_image)  # Convert to Tkinter-compatible format
            self._images.append(tk_image)


    def getFilePath(self, fileName: str):
        for path in self._filePaths:
            if path[path.rfind("\\")+1:path.rfind(".")].lower() == fileName.lower() != -1:
                return path
    
    def getImage(self, imageName: str):
        path = self.getFilePath(imageName)
        return self._images[self._filePaths.index(path)]

    def rotateImage(self, imageName: str, angle: float, resample=Image.BILINEAR):
        rotatedImage = Image.open(GUI.gui.imageHandler.getFilePath(imageName)).rotate(angle, resample=resample, expand=True)
        return ImageTk.PhotoImage(image=rotatedImage)
    
    def _getAllFiles():
        directory = "./Assets/Images"
        allFiles = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                allFiles.append(os.path.join(root, file))
        return allFiles
