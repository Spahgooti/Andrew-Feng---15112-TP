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
        self.image = CMUImage(self.image)

    def draw(self, app, dx, dy, scale):
        
        imageWidth, imageHeight = getImageSize(self.image)
        newWidth, newHeight = int(imageWidth * scale), int(imageHeight * scale)

        imageCenterX, imageCenterY = app.width//2 + dx, app.height//2 + dy
        drawImage(self.image, imageCenterX, imageCenterY, align = 'center', 
                  width = newWidth, height = newHeight)

def initializeLocations(app):
    app.allLocations.append(Location("Flowers and a Bench", 490, 856, 0, "Locations/baker1.jpg"))
    app.allLocations.append(Location("Brick Ceiling", 466, 854, 2, "Locations/baker2.jpg"))
    app.allLocations.append(Location("Glass Pyramid", 434, 858, 1, "Locations/baker3.jpg"))
    app.allLocations.append(Location("Long Hall", 440, 848, 0, "Locations/baker4.jpg"))
    app.allLocations.append(Location("Sofas", 458, 848, 2, "Locations/baker5.jpg"))

    app.allLocations.append(Location("Sculptures 1", 618, 788, 1, "Locations/cfa1.jpg"))
    app.allLocations.append(Location("Vaulted Ceiling", 630, 814, 1, "Locations/cfa2.jpg"))
    app.allLocations.append(Location("Sculptures 2", 612, 822, 1, "Locations/cfa3.jpg"))

    app.allLocations.append(Location("", 686, 576, 0, "Locations/cuc1.jpg"))
    app.allLocations.append(Location("", 708, 592, 0, "Locations/cuc2.jpg"))
    app.allLocations.append(Location("", 734, 542, 0, "Locations/cuc3.jpg"))
    app.allLocations.append(Location("", 734, 542, 0, "Locations/cuc4.jpg"))
    app.allLocations.append(Location("", 762, 524, 1, "Locations/cuc5.jpg"))
    app.allLocations.append(Location("", 714, 494, 1, "Locations/cuc6.jpg"))
    app.allLocations.append(Location("", 736, 514, 1, "Locations/cuc7.jpg"))
    app.allLocations.append(Location("", 802, 538, 0, "Locations/cuc8.jpg"))
    app.allLocations.append(Location("", 830, 546, 0, "Locations/cuc9.jpg"))
    app.allLocations.append(Location("Noodles, Don't Noodles", 770, 530, 0, "Locations/cuc10.jpg"))
    app.allLocations.append(Location("", 752, 528, 0, "Locations/cuc11.jpg"))
    app.allLocations.append(Location("", 818, 394, 1, "Locations/cuc12.jpg"))
    app.allLocations.append(Location("", 752, 380, 0, "Locations/cuc13.jpg"))

    app.allLocations.append(Location("", 540, 702, 0, "Locations/cut1.jpg"))
    app.allLocations.append(Location("", 568, 666, 0, "Locations/cut2.jpg"))
    app.allLocations.append(Location("", 658, 622, 0, "Locations/cut3.jpg"))
    app.allLocations.append(Location("", 644, 384, 0, "Locations/cut4.jpg"))
    app.allLocations.append(Location("", 612, 394, 1, "Locations/cut5.jpg"))
    app.allLocations.append(Location("", 610, 408, 0, "Locations/cut6.jpg"))
    app.allLocations.append(Location("", 542, 666, 1, "Locations/cut7.jpg"))
    app.allLocations.append(Location("Stumped?", 544, 662, 1, "Locations/cut8.jpg"))
    app.allLocations.append(Location("", 558, 614, 1, "Locations/cut9.jpg"))
    app.allLocations.append(Location("", 570, 568, 0, "Locations/cut10.jpg"))
    app.allLocations.append(Location("", 556, 548, 1, "Locations/cut11.jpg"))
    app.allLocations.append(Location("", 550, 560, 2, "Locations/cut12.jpg"))

    app.allLocations.append(Location("", 532, 386, 2, "Locations/cyert1.jpg"))
    app.allLocations.append(Location("", 486, 366, 2, "Locations/cyert2.jpg"))

    app.allLocations.append(Location("", 378, 664, 2, "Locations/doherty1.jpg"))
    app.allLocations.append(Location("", 446, 708, 1, "Locations/doherty2.jpg"))
    app.allLocations.append(Location("", 448, 708, 1, "Locations/doherty3.jpg"))
    app.allLocations.append(Location("", 500, 690, 0, "Locations/doherty4.jpg"))
    app.allLocations.append(Location("", 490, 604, 1, "Locations/doherty5.jpg"))
    app.allLocations.append(Location("", 510, 634, 2, "Locations/doherty6.jpg"))

    app.allLocations.append(Location("", 1022, 786, 1, "Locations/donner1.jpg"))
    app.allLocations.append(Location("", 834, 780, 1, "Locations/donner2.jpg"))
    app.allLocations.append(Location("", 828, 810, 0, "Locations/donner3.jpg"))
    app.allLocations.append(Location("", 932, 740, 2, "Locations/donner4.jpg"))

    app.allLocations.append(Location("", 1078, 682, 1, "Locations/field1.jpg"))
    app.allLocations.append(Location("", 1074, 634, 1, "Locations/field2.jpg"))

    app.allLocations.append(Location("Evacuation", 413, 170, 2, "Locations/tepper1.jpg"))
    app.allLocations.append(Location("An Enthralling Bulletin Board", 360, 216, 2, "Locations/tepper2.jpg"))
    app.allLocations.append(Location("Big Glass Window", 364, 214, 0, "Locations/tepper3.jpg"))
    app.allLocations.append(Location("Cathedral View", 332, 232, 1, "Locations/tepper4.jpg"))
    app.allLocations.append(Location("Numbers", 712, 848, 1, "Locations/kraus1.jpg"))