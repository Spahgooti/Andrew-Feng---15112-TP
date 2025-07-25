from cmu_graphics import *
from PIL import Image

class Location():
    def __init__(self, name, locX, locY, difficulty, fileName):
        self.name = name
        self.locX = locX
        self.locY = locY

        # difficulty ranges from 0 - 2:
        # normal mode takes images with difficulty 0-1, and hard mode takes 
        # images with difficulty 1-2
        self.difficulty = difficulty

        self.image = Image.open(fileName) 
    

    def draw(self, dx, dy, scale, app):
        
        imageWidth, imageHeight = self.image.size
        newWidth, newHeight = int(imageWidth * scale), int(imageHeight * scale)

        scaledImage = self.image.resize((newWidth, newHeight))
        scaledImage = CMUImage(scaledImage)

        imageCenterX, imageCenterY = app.width/2 + dx, app.height/2 + dy
        drawImage(scaledImage, imageCenterX, imageCenterY + dy, align = 'center')


def onAppStart(app):
    pass

def redrawAll(app):
    l1 = Location("Hallway", 20, 20, 3, "Locations/PXL_20250724_165159858.jpg")
    l1.draw(0, 0, 0.2, app)

def main():
    runApp(width = 1200, height = 700)

main()