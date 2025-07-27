from cmu_graphics import *
from PIL import Image

def onAppStart(app):
    app.clickX = 0
    app.clickY = 0

def redrawAll(app):
    drawImage(CMUImage(Image.open("CMUMap.png")), 0, 0, width = 1362//2, height = 1050//2)
    drawCircle(app.clickX//2, app.clickY//2, 3, fill = 'red')
    drawLabel(f"Last click at {app.clickX, app.clickY}", app.width//2, 40, 
              size = 48, bold = True, fill = 'white')

def onMousePress(app, mouseX, mouseY):
    app.clickX = mouseX * 2
    app.clickY = mouseY * 2

def main():
    runApp(width = 1362//2, height = 1050//2)

main()

