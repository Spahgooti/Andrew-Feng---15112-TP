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

    app.allLocations.append(Location("Sculptures", 618, 788, 1, "Locations/cfa1.jpg"))
    app.allLocations.append(Location("Vaulted Ceiling", 630, 814, 1, "Locations/cfa2.jpg"))
    app.allLocations.append(Location("Sculptures", 612, 822, 1, "Locations/cfa3.jpg"))

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
    app.allLocations.append(Location("Just a Really Nice Sunset", 370, 685, 0, "Locations/doherty7.jpg"))

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

    app.allLocations.append(Location("", 712, 848, 1, "Locations/kraus1.jpg"))
    app.allLocations.append(Location("Yo that's deep", 693, 865, 1, "Locations/kraus2.jpg"))
    app.allLocations.append(Location("", 681, 849, 2, "Locations/kraus3.jpg")) # check this one
    app.allLocations.append(Location("", 718, 789, 1, "Locations/kraus4.jpg"))

    app.allLocations.append(Location("", 342, 708, 0, "Locations/mall1.jpg"))
    app.allLocations.append(Location("Some Nice Flowers", 360, 712, 0, "Locations/mall2.jpg"))
    app.allLocations.append(Location("", 456, 733, 1, "Locations/mall3.jpg"))
    # app.allLocations.append(Location("Three Balls", 472, 733, 1, "Locations/mall4.jpg")) Image is the wrong size... oops
    app.allLocations.append(Location("", 270, 748, 1, "Locations/mall5.jpg"))
    app.allLocations.append(Location("Does This Tickle Your Crane(ium)", 469, 795, 0, "Locations/mall6.jpg"))

    app.allLocations.append(Location("", 817, 777, 0, "Locations/mm1.jpg"))
    app.allLocations.append(Location("", 846, 756, 2, "Locations/mm2.jpg"))
    app.allLocations.append(Location('''"Surely Nobody Gets This"''', 843, 759, 2, "Locations/mm3.jpg"))
    app.allLocations.append(Location("", 822, 744, 1, "Locations/mm4.jpg"))

    app.allLocations.append(Location("", 364, 816, 1, "Locations/porter1.jpg"))
    app.allLocations.append(Location("", 241, 790, 1, "Locations/porter2.jpg"))
    app.allLocations.append(Location("", 226, 823, 1, "Locations/porter3.jpg"))
    app.allLocations.append(Location("", 216, 835, 0, "Locations/porter4.jpg"))
    app.allLocations.append(Location("It's Not Just a Boulder", 168, 828, 2, "Locations/porter5.jpg"))

    app.allLocations.append(Location("", 751, 924, 2, "Locations/posner1.jpg"))
    app.allLocations.append(Location("", 730, 979, 0, "Locations/posner2.jpg"))
    app.allLocations.append(Location("", 760, 898, 2, "Locations/posner3.jpg"))
    app.allLocations.append(Location("", 762, 888, 0, "Locations/posner4.jpg"))
    app.allLocations.append(Location("", 760, 786, 0, "Locations/posner5.jpg"))
    app.allLocations.append(Location("Two Chairs", 760, 819, 2, "Locations/posner6.jpg"))
    app.allLocations.append(Location("", 760, 826, 0, "Locations/posner7.jpg"))
    app.allLocations.append(Location("", 757, 850, 1, "Locations/posner8.jpg"))
    app.allLocations.append(Location("", 730, 873, 2, "Locations/posner9.jpg"))
    app.allLocations.append(Location("", 741, 918, 2, "Locations/posner10.jpg"))
    app.allLocations.append(Location("", 741, 916, 2, "Locations/posner11.jpg"))
    app.allLocations.append(Location("", 724, 933, 1, "Locations/posner12.jpg"))
    app.allLocations.append(Location("", 679, 915, 2, "Locations/posner13.jpg"))
    app.allLocations.append(Location("", 649, 937, 1, "Locations/posner14.jpg"))
    app.allLocations.append(Location("", 660, 945, 2, "Locations/posner15.jpg"))
    app.allLocations.append(Location("", 741, 817, 1, "Locations/posner16.jpg"))
    app.allLocations.append(Location("", 735, 843, 2, "Locations/posner17.jpg"))
    app.allLocations.append(Location("", 733, 856, 1, "Locations/posner18.jpg"))
    app.allLocations.append(Location("", 732, 886, 2, "Locations/posner19.jpg"))
    app.allLocations.append(Location("", 720, 916, 2, "Locations/posner20.jpg"))

    app.allLocations.append(Location("", 718, 603, 0, "Locations/resnik1.jpg"))
    app.allLocations.append(Location("", 814, 628, 0, "Locations/resnik2.jpg"))
    app.allLocations.append(Location("", 891, 660, 1, "Locations/resnik3.jpg"))
    app.allLocations.append(Location("", 951, 616, 0, "Locations/resnik4.jpg"))
    app.allLocations.append(Location("", 1039, 694, 0, "Locations/resnik5.jpg"))

    app.allLocations.append(Location("", 103, 810, 0, "Locations/scaife1.jpg"))
    app.allLocations.append(Location("", 30, 817, 2, "Locations/scaife2.jpg"))
    app.allLocations.append(Location("", 57, 733, 2, "Locations/scaife3.jpg"))
    app.allLocations.append(Location("", 76, 742, 2, "Locations/scaife4.jpg"))
    app.allLocations.append(Location("", 100, 783, 1, "Locations/scaife5.jpg"))
    app.allLocations.append(Location('''"Have I been here before?"''', 54, 804, 0, "Locations/scaife6.jpg"))
    app.allLocations.append(Location("", 63, 789, 1, "Locations/scaife7.jpg"))
    app.allLocations.append(Location("", 70, 799, 1, "Locations/scaife8.jpg"))
    app.allLocations.append(Location("", 117, 790, 2, "Locations/scaife9.jpg"))
    app.allLocations.append(Location("", 135, 736, 2, "Locations/scaife10.jpg"))
    app.allLocations.append(Location("", 144, 715, 1, "Locations/scaife11.jpg"))
    app.allLocations.append(Location("", 174, 724, 1, "Locations/scaife12.jpg"))
    app.allLocations.append(Location("", 93, 730, 2, "Locations/scaife13.jpg"))
    app.allLocations.append(Location("A Nice Place", 99, 618, 1, "Locations/scaife14.jpg"))
    app.allLocations.append(Location("The Museum!", 108, 618, 1, "Locations/scaife15.jpg"))
    app.allLocations.append(Location("Terrace", 97, 754, 0, "Locations/scaife16.jpg"))

    app.allLocations.append(Location("", 136, 619, 1, "Locations/scott1.jpg"))
    app.allLocations.append(Location("", 168, 646, 2, "Locations/scott2.jpg"))
    app.allLocations.append(Location("Criminal Act", 144, 594, 1, "Locations/scott3.jpg"))
    app.allLocations.append(Location("", 181, 624, 1, "Locations/scott4.jpg"))

    app.allLocations.append(Location("", 574, 189, 2, "Locations/stackd1.jpg"))
    app.allLocations.append(Location('''"Get a Picture of the Sand Bro"''', 571, 196, 2, "Locations/stackd2.jpg"))
    app.allLocations.append(Location("D", 583, 220, 1, "Locations/stackd3.jpg"))
    app.allLocations.append(Location("Reflections", 564, 217, 2, "Locations/stackd4.jpg"))

    app.allLocations.append(Location("", 486, 552, 1, "Locations/steps1.jpg"))
    app.allLocations.append(Location("", 495, 583, 1, "Locations/steps2.jpg"))
    app.allLocations.append(Location("", 508, 618, 1, "Locations/steps3.jpg"))

    app.allLocations.append(Location("", 717, 735, 0, "Locations/tennis1.jpg"))
    app.allLocations.append(Location("", 670, 721, 0, "Locations/tennis2.jpg"))

    app.allLocations.append(Location("", 413, 170, 2, "Locations/tepper1.jpg"))
    app.allLocations.append(Location("An Enthralling Bulletin Board", 360, 216, 2, "Locations/tepper2.jpg"))
    app.allLocations.append(Location("Big Glass Window", 364, 214, 0, "Locations/tepper3.jpg"))
    app.allLocations.append(Location("Cathedral View", 332, 232, 1, "Locations/tepper4.jpg"))
    app.allLocations.append(Location("", 496, 214, 2, "Locations/tepper5.jpg"))
    app.allLocations.append(Location("", 462, 226, 0, "Locations/tepper6.jpg"))
    app.allLocations.append(Location("", 364, 274, 0, "Locations/tepper7.jpg"))

    app.allLocations.append(Location("Concrete Halls", 313, 648, 0, "Locations/wean1.jpg"))
    app.allLocations.append(Location("", 253, 679, 0, "Locations/wean2.jpg"))
    app.allLocations.append(Location("", 267, 636, 0, "Locations/wean3.jpg"))
    app.allLocations.append(Location("", 288, 615, 1, "Locations/wean4.jpg"))
    app.allLocations.append(Location("", 288, 592, 0, "Locations/wean5.jpg"))
    app.allLocations.append(Location("", 271, 628, 1, "Locations/wean6.jpg"))
    app.allLocations.append(Location("", 321, 655, 1, "Locations/wean7.jpg"))
    app.allLocations.append(Location("", 189, 615, 2, "Locations/wean8.jpg"))
    app.allLocations.append(Location("", 330, 661, 1, "Locations/wean9.jpg"))
    app.allLocations.append(Location("", 369, 661, 1, "Locations/wean10.jpg"))
    app.allLocations.append(Location("", 269, 631, 1, "Locations/wean11.jpg"))
    app.allLocations.append(Location("", 291, 619, 2, "Locations/wean12.jpg"))
    app.allLocations.append(Location("", 364, 640, 2, "Locations/wean13.jpg"))