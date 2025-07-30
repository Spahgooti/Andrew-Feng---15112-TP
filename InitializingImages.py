from cmu_graphics import *
from PIL import Image

def onAppStart(app):
    app.clickX = 0
    app.clickY = 0

def redrawAll(app):
    drawImage(CMUImage(Image.open("CMUMap.png")), 0, 0, width = 1362//1.5, height = 1050//1.5)
    drawCircle(app.clickX//1.5, app.clickY//1.5, 3, fill = 'red')
    drawLabel(f"Last click at {app.clickX, app.clickY}", app.width//2, 40, 
              size = 48, bold = True, fill = 'white')

def onMousePress(app, mouseX, mouseY):
    app.clickX = mouseX * 1.5
    app.clickY = mouseY * 1.5

def main():
    runApp(width = int(1362//1.5), height = int(1050//1.5))

main()

