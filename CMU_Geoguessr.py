from cmu_graphics import *
import os
import random
from PIL import Image
from getLocationImages import initializeLocations, Location

def onAppStart(app):
    app.backgroundGradient = gradient('indigo', 'darkSlateBlue', 
                                      start = 'bottom')

    # from my phone's camera
    app.defaultImageWidth = 4032
    app.defaultImageHeight = 3024

    app.allLocations = []
    initializeLocations(app)

        
    # Variables that pertain to a specific game
    app.gameDifficulty = None
    app.gameLocations = []
    app.round = 0 # indexes into app.gameLocations, with 5 total rounds (0 - 4)
    app.totalScore = 0
    app.roundScore = 0

    app.imageScale = 64/125
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
    app.mapViewWidth, app.mapViewHeight = 240, 240
    app.mapView = app.map.crop((app.mapWidth // 2 - app.mapViewWidth // 2, 
                                app.mapHeight // 2 - app.mapViewHeight // 2, 
                                app.mapWidth // 2 + app.mapViewWidth // 2, 
                                app.mapHeight // 2 + app.mapViewHeight // 2))
    app.mapOpacity = 100
    
    # coordinates of the top left of the cropped region on the canvas
    app.mapTopLeftX = app.width - app.mapViewWidth - 50
    app.mapTopLeftY = app.height - app.mapViewHeight - 50
    app.currDragMapDX = 0
    app.currDragMapDY = 0
    app.totalMapDX = 0
    app.totalMapDY = 0
    app.isDraggingMap = False

    # These variables are taken with respect to the map. Note that (0, 0) is 
    # the top left of the full map.)
    app.guessX = None
    app.guessY = None
    app.guessMeters = None

def resetGame(app):
    resetRound(app)
    app.totalScore = 0
    app.round = 0
    app.gameDifficulty = None

def resetRound(app):

    app.guessX = None
    app.guessY = None
    app.guessMeters = None

    app.mapWidth = app.defaultMapWidth
    app.mapHeight = app.defaultMapHeight
    app.map = app.map.resize((int(app.defaultMapWidth), int(app.defaultMapHeight)))
    app.mapView = app.map.crop((app.mapWidth // 2 - app.mapViewWidth // 2, 
                                app.mapHeight // 2 - app.mapViewHeight // 2, 
                                app.mapWidth // 2 + app.mapViewWidth // 2, 
                                app.mapHeight // 2 + app.mapViewHeight // 2))
    app.currDragMapDX = 0
    app.currDragMapDY = 0
    app.totalMapDX = 0
    app.totalMapDY = 0
    app.mapScale = 1
        
    app.imageScale = 64/125
    app.totalImageDX = 0
    app.totalImageDY = 0
    app.currDragImageDX = 0
    app.currDragImageDY = 0
    app.isDraggingImage = False
    app.isDraggingMap = False

################################################################################
# Starting Screen
################################################################################

def starting_redrawAll(app):
    drawStart(app)

def drawStart(app): # This will be used several times

    normalColor = rgb(151, 232, 81)
    hardColor = rgb(233, 69, 96)
    wordOutline = rgb(204, 48, 46)

    drawRect(0, 0, app.width, app.height, fill = app.backgroundGradient)
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
    numLocations = len(app.allLocations)

    while len(currLocations) < 5:
        locationIdx = random.randint(0, numLocations - 1)
        location = app.allLocations[locationIdx]
        
        if app.gameDifficulty == 'Normal':
            if 0 <= location.difficulty <= 1 and location not in currLocations:
                currLocations.append(location)
        elif app.gameDifficulty == 'Hard':
            if 1 <= location.difficulty <= 2 and location not in currLocations:
                currLocations.append(location)
    
    return currLocations


################################################################################
# Guessing Screen
################################################################################
    
def guessing_redrawAll(app):
    drawGuessing(app)

def drawGuessing(app): # This will be used several times
    imageCenterDX = app.currDragImageDX + app.totalImageDX
    imageCenterDY = app.currDragImageDY + app.totalImageDY
    
    app.gameLocations[app.round].draw(app, imageCenterDX, imageCenterDY, app.imageScale)
    drawImage(CMUImage(app.mapView), app.mapTopLeftX, app.mapTopLeftY, 
              opacity = app.mapOpacity)
    

    locationName = app.gameLocations[app.round].name
    bannerWidth = 16 * len(locationName) + 150
    drawRect(app.width - (bannerWidth + 50), 50, bannerWidth, 50,
             border = 'white', borderWidth = 4, fill = app.backgroundGradient)
    
    locationName = app.gameLocations[app.round]
    drawLabel(locationName.name, app.width - (bannerWidth + 25), 75, size = 24, 
              fill = 'white', align = 'left')
    drawLabel(f'Round {app.round + 1}/5', app.width - 125, 75, size = 24, 
              fill = 'white')

    if app.guessX != None and app.guessY != None: 
        
        mapViewLeft = app.mapWidth // 2 - app.mapViewWidth // 2 - app.currDragMapDX - app.totalMapDX
        mapViewTop = app.mapHeight // 2 - app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY

        # We get the location of the guess with respect to the left side of the 
        # viewable part of the map, and obtain the guess's location with respect
        # to the canvas by adding back app.mapTopLeftX and app.mapTopLeftY

        guessX = app.guessX - mapViewLeft + app.mapTopLeftX
        guessY = app.guessY - mapViewTop + app.mapTopLeftY
        if (app.mapTopLeftX + 8 <= guessX 
            <= app.mapTopLeftX + app.mapViewWidth - 8 and
            app.mapTopLeftY + 8 <= guessY 
            <= app.mapTopLeftY + app.mapViewHeight - 8):        
            drawCircle(guessX, guessY, 8, fill = 'red', 
                       opacity = app.mapOpacity)
    
    drawRect(app.mapTopLeftX, app.mapTopLeftY, app.mapViewWidth, 
             app.mapViewHeight, fill = None, border = 'white',
             borderWidth = 11, opacity = app.mapOpacity)

def guessing_onMouseMove(app, mouseX, mouseY):
    if (app.mapTopLeftX <= mouseX <= app.mapTopLeftX + app.mapViewWidth and
        app.mapTopLeftY <= mouseY <= app.mapTopLeftY + app.mapViewHeight):
        app.mapOpacity = 100
    else:
        app.mapOpacity = 45


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
        else:
            app.isDraggingMap = True
    if button == 2:
        if (app.mapTopLeftX <= mouseX <= app.mapTopLeftX + app.mapViewWidth and
            app.mapTopLeftY <= mouseY <= app.mapTopLeftY + app.mapViewHeight):
            mapViewLeft = app.mapWidth // 2 - app.mapViewWidth // 2 - app.totalMapDX
            mapViewTop = app.mapHeight // 2 - app.mapViewHeight // 2 - app.totalMapDY

            # setting the coordinates of app.guessX and app.guessY to be with
            # respect of the top left corner of the map, rather than the canvas
            app.guessX = (mouseX - app.mapTopLeftX) + mapViewLeft
            app.guessY = (mouseY - app.mapTopLeftY) + mapViewTop



def guessing_onMouseDrag(app, mouseX, mouseY):

    if app.isDraggingImage:
        moveImage(app, mouseX, mouseY)
    elif app.isDraggingMap: # the map is being dragged
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
    app.isDraggingMap = False



def guessing_onKeyPress(app, key):

    if key == 'enter':
        print(f'guessX: {app.guessX * 1/app.mapScale}, guessY: {app.guessY * 1/app.mapScale} (wrt to original map)')

    if key == 'space':
        if app.guessX != None and app.guessY != None: 
            setActiveScreen("postGuess")
    if key == 'z': # zoom out
        if app.mapOpacity != 100: # the mouse is not over the map
            if app.imageScale >= 64/125:
                zoomImage(app, 4/5)

                scaledImageWidth = app.defaultImageWidth * app.imageScale
                scaledImageHeight = app.defaultImageHeight * app.imageScale

                imageCenterDX = app.currDragImageDX + app.totalImageDX
                imageCenterDY = app.currDragImageDY + app.totalImageDY

                if imageCenterDX >= scaledImageWidth // 2 - app.width // 2:
                    app.totalImageDX = scaledImageWidth // 2 - app.width // 2
                if imageCenterDX <= -(scaledImageWidth // 2 - app.width // 2):
                    app.totalImageDX = -(scaledImageWidth // 2 - app.width // 2)
                if imageCenterDY >= scaledImageHeight // 2 - app.height // 2:
                    app.totalImageDY = scaledImageHeight // 2 - app.height // 2
                if imageCenterDY <= -(scaledImageHeight // 2 - app.height // 2):
                    app.totalImageDY = -(scaledImageHeight // 2 - app.height // 2)
        else: # the mouse is over the map
            if app.mapScale >= 64/125:
                zoomMap(app, 4/5)

    if key == 'x': # zoom in
        if app.mapOpacity != 100: # the mouse is not over the map
            if app.imageScale <= 125/64:
                zoomImage(app, 5/4)
        else: # the mouse is over the map
            if app.mapScale <= 125/64:
                zoomMap(app, 5/4)

def zoomImage(app, scaleModifier):
    app.imageScale *= scaleModifier
    app.currDragImageDX *= scaleModifier
    app.currDragImageDY *= scaleModifier
    app.totalImageDX *= scaleModifier
    app.totalImageDY *= scaleModifier

def zoomMap(app, scaleModifier):

    app.mapScale *= scaleModifier
    app.mapWidth = app.defaultMapWidth * app.mapScale
    app.mapHeight =  app.defaultMapHeight * app.mapScale
    
    app.totalMapDX = scaleModifier * (app.currDragMapDX + app.totalMapDX)
    app.totalMapDY = scaleModifier * (app.currDragMapDY + app.totalMapDY)

    mapViewLeft = app.mapWidth // 2 - app.mapViewWidth // 2  - app.currDragMapDX - app.totalMapDX
    mapViewTop = app.mapHeight // 2 - app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY
    mapViewRight = app.mapWidth // 2 + app.mapViewWidth // 2 - app.currDragMapDX - app.totalMapDX
    mapViewBottom = app.mapHeight // 2 + app.mapViewHeight // 2 - app.currDragMapDY - app.totalMapDY

    # This is buggy with the display of the guess. If we zoom out of the map near
    # the edge of the map, we have to shift the map back into the view because
    # otherwise, there will be empty space. However, the guess won't be shifted
    # properly. To fix this, (see below)
    if mapViewLeft <= 0:
        mapViewLeft = 0
        mapViewRight = app.mapViewWidth
    if mapViewTop <= 0:
        mapViewTop = 0
        mapViewBottom = app.mapViewHeight
    if mapViewRight >= app.mapWidth:
        mapViewRight = app.mapWidth
        mapViewLeft = app.mapWidth - app.mapViewWidth
    if mapViewBottom >= app.mapHeight:
        mapViewBottom = app.mapHeight
        mapViewTop = app.mapHeight - app.mapViewWidth


    if app.guessX != None and app.guessY != None:
        app.guessX = scaleModifier * app.guessX
        app.guessY = scaleModifier * app.guessY
    
    # we just call moveMap to update the cropped map, which fixes everything.
    app.startDragX = 0
    app.startDragY = 0
    moveMap(app, 0, 0)

    app.map = app.map.resize((int(app.mapWidth), int(app.mapHeight)))
    app.mapView = app.map.crop((mapViewLeft, mapViewTop, mapViewRight, 
                                mapViewBottom))



################################################################################
# Post Guess Screen
################################################################################

def postGuess_onScreenActivate(app):
    app.roundScore = calculateScore(app)
    # app.guessX and app.guessY have to be scaled because the user may have
    # zoomed into the map
    app.guessMeters = int(getDistance(app.guessX * 1/app.mapScale, 
                                      app.guessY * 1/app.mapScale, 
                                      app.gameLocations[app.round].locX,
                                      app.gameLocations[app.round].locY) / 1.48)
    app.totalScore += app.roundScore

def calculateScore(app):
    distance = getDistance(app.guessX * 1/app.mapScale, 
                           app.guessY * 1/app.mapScale, 
                           app.gameLocations[app.round].locX,
                           app.gameLocations[app.round].locY)
    
    # 1362 pixels width --> 924 meters
    # 1050 pixels height --> 699 meters
    # approximately 1.48 pixels per meter

    size = (app.defaultMapWidth ** 2 + app.defaultMapHeight ** 2) ** 0.5
    roundScore = 5000 * (2.718) ** (-10 * distance / size)

    return int(roundScore)

def getDistance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


def postGuess_redrawAll(app):
    # postGuess_redrawAll gets called after the next round is started in 
    # postGuess_onMousePress, so we just use a conditional to make sure 
    # redrawAll runs as desired. (It either shows the guess, or the next round)

    # Note that we show the next round in this redrawAll in addition to in
    # guess_redrawAll because guess_redrawAll will only be called after
    # a controller is also called. If we do not show the next 'guessing'
    # screen here, there will be a delay.
    if app.guessX != None and app.guessY != None:

        drawRect(0, 0, app.width, app.height, fill = app.backgroundGradient)

        drawLabel(f'Round {app.round + 1}: Your guess was {app.guessMeters} m away from the correct location',
                app.width // 2, 75, size = 32, fill = 'white')
        drawLabel(f'You earned {app.roundScore} points', app.width // 2, 125, 
                size = 16, fill = 'white')

        w = app.defaultMapWidth // 2
        h = app.defaultMapHeight // 2
        drawImage(CMUImage(app.map), app.width // 2, app.height // 2,
                width = w, height = h, align = 'center')
        
        # Like before, app.guessX and app.guessY are currently stored 
        # with respect to the top left corner of the map, not the canvas,
        # so we must do some math here
        guessX = (app.guessX * 1/app.mapScale) // 2 + (app.width // 2  - w/2)
        guessY = (app.guessY * 1/app.mapScale) // 2 + (app.height // 2 - h/2)

        #Same as above:
        trueX = app.gameLocations[app.round].locX // 2 + (app.width // 2  - w/2)
        trueY = app.gameLocations[app.round].locY // 2 + + (app.height // 2 - h/2)
        drawLine(guessX, guessY, trueX, trueY, dashes = True, fill = 'white')
        drawCircle(guessX, guessY, 10, fill = 'red')
        drawCircle(trueX, trueY, 10, fill = 'lime') # marks the actual location

        green50 = rgb(151, 232, 81)
        drawRect(app.width // 2, 775, 200, 100, fill = green50,
                 align = 'center')
        if app.round < 4:
            drawLabel("Next Round", app.width // 2, 775, size = 24, 
                      fill = 'white')
        else:
            drawLabel('Finish Game', app.width // 2, 775, size = 24, 
                      fill = 'white')

    else:
        if app.round < 5:
            drawGuessing(app)
            
        else: # draw the end screen
            drawEnd(app)


def postGuess_onMousePress(app, mouseX, mouseY):
    if (app.width // 2 - 100 <= mouseX <= app.width // 2 + 100
        and 675 <= mouseY <= 825):
        app.round += 1
        resetRound(app) # Note that this sets app.guessX and app.guessY to None
        
        if app.round > 4:
            setActiveScreen('endGame')
        else:
            setActiveScreen('guessing')

################################################################################
# End of Game Screen
################################################################################

# All the work for drawing the end of game screen is done by the previous screen

# However, we must draw the starting screen here after the user starts a new
# game because endGame_redrawAll is called after any mouse press

def drawEnd(app):
    drawRect(0, 0, app.width, app.height, fill = app.backgroundGradient)
    drawLabel(f'You won {app.totalScore}/25000 points this game!', 
                app.width // 2, 200, size = 72, fill = 'white')

    green50 = rgb(151, 232, 81)
    drawRect(app.width // 2, app.height // 2, 200, 100, 
                fill = green50, align = 'center')
    drawLabel(f'Play Again', app.width // 2, app.height // 2, 
                size = 24, fill = 'white')

def endGame_redrawAll(app):
    drawEnd(app)
    if app.round == 0:
        drawStart(app)


def endGame_onMousePress(app, mouseX, mouseY):
    if (app.width // 2 - 100 <= mouseX <= app.width // 2 + 100 and
        app.height // 2 - 50 <= mouseY <= app.height // 2 + 50):
        resetGame(app)

        setActiveScreen('starting')
        

def main():
    runAppWithScreens(width = 1400, height = 860, 
                      initialScreen = 'starting')


main()