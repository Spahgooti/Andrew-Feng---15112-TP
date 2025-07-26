from cmu_graphics import *
import os
from PIL import Image

class Location():
    def __init__(self, locX, locY, difficulty, fileName):

        self.locX = locX
        self.locY = locY

        # difficulty ranges from 0 - 2:
        # normal mode takes images with difficulty 0-1, and hard mode takes 
        # images with difficulty 1-2
        self.difficulty = difficulty

        self.image = Image.open(fileName)
        self.image = CMUImage(self.image)

        # some cool images will get custom names
        self.name = None

    def draw(self, app, dx, dy, scale):
        
        imageWidth, imageHeight = getImageSize(self.image)
        newWidth, newHeight = int(imageWidth * scale), int(imageHeight * scale)

        imageCenterX, imageCenterY = app.width//2 + dx, app.height//2 + dy
        drawImage(self.image, imageCenterX, imageCenterY, align = 'center', 
                  width = newWidth, height = newHeight)

def importImages(app):
    listOfImages = []
    path = './Locations'
    files = os.listdir(path)
    
    for file in files:
        app.allLocations.append(CMUImage(Image.open(os.path.join(path, file))))
    return listOfImages

def onAppStart(app):
    # from my phone's camera
    app.defaultImageWidth = 4032
    app.defaultImageHeight = 3024
    app.defaultImageScale = 0.5

    # Variables that stay constant over all games
    app.defaultImageWidth = 4032
    app.defaultImageHeight = 3024

    # for image in Locations:
    #     #tempFile = image
    #     # locX = ?? probably some gps data
    #     # locY = ??
    #     # difficulty - has to be set manually, maybe itd be easier to keep track of the photos with an id?
    #     pass


    app.allLocations = [] # figure out how to add all the locations later
    importImages(app)

        
    # Variables that pertain to a specific game
    app.gameDifficulty = None # difficulty of the game
    app.gameLocations = []
    app.round = 0 # indexes into app.gameLocations, with 5 total rounds (0 - 4)
    app.score = 0

    app.imageScale = 0.4
    # These variables help store the differences between the x and y coordinates  
    # of the image's center with the center of the canvas
    app.totalImageDX = 0
    app.totalImageDY = 0
    app.currDragImageDX = 0
    app.currDragImageDY = 0
    app.isDraggingImage = False  # the user could be dragging the map, not the photo
    
    app.startDragX = 0
    app.startDragY = 0

    app.mapScale = 1
    app.mapX = None
    app.mapY = None

    app.guessX = None
    app.guessY = None

    app.l1 = Location(0, 0, 0, "Locations/PXL_20250724_165250547.jpg")

################################################################################
# Starting Screen
################################################################################

def starting_redrawAll(app):

    backgroundGradient = gradient('indigo', 'darkSlateBlue', start = 'bottom')
    normalColor = rgb(151, 232, 81)
    hardColor = rgb(233, 69, 96)

    drawRect(0, 0, app.width, app.height, fill=backgroundGradient)
    drawLabel("CMU Geoguessr", app.width // 2, 200, size=96, fill = 'white')

    buttonWidth = 200
    buttonHeight = 100
    drawRect(app.width // 2, 525, buttonWidth, buttonHeight, 
             fill = normalColor, align = 'center')
    drawRect(app.width // 2, 650, buttonWidth, buttonHeight, 
             fill = hardColor, align = 'center')
    
    drawLabel("Normal Mode", app.width // 2, 525, size = 24, fill = 'white')
    drawLabel("Hard Mode", app.width // 2, 650, size = 24, fill = 'white') 
    # drawImage(app.allLocations[0], 0, 0)   

def starting_onMousePress(app, mouseX, mouseY):
    buttonWidth = 200
    buttonHeight = 100
    # user clicked normal mode
    if (app.width//2 - buttonWidth//2 <= mouseX <= app.width//2 + buttonWidth//2 and
        525 - buttonHeight//2 <= mouseY <= 525 + buttonHeight//2):
        app.gameDifficulty = "Normal"
        # app.gameLocations = getGameLocations(app)
        setActiveScreen('guessing')
    
    # user clicked hard mode
    if (app.width//2 - buttonWidth//2 <= mouseX <= app.width//2 + buttonWidth//2 and
        650 - buttonHeight//2 <= mouseY <= 650 + buttonHeight//2):
        app.gameDifficulty = "Hard"
        # app.gameLocations = getGameLocations(app)
        setActiveScreen('guessing')

def getGameLocations(app):
    pass

################################################################################
# Guessing Screen
################################################################################

def guessing_redrawAll(app):
    # display the first image over the full screen
    # display the map on the bottom right
    imageCenterDX = app.currDragImageDX + app.totalImageDX
    imageCenterDY = app.currDragImageDY + app.totalImageDY


    
    app.l1.draw(app, imageCenterDX, imageCenterDY, app.imageScale)

def guessing_onMousePress(app, mouseX, mouseY):
    # if the mouse is on the map, enter a guess on the map
    # set a variable like "app.guessEntered" to True

    # if the mouse is on the image of the location
    app.startDragX = mouseX
    app.startDragY = mouseY

    


def guessing_onMouseDrag(app, mouseX, mouseY):
    # if the mouse is on the image and not the map, drag the image
    # if the mouse is on the map, drag the map

    app.currDragImageDX = mouseX - app.startDragX
    app.currDragImageDY = mouseY - app.startDragY

    scaledImageWidth = app.defaultImageWidth * app.imageScale
    scaledImageHeight = app.defaultImageHeight * app.imageScale
    imageCenterDX = app.currDragImageDX + app.totalImageDX
    imageCenterDY = app.currDragImageDY + app.totalImageDY

    # These tests make sure that the image of the location is not dragged off
    # of the screen.
    if imageCenterDX >= scaledImageWidth // 2 - app.width // 2:
        app.totalImageDX = scaledImageWidth // 2 - app.width // 2
        app.currDragImageDX = 0
    if imageCenterDX <= -(scaledImageWidth // 2 - app.width // 2):
        app.totalImageDX = -(scaledImageWidth // 2 - app.width // 2)
        app.currDragImageDX = 0

    if imageCenterDY >= scaledImageHeight // 2 - app.height // 2:
        app.totalImageDY = scaledImageHeight // 2 - app.height // 2
        app.currDragImageDY = 0
    if imageCenterDY <= -(scaledImageHeight // 2 - app.height // 2):
        app.totalImageDY = -(scaledImageHeight // 2 - app.height // 2)
        app.currDragImageDY = 0

def guessing_onMouseRelease(app, mouseX, mouseY):

    # This updates the total distance by which the image has been dragged
    app.totalImageDX += app.currDragImageDX
    app.totalImageDY += app.currDragImageDY
    app.currDragImageDX = 0
    app.currDragImageDY = 0




def guessing_onKeyPress(app, key):
    # if a guess has been entered, actually enter the guess
    # calculate the score/distance of the guess from the true location
    # add score to the user's current score
    # switch the screen to the post guess screen
    pass

################################################################################
# Post Guess Screen
################################################################################

def postGuess_onScreenActivate(app):
    pass


def main():
    runAppWithScreens(width = 1400, height = 860, 
                      initialScreen = 'starting')


main()