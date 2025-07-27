from cmu_graphics import *
import os
import random
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
        self.image = CMUImage(self.image)

    def draw(self, app, dx, dy, scale):
        
        imageWidth, imageHeight = getImageSize(self.image)
        newWidth, newHeight = int(imageWidth * scale), int(imageHeight * scale)

        imageCenterX, imageCenterY = app.width//2 + dx, app.height//2 + dy
        drawImage(self.image, imageCenterX, imageCenterY, align = 'center', 
                  width = newWidth, height = newHeight)

# def importImages(app): # From TA
#     listOfImages = []
#     path = './Locations'
#     files = os.listdir(path)
    
#     for file in files:
#         app.allLocations.append(CMUImage(Image.open(os.path.join(path, file))))
#     return listOfImages
def initializeLocations(app):
    app.allLocations.append(Location("Evacuation", 413, 170, 2, "Locations/tepper1.jpg"))
    app.allLocations.append(Location("An Enthralling Bulletin Board", 360, 216, 2, "Locations/tepper2.jpg"))
    app.allLocations.append(Location("Big Glass Window", 364, 214, 0, "Locations/tepper3.jpg"))
    app.allLocations.append(Location("Cathedral View", 332, 232, 2, "Locations/tepper4.jpg"))
    app.allLocations.append(Location("Message", 690, 878, 2, "Locations/kraus1.jpg"))

