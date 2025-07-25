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
        print(imageWidth, imageHeight)
        newWidth, newHeight = int(imageWidth * scale), int(imageHeight * scale)

        scaledImage = self.image.resize((newWidth, newHeight))
        scaledImage = CMUImage(scaledImage)

        imageCenterX, imageCenterY = app.width/2 + dx, app.height/2 + dy
        drawImage(scaledImage, imageCenterX, imageCenterY + dy, align = 'center')


def onAppStart(app):
    # from my phone's camera
    app.defaultImageWidth = 4032
    app.defaultImageHeight = 3024
    app.defaultImageScale = 0.5

    # Variables that stay constant over all games
    app.allLocations = [] # figure out how to add all the locations later

    # Variables that pertain to a specific game
    app.gameDifficulty = None # difficulty of the game
    app.gameLocations = []
    app.round = 0 # indexes into app.gameLocations, with 5 total rounds (0 - 4)
    app.score = 0

    app.imageScale = 1
    app.imageCX = app.width // 2
    app.imageCY = app.height // 2

    app.mapScale = 1
    app.mapX = None
    app.mapY = None

    app.guessX = None
    app.guessY = None

    # Colors
    app.bgColor1 = 'indigo'
    app.bgColor2 = 'darkSlateBlue'


################################################################################
# Starting Screen
################################################################################

def starting_redrawAll(app):
    # l1 = Location("Cathedral View", 20, 20, 3, "Locations/PXL_20250724_165953836.jpg")
    # l1.draw(0, 0, 0.5, app)
    backgroundGradient = gradient('indigo', 'darkSlateBlue', start = 'left')
    normalColor = rgb(151, 232, 81)
    hardColor = rgb(233, 69, 96)

    drawRect(0, 0, app.width, app.height, fill=backgroundGradient)
    drawLabel("CMU Geoguessr", app.width // 2, 200, size=96, fill = 'white')

    drawRect(app.width // 2, 600, 200, 100, fill = normalColor, align = 'center')
    drawRect(app.width // 2, 800, 200, 100, fill = hardColor, align = 'center')
    drawLabel("Normal Mode", app.width // 2, 600, size = 24, fill = 'white')
    drawLabel("Hard Mode", app.width // 2, 600, size = 24, fill = 'white')    

    pass

################################################################################
# Guessing Screen
################################################################################

def guessing_onScreenActivate(app):
    # get 5 locations of the right difficulty into a list
    pass

def guessing_redrawllAll(app):
    # display the first image over the full screen
    # display the map on the bottom right
    pass

def guessing_onMouseDrag(app, mouseX, mouseY):
    # if the mouse is on the image and not the map, drag the image
    # if the mouse is on the map, drag the map
    pass

def guessing_onMouseClick(app, mouseX, mouseY):
    # if the mouse is on the map, enter a guess on the map
    # set a variable like "app.guessEntered" to True
    pass

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
    runAppWithScreens(width = 4032//3, height = 3024//3, 
                      initialScreen = 'starting')
    pass

main()