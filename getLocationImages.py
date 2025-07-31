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
    app.allLocations.append(Location("", 939, 811, 1, "Locations/donner2.jpg"))
    app.allLocations.append(Location("", 828, 810, 0, "Locations/donner3.jpg"))
    app.allLocations.append(Location("", 932, 740, 2, "Locations/donner4.jpg"))

    app.allLocations.append(Location("", 1078, 682, 1, "Locations/field1.jpg"))
    app.allLocations.append(Location("", 1074, 634, 1, "Locations/field2.jpg"))

    app.allLocations.append(Location("", 1136, 472, 1, "Locations/forbes1.jpg"))
    app.allLocations.append(Location("", 1060, 426, 1, "Locations/forbes2.jpg"))
    app.allLocations.append(Location("", 550, 406, 1, "Locations/forbes3.jpg"))
    app.allLocations.append(Location("", 506, 420, 1, "Locations/forbes4.jpg"))
    app.allLocations.append(Location("", 296, 336, 0, "Locations/forbes5.jpg"))
    app.allLocations.append(Location("", 304, 336, 1, "Locations/forbes6.jpg"))
    app.allLocations.append(Location("", 232, 346, 1, "Locations/forbes7.jpg"))
    app.allLocations.append(Location("", 234, 388, 1, "Locations/forbes8.jpg"))
    app.allLocations.append(Location("", 192, 444, 2, "Locations/forbes9.jpg"))
    app.allLocations.append(Location("", 880, 382, 0, "Locations/garage3.jpg"))

    app.allLocations.append(Location("", 528, 552, 0, "Locations/ghc1.jpg"))
    app.allLocations.append(Location("", 456, 526, 0, "Locations/ghc2.jpg"))
    app.allLocations.append(Location("", 402, 524, 1, "Locations/ghc3.jpg"))
    app.allLocations.append(Location("", 426, 512, 2, "Locations/ghc4.jpg"))
    app.allLocations.append(Location("", 446, 492, 1, "Locations/ghc5.jpg"))
    app.allLocations.append(Location("", 454, 512, 1, "Locations/ghc6.jpg"))
    app.allLocations.append(Location("", 454, 476, 1, "Locations/ghc7.jpg"))
    app.allLocations.append(Location("", 402, 510, 2, "Locations/ghc8.jpg"))
    app.allLocations.append(Location("Have You Gone to OH?", 438, 492, 1, "Locations/ghc9.jpg"))
    app.allLocations.append(Location("", 374, 524, 1, "Locations/ghc10.jpg"))
    app.allLocations.append(Location("", 342, 532, 2, "Locations/ghc11.jpg"))
    app.allLocations.append(Location("", 310, 508, 0, "Locations/ghc12.jpg"))
    app.allLocations.append(Location("", 298, 444, 1, "Locations/ghc13.jpg"))
    app.allLocations.append(Location("", 344, 474, 0, "Locations/ghc14.jpg"))
    app.allLocations.append(Location("", 410, 418, 0, "Locations/ghc15.jpg"))
    app.allLocations.append(Location("", 406, 460, 1, "Locations/ghc16.jpg"))
    app.allLocations.append(Location("", 378, 510, 2, "Locations/ghc17.jpg"))
    app.allLocations.append(Location("", 390, 524, 2, "Locations/ghc18.jpg"))
    app.allLocations.append(Location("Where Wall You Guess?", 396, 392, 2, "Locations/ghc19.jpg"))
    app.allLocations.append(Location("", 432, 430, 0, "Locations/ghc20.jpg"))

    app.allLocations.append(Location("", 246, 706, 0, "Locations/hh1.jpg"))
    app.allLocations.append(Location("", 208, 696, 2, "Locations/hh2.jpg"))
    app.allLocations.append(Location("", 158, 684, 0, "Locations/hh3.jpg"))
    app.allLocations.append(Location("", 138, 690, 2, "Locations/hh4.jpg"))
    app.allLocations.append(Location("", 130, 676, 2, "Locations/hh5.jpg"))

    app.allLocations.append(Location("", 222, 504, 1, "Locations/hhdr1.jpg"))
    app.allLocations.append(Location("", 206, 572, 1, "Locations/hhdr2.jpg"))
    app.allLocations.append(Location("", 174, 590, 1, "Locations/hhdr3.jpg"))
    app.allLocations.append(Location("", 124, 644, 1, "Locations/hhdr4.jpg"))

    app.allLocations.append(Location("Circle", 576, 862, 2, "Locations/hunt1.jpg"))
    app.allLocations.append(Location("", 555, 862, 0, "Locations/hunt2.jpg"))
    app.allLocations.append(Location("", 522, 885, 2, "Locations/hunt3.jpg"))
    app.allLocations.append(Location("", 516, 897, 1, "Locations/hunt4.jpg"))
    app.allLocations.append(Location("", 538, 903, 1, "Locations/hunt5.jpg"))
    app.allLocations.append(Location("", 561, 909, 1, "Locations/hunt6.jpg"))
    app.allLocations.append(Location("", 546, 879, 0, "Locations/hunt7.jpg"))
    app.allLocations.append(Location("", 534, 885, 1, "Locations/hunt8.jpg"))
    app.allLocations.append(Location("", 520, 891, 1, "Locations/hunt9.jpg"))
    app.allLocations.append(Location("", 532, 871, 1, "Locations/hunt10.jpg"))

    app.allLocations.append(Location("Numbers", 712, 848, 1, "Locations/kraus1.jpg"))
    app.allLocations.append(Location("Yo that's deep", 691, 858, 1, "Locations/kraus2.jpg"))
    app.allLocations.append(Location("PROHIBITED!", 681, 849, 2, "Locations/kraus3.jpg")) # check this one
    app.allLocations.append(Location("Posner Center", 718, 789, 1, "Locations/kraus4.jpg"))

    app.allLocations.append(Location("", 342, 708, 0, "Locations/mall1.jpg"))
    app.allLocations.append(Location("Some Nice Flowers", 360, 712, 0, "Locations/mall2.jpg"))
    app.allLocations.append(Location("", 456, 733, 1, "Locations/mall3.jpg"))
    # app.allLocations.append(Location("Three Balls", 472, 733, 1, "Locations/mall4.jpg")) Image is the wrong size... oops
    app.allLocations.append(Location("", 270, 748, 1, "Locations/mall5.jpg"))
    app.allLocations.append(Location("Does This Tickle Your Crane(ium)", 469, 795, 0, "Locations/mall6.jpg"))




    app.allLocations.append(Location("Evacuation", 413, 170, 2, "Locations/tepper1.jpg"))
    app.allLocations.append(Location("An Enthralling Bulletin Board", 360, 216, 2, "Locations/tepper2.jpg"))
    app.allLocations.append(Location("Big Glass Window", 364, 214, 0, "Locations/tepper3.jpg"))
    app.allLocations.append(Location("Cathedral View", 332, 232, 1, "Locations/tepper4.jpg"))
    