def onAppStart(app):
    # from my phone's camera
    app.defaultImageWidth = 4032
    app.defaultImageHeight = 3024
    app.defaultImageScale = 0.5

    app.allLocations = [] # figure out how to add all the locations later
    initializeLocations(app)

        
    # Variables that pertain to a specific game
    app.gameDifficulty = None # difficulty of the game
    app.gameLocations = []
    app.round = 0 # indexes into app.gameLocations, with 5 total rounds (0 - 4)
    app.totalScore = 0
    app.roundScore = 0

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

    # these variables refer to the map as a whole
    app.map = Image.open("CMUMap.png")
    # the default map size is 1362 x 1050
    app.defaultMapWidth = 1362
    app.defaultMapHeight = 1050
    app.mapWidth, app.mapHeight = app.map.size
    app.mapScale = 1
    
    # these variables refer to the part of the map that is actually visible
    app.mapViewWidth, app.mapViewHeight = 216, 216
    app.mapView = app.map.crop((app.mapWidth // 2 - app.mapViewWidth // 2, 
                                app.mapHeight // 2 - app.mapViewHeight // 2, 
                                app.mapWidth // 2 + app.mapViewWidth // 2, 
                                app.mapHeight // 2 + app.mapViewHeight // 2))
    
    app.mapTopLeftX = app.width - app.mapViewWidth - 50
    app.mapTopLeftY = app.height - app.mapViewHeight - 50
    app.currDragMapDX = 0
    app.currDragMapDY = 0
    app.totalMapDX = 0
    app.totalMapDY = 0

    # These variables are taken with respect to the map. Note that (0, 0) is 
    # the top left of the full map.)
    app.guessX = None
    app.guessY = None

    # only for testing purposes:
    # app.l1 = Location(0, 0, 0, "Locations/PXL_20250724_202010299.jpg")

################################################################################
# Starting Screen
################################################################################

def starting_redrawAll(app):

    backgroundGradient = gradient('indigo', 'darkSlateBlue', start = 'bottom')
    normalColor = rgb(151, 232, 81)
    hardColor = rgb(233, 69, 96)
    wordOutline = rgb(204, 48, 46)

    drawRect(0, 0, app.width, app.height, fill=backgroundGradient)
    drawLabel('CMU Geoguessr', app.width // 2, 200, size = 128, fill = 'white',
              border = wordOutline, borderWidth = 3, bold = True)

    buttonWidth = 200
    buttonHeight = 100
    drawRect(app.width // 2, 525, buttonWidth, buttonHeight, 
             fill = normalColor, align = 'center')
    drawRect(app.width // 2, 650, buttonWidth, buttonHeight, 
             fill = hardColor, align = 'center')
    
    drawLabel('Normal Mode', app.width // 2, 525, size = 24, fill = 'white')
    drawLabel('Hard Mode', app.width // 2, 650, size = 24, fill = 'white')   

def starting_onMousePress(app, mouseX, mouseY):
    buttonWidth = 200
    buttonHeight = 100
    # user clicked normal mode
    if (app.width//2 - buttonWidth//2 <= mouseX <= app.width//2 + buttonWidth//2 and
        525 - buttonHeight//2 <= mouseY <= 525 + buttonHeight//2):
        app.gameDifficulty = 'Normal'
        app.gameLocations = getGameLocations(app)
        setActiveScreen('guessing')
    
    # user clicked hard mode
    if (app.width//2 - buttonWidth//2 <= mouseX <= app.width//2 + buttonWidth//2 and
        650 - buttonHeight//2 <= mouseY <= 650 + buttonHeight//2):
        app.gameDifficulty = 'Hard'
        app.gameLocations = getGameLocations(app)
        setActiveScreen('guessing')

def getGameLocations(app):
    currLocations = []

    while len(currLocations) < 5:
        numLocations = len(app.allLocations)
        locationIdx = random.randint(0, numLocations - 1)
        location = app.allLocations[locationIdx]
        
        if location.difficulty <= 2000 and location not in currLocations:
            currLocations.append(location)
    
    return currLocations


################################################################################
# Guessing Screen
################################################################################

def guessing_redrawAll(app):
    # display the first image over the full screen
    # display the map on the bottom right
    imageCenterDX = app.currDragImageDX + app.totalImageDX
    imageCenterDY = app.currDragImageDY + app.totalImageDY
    
    # app.l1.draw(app, imageCenterDX, imageCenterDY, app.imageScale)
    app.gameLocations[app.round].draw(app, imageCenterDX, imageCenterDY, app.imageScale)
    drawImage(CMUImage(app.mapView), app.mapTopLeftX, app.mapTopLeftY)


# NoTE TO SELF: make sure that the star isn't visible if the user scrolls the guess off the map
    if app.guessX != None and app.guessY != None: 
        
        mapViewLeft = app.mapWidth // 2 - app.mapViewWidth // 2 - app.currDragMapDX - app.totalMapDX
        mapViewTop = app.mapHeight // 2 - app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY

        # We get the location of the guess with respect to the left side of the 
        # viewable part of the map, and obtain the guess's location with respect
        # to the canvas by adding back app.mapTopLeftX and app.mapTopLeftY
    
        drawCircle(app.guessX - mapViewLeft + app.mapTopLeftX, 
                   app.guessY - mapViewTop + app.mapTopLeftY, 10, fill = 'red')



def guessing_onMousePress(app, mouseX, mouseY, button):
    # if the mouse is on the map, enter a guess on the map
    # set a variable like "app.guessEntered" to True

    # if the mouse is on the image of the location
    app.startDragX = mouseX
    app.startDragY = mouseY
    if button == 0:
        if not (app.mapTopLeftX <= mouseX <= app.mapTopLeftX + app.mapViewWidth 
                and app.mapTopLeftY <= mouseY <= app.mapTopLeftY + app.mapViewHeight):
            app.isDraggingImage = True
    if button == 2:
        if (app.mapTopLeftX <= mouseX <= app.mapTopLeftX + app.mapViewWidth and
            app.mapTopLeftY <= mouseY <= app.mapTopLeftY + app.mapViewHeight):
            mapViewLeft = app.mapWidth // 2 - app.mapViewWidth // 2 - app.totalMapDX
            mapViewTop = app.mapHeight // 2 - app.mapViewHeight // 2 - app.totalMapDY

            app.guessX = mouseX - app.mapTopLeftX + mapViewLeft
            app.guessY = mouseY - app.mapTopLeftY + mapViewTop
            # setting the coordinates of app.guessX and app.guessY to be with
            # respect of the top left corner of the map, rather than the canvas
            print(app.guessX, app.guessY)


def guessing_onMouseDrag(app, mouseX, mouseY):
    # if the mouse is on the image and not the map, drag the image
    # if the mouse is on the map, drag the map

    if app.isDraggingImage:
        moveImage(app, mouseX, mouseY)
    else: # the map is being dragged
        moveMap(app, mouseX, mouseY)


def moveImage(app, mouseX, mouseY):
        app.currDragImageDX = mouseX - app.startDragX
        app.currDragImageDY = mouseY - app.startDragY

        scaledImageWidth = app.defaultImageWidth * app.imageScale
        scaledImageHeight = app.defaultImageHeight * app.imageScale
        imageCenterDX = app.currDragImageDX + app.totalImageDX
        imageCenterDY = app.currDragImageDY + app.totalImageDY

        # These tests make sure that the image of the location is not dragged
        # off of the screen.
        if imageCenterDX >= scaledImageWidth // 2 - app.width // 2:
            app.totalImageDX = scaledImageWidth // 2 - app.width // 2
            app.startDragX = mouseX 
            # resetting the start position of the drag so the image 
            # doesn't get "stuck" at any side
            app.currDragImageDX = 0
        if imageCenterDX <= -(scaledImageWidth // 2 - app.width // 2):
            app.totalImageDX = -(scaledImageWidth // 2 - app.width // 2)
            app.startDragX = mouseX
            app.currDragImageDX = 0

        if imageCenterDY >= scaledImageHeight // 2 - app.height // 2:
            app.totalImageDY = scaledImageHeight // 2 - app.height // 2
            app.startDragY = mouseY
            app.currDragImageDY = 0
        if imageCenterDY <= -(scaledImageHeight // 2 - app.height // 2):
            app.totalImageDY = -(scaledImageHeight // 2 - app.height // 2)
            app.startDragY = mouseY
            app.currDragImageDY = 0


def moveMap(app, mouseX, mouseY):
        app.currDragMapDX = mouseX - app.startDragX
        app.currDragMapDY = mouseY - app.startDragY
        
        # The signs for app.currDragMap DX and DY are negative, unlike with the 
        # location image.
        # This is because we are dragging the box cropping the map, and not the
        # map itself. (Which reverses the sign)
        mapViewLeft = app.mapWidth // 2 - app.mapViewWidth // 2 - app.currDragMapDX - app.totalMapDX
        mapViewTop = app.mapHeight // 2 - app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY
        mapViewRight = app.mapWidth // 2 + app.mapViewWidth // 2 - app.currDragMapDX - app.totalMapDX
        mapViewBottom = app.mapHeight // 2 + app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY
        # Also, note that these values are with respect to the image of the map,
        # and not the canvas itself
        
        if mapViewLeft <= 0:
            mapViewLeft = 0
            mapViewRight = app.mapViewWidth
            app.totalMapDX = app.mapWidth // 2 - app.mapViewWidth // 2
            app.currDragMapDX = 0
            app.startDragX = mouseX
        if mapViewRight >= app.mapWidth - 0.8: 
            # the 0.8 is from map being a bit buggy when detecting the border
            mapViewLeft = app.mapWidth - app.mapViewWidth
            mapViewRight = app.mapWidth
            app.totalMapDX = -(app.mapWidth // 2 - app.mapViewWidth // 2)
            app.currDragMapDX = 0
            app.startDragX = mouseX

        
        if mapViewTop <= 0:
            mapViewTop = 0
            mapViewBottom = app.mapViewHeight
            app.totalMapDY = app.mapHeight // 2 - app.mapViewHeight // 2
            app.currDragMapDY = 0
            app.startDragY = mouseY
        if mapViewBottom >= app.mapHeight:
            mapViewTop = app.mapHeight - app.mapViewHeight
            mapViewBottom = app.mapHeight
            app.totalMapDY = -(app.mapHeight // 2 - app.mapViewHeight // 2)
            app.currDragMapDY = 0
            app.startDragY = mouseY

        view = (mapViewLeft, mapViewTop, mapViewRight, mapViewBottom)
        
        app.mapView = app.map.crop(view)

def guessing_onMouseRelease(app, mouseX, mouseY):
    
    # This updates the total distance by which the image has been dragged
    if app.isDraggingImage:
        app.totalImageDX += app.currDragImageDX
        app.totalImageDY += app.currDragImageDY
        app.currDragImageDX = 0
        app.currDragImageDY = 0
    else:
        app.totalMapDX += app.currDragMapDX
        app.totalMapDY += app.currDragMapDY
        app.currDragMapDX = 0
        app.currDragMapDY = 0

    app.isDraggingImage = False




def guessing_onKeyPress(app, key):
    if key == 'enter':
        if app.guessX != None and app.guessY != None: 
            setActiveScreen("postGuess")
    if key == 'z':
        if app.mapScale >= 0.3:
            zoomMap(app, 0.8)
    if key == 'x':
        if app.mapScale <= 2:
            zoomMap(app, 1.25)

    # if a guess has been entered, actually enter the guess
    # calculate the score/distance of the guess from the true location
    # add score to the user's current score
    # switch the screen to the post guess screen

################################################################################
#FIX THIS LATER
################################################################################
def zoomMap(app, scaleModifier):

    app.mapScale *= scaleModifier
    app.mapWidth = app.defaultMapWidth * app.mapScale
    app.mapHeight =  app.defaultMapHeight * app.mapScale
    
    app.totalMapDX = app.mapScale * (app.currDragMapDX + app.totalMapDX)
    app.totalMapDY = app.mapScale * (app.currDragMapDY + app.totalMapDY)

    mapViewLeft = app.mapWidth // 2 - app.mapViewWidth // 2  - app.currDragMapDX- app.totalMapDX
    mapViewTop = app.mapHeight // 2 - app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY
    mapViewRight = app.mapWidth // 2 + app.mapViewWidth // 2 - app.currDragMapDX- app.totalMapDX
    mapViewBottom = app.mapHeight // 2 + app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY

    mapCenterX = (mapViewLeft + mapViewRight) // 2
    mapCenterY = (mapViewTop + mapViewBottom) // 2

    if app.guessX != None and app.guessY != None:
        app.guessX = app.mapScale * app.guessX
        app.guessY = app.mapScale * app.guessY

    app.map = app.map.resize((int(app.mapWidth), int(app.mapHeight)))
    app.mapView = app.map.crop((mapViewLeft, mapViewTop, mapViewRight, 
                                mapViewBottom))

    # casting width and height to ints because of some cmu graphics bug

################################################################################
# Post Guess Screen
################################################################################

def postGuess_onScreenActivate(app):
    app.roundScore = calculateScore(app)
    app.totalScore += app.roundScore

def calculateScore(app):
    print(app.guessX, app.guessY, app.gameLocations[app.round].locX, app.gameLocations[app.round].locY)
    distance = getDistance(app.guessX, app.guessY, 
                        app.gameLocations[app.round].locX,
                        app.gameLocations[app.round].locY)
    
    size = (app.defaultMapWidth ** 2 + app.defaultMapHeight ** 2) ** 0.5
    roundScore = 5000 * (2.718) ** (-10 * distance / size)

    return int(roundScore)

def getDistance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


def postGuess_redrawAll(app):

    drawLabel(f'Your guess was ____ m away and you earned {app.roundScore} points', 
              app.width // 2, 50, size = 32)

    w = app.defaultMapWidth // 2
    h = app.defaultMapHeight // 2
    drawImage(CMUImage(app.map), app.width // 2, app.height // 2,
              width = w, height = h, align = 'center')
    
    # Like before, app.guessX and app.guessY are currently stored 
    # with respect to the top left corner of the map, not the canvas,
    # so we must do some math here
    guessX = app.guessX // 2 + (app.width // 2  - w/2)
    guessY = app.guessY // 2 + (app.height // 2 - h/2)
    print(guessX, guessY)
    drawCircle(guessX, guessY, 10, fill = 'red')
    
    #Same as above:
    trueX = app.gameLocations[app.round].locX // 2 + (app.width // 2  - w/2)
    trueY = app.gameLocations[app.round].locY // 2 + + (app.height // 2 - h/2)
    drawCircle(trueX, trueY, 10, fill = 'lime') # marks the actual location

    drawLine(guessX, guessY, trueX, trueY, dashes = True, fill = 'white')


def postGuess_onMousePress(app, mouseX, mouseY):
    app.round += 1
    if app.round > 5:
        pass


def main():
    runAppWithScreens(width = 1400, height = 860, 
                      initialScreen = 'starting')


main()