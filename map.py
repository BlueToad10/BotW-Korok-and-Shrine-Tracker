import pygame, os, sys, random
from pygame.locals import *

WINDOWSIZEX = int(720)#720+40#2880/4
WINDOWSIZEY = int(2400/4)#600#/15=40
WINDOWSIZE = (WINDOWSIZEX+40, WINDOWSIZEY)
Version = "Version 1.2"
windowName = "Korok and Shrine Map " + Version
FPS=60
mouseposx=mouseposy=0
print("setting values")
mapColours=[(127,0,0),(153,153,153),(0,127,127),(0,255,0),(48,0,109),(255,133,1),(136,73,14),(0,0,207),(0,68,0),(70,70,70),(255,255,83),(191,123,99),(205,55,198),(255,11,11),(97,0,88)]

PlateauSeeds  =PlateauSeedsMax  =18
HyruleSeeds   =HyruleSeedsMax   =114#25 for hyrule castle#89+25=114 total
DualingSeeds  =DualingSeedsMax  =59
HatenoSeeds   =HatenoSeedsMax   =66
LanayruSeeds  =LanayruSeedsMax  =62
GerudoSeeds   =GerudoSeedsMax   =68
HighlandsSeeds=HighlandsSeedsMax=36
LakeSeeds     =LakeSeedsMax     =92
FaronSeeds    =FaronSeedsMax    =58
RidgelandSeeds=RidgelandSeedsMax=80
TabanthaSeeds =TabanthaSeedsMax =37
HebraSeeds    =HebraSeedsMax    =73
ForestSeeds   =ForestSeedsMax   =35
MountainSeeds =MountainSeedsMax =45
AkalaSeeds    =AkalaSeedsMax    =57
seedCounters=[PlateauSeeds, HyruleSeeds, DualingSeeds, HatenoSeeds, LanayruSeeds, GerudoSeeds, HighlandsSeeds, LakeSeeds, FaronSeeds, RidgelandSeeds, TabanthaSeeds, HebraSeeds, ForestSeeds, MountainSeeds, AkalaSeeds]
seedCountersMax=[PlateauSeedsMax, HyruleSeedsMax, DualingSeedsMax, HatenoSeedsMax, LanayruSeedsMax, GerudoSeedsMax, HighlandsSeedsMax, LakeSeedsMax, FaronSeedsMax, RidgelandSeedsMax, TabanthaSeedsMax, HebraSeedsMax, ForestSeedsMax, MountainSeedsMax, AkalaSeedsMax]

#57 89 59 45 58 18 36 66 73 25 92 62 80 37 68 35
#900
totalSeeds = PlateauSeeds+HyruleSeeds+DualingSeeds+HatenoSeeds+LanayruSeeds+GerudoSeeds+HighlandsSeeds+LakeSeeds+FaronSeeds+RidgelandSeeds+TabanthaSeeds+HebraSeeds+ForestSeeds+MountainSeeds+AkalaSeeds
#print("Korok Seeds:" + str(totalSeeds))

PlateauShrines  =PlateauShrinesMax  =4
HyruleShrines   =HyruleShrinesMax   =8
DualingShrines  =DualingShrinesMax  =9
HatenoShrines   =HatenoShrinesMax   =7
LanayruShrines  =LanayruShrinesMax  =9#3 dlc
GerudoShrines   =GerudoShrinesMax   =12#3 dlc
HighlandsShrines=HighlandsShrinesMax=6
LakeShrines     =LakeShrinesMax     =6
FaronShrines    =FaronShrinesMax    =8
RidgelandShrines=RidgelandShrinesMax=7#1 dlc
TabanthaShrines =TabanthaShrinesMax =6#1 dlc
HebraShrines    =HebraShrinesMax    =13#1 dlc
ForestShrines   =ForestShrinesMax   =8
MountainShrines =MountainShrinesMax =9#3 dlc
AkalaShrines    =AkalaShrinesMax    =8
shrineCounters=[PlateauShrines, HyruleShrines, DualingShrines, HatenoShrines, LanayruShrines, GerudoShrines, HighlandsShrines, LakeShrines, FaronShrines, RidgelandShrines, TabanthaShrines, HebraShrines, ForestShrines, MountainShrines, AkalaShrines]
shrineCountersMax=[PlateauShrinesMax, HyruleShrinesMax, DualingShrinesMax, HatenoShrinesMax, LanayruShrinesMax, GerudoShrinesMax, HighlandsShrinesMax, LakeShrinesMax, FaronShrinesMax, RidgelandShrinesMax, TabanthaShrinesMax, HebraShrinesMax, ForestShrinesMax, MountainShrinesMax, AkalaShrinesMax]

#4 9 7 8 9 9 12 6 6 7 6 8 8 8 13 DLC16
#120
#print("Shrines:" + str(PlateauShrines+HyruleShrines+DualingShrines+HatenoShrines+LanayruShrines+GerudoShrines+HighlandsShrines+LakeShrines+FaronShrines+RidgelandShrines+TabanthaShrines+HebraShrines+ForestShrines+MountainShrines+AkalaShrines))

AreaNames={
    "shrines" : "PlateauShrines HyruleShrines DualingShrines HatenoShrines LanayruShrines GerudoShrines HighlandsShrines LakeShrines FaronShrines RidgelandShrines TabanthaShrines HebraShrines ForestShrines MountainShrines AkalaShrines",
    "seeds" : "PlateauSeeds HyruleSeeds DualingSeeds HatenoSeeds LanayruSeeds GerudoSeeds HighlandsSeeds LakeSeeds FaronSeeds RidgelandSeeds TabanthaSeeds HebraSeeds ForestSeeds MountainSeeds AkalaSeeds"
}
korokSeeds=0
shrines=0
def collectableTotals():
    global korokSeeds, shrines
    shrines=0
    for object in shrineCounters:
        shrines+=object
    korokSeeds=0
    for object in seedCounters:
        korokSeeds+=object

def load():
    global seedCounters, shrineCounters
    f = open("assets/DATA.txt", "r")
    areaNumber=0
    source = f.read().splitlines()
    for object in AreaNames["seeds"].split(" "):
        for line in source:
            if line.startswith(object):
                splitline = line.split(" ")
                seedCounters[areaNumber] = int(splitline[1])
                
        areaNumber += 1
    areaNumber=0
    #print("Korok Seeds:" + str(korokSeeds) + "/900")
    for object in AreaNames["shrines"].split(" "):
        for line in source:
            splitline = line.split(" ")
            if splitline[0] == object:
                shrineCounters[areaNumber] = int(splitline[1])
        areaNumber += 1
    #print("Shrines:" + str(shrines) + "/120")
    for line in source:
        if line.startswith("tower"):
            splitline = line.split(" ")
            for object in DontDraw_List:
                try:
                    if object.value == int(splitline[1]):
                        Button_List.add(object)
                        Draw_List.add(object.object)
                except:
                    areaNumber=0
        
def save():
    global seedCounters, shrineCounters
    f = open("assets/DATA.txt", "w")
    splitshrines = AreaNames["shrines"].split(" ")
    splitseeds = AreaNames["seeds"].split(" ")
    areaNumber=0
    for object in seedCounters:
        f.write(splitseeds[areaNumber] + " " + str(object) + " \n")
        areaNumber += 1
    areaNumber=0
    f.write("\n \n")
    for object in shrineCounters:
        f.write(splitshrines[areaNumber] + " " + str(object) + " \n")
        areaNumber += 1
    f.write("\n \n")
    for object in Button_List:
        if object.value > -1:
            f.write("tower " + str(object.value) + " \n")

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(windowName)
icon = pygame.image.load('assets/shrine.png')
pygame.display.set_icon(icon)
windowSurface = pygame.display.set_mode(WINDOWSIZE)
mainClock = pygame.time.Clock()

def terminate():
    save()
    pygame.quit()
    sys.exit()

def DrawTextFileFont(text, fontType, fontSize, textcolour, surface, x, y, Mx, My):
    font = pygame.font.Font(fontType, fontSize)
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = (Mx, My)
    y = y
    pos = x, y
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, textcolour)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

Background_List = pygame.sprite.Group()#background
Draw_List = pygame.sprite.Group()#map
DontDraw_List = pygame.sprite.Group()#blank
Button_List = pygame.sprite.Group()#buttons
Cursor_List = pygame.sprite.Group()#cursor

imamgesCounter = 15+15+6
persentageTotal = persentage = 100/imamgesCounter

print("getting images")
imageGroups=[]
class lists():
    def __init__(self, name, nameAgain):
        global imageGroups, imageCounter, persentageTotal, persentage
        self.filename = "Images/" + str(nameAgain)
        self.maxnum = 0
        self.nameAgain = nameAgain
        name = []
        try:
            #print(nameAgain)
            for object in sorted(os.listdir(str(self.filename)), key=len):
                windowSurface.fill((0,0,0))
                DrawTextFileFont(str(persentageTotal)[:4] + "%", "font.ttf", 48, (255,255,255), windowSurface, 0, 0, WINDOWSIZEX, WINDOWSIZEY)
                pygame.display.update()
                #print("  " + str(object))
                Image = pygame.image.load("Images/" + str(self.nameAgain) + "/" + str(object)).convert_alpha()
                #ImageRect = Image.get_rect()
                #Imagesizex = int(str(ImageRect[2]).replace(",",""))
                #Imagesizey = int(str(ImageRect[3]).replace(")>",""))
                name.append(pygame.transform.scale(Image, (WINDOWSIZEX, WINDOWSIZEY)))
                persentageTotal+=persentage
                self.maxnum += 1
            if self.maxnum > 0:
                imageGroups.append(name)
        except:
            print("ERROR: '" + str(nameAgain) + "'")

imageCounter=2
for object in sorted(os.listdir("Images")):
    try:
        for object in sorted(os.listdir("Images/" + object)):
            if str(object).endswith(".png"):
                imageCounter += 1
    except:
        print("ERROR: '" + str(object) + "'")

for object in sorted(os.listdir("Images")):
    object = lists(object, object)

BackgroundImage = pygame.transform.scale(pygame.image.load("assets/background.png"), (WINDOWSIZEX, WINDOWSIZEY)).convert_alpha()
SheikahBackgroundImage = pygame.image.load("assets/sheikah background.png").convert_alpha()
ShrineImage = pygame.transform.scale(pygame.image.load("assets/shrine.png"), (30, 30)).convert_alpha()#125
ButtonImage = pygame.transform.scale(pygame.image.load("assets/buttonimage.png"), (30*4, 30*2)).convert_alpha()
SeedImage = pygame.transform.scale(pygame.image.load("assets/KorokSeed.png"), (30, 30)).convert_alpha()#125
ColourMapImage = pygame.image.load("assets/map light up.png").convert_alpha()

cursorImage = pygame.transform.scale(pygame.image.load("assets/background.png"), (1, 1)).convert_alpha()

class image(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class button(pygame.sprite.Sprite):
    def __init__(self, objectimage, x, y, object, value):
        pygame.sprite.Sprite.__init__(self)
        self.image = objectimage
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.object = object
        self.value = value
        self.shrine = image(ShrineImage, self.x, self.y)
        self.seed = image(SeedImage, self.x, self.y+30)
    def rightclick(self):
        global mouseposx, mouseposy
        if pygame.sprite.spritecollideany(self, Cursor_List) == cursor and self.value > -1:
            if mouseposy > self.y+30:
                seedCounters[self.value]+=1
                self.maxCounterLimit(1)
            else:
                shrineCounters[self.value]+=1
                self.maxCounterLimit(0)
        if pygame.sprite.spritecollideany(self, Cursor_List) == cursor and self.value == -1:
            self.level = int(mouseposy / 40)
            for object in Button_List:
                if object.value == self.level and not self.level == -1:
                    if not object in DontDraw_List:
                        DontDraw_List.add(object)
                    if not object.object in DontDraw_List:
                        DontDraw_List.add(object.object)
                    Draw_List.remove(object.object)
                    Button_List.remove(object)
            
    def leftclick(self):
        global mouseposx, mouseposy
        if pygame.sprite.spritecollideany(self, Cursor_List) == cursor and self.value > -1:
            if mouseposy > self.y+30:
                seedCounters[self.value]-=1
                self.maxCounterLimit(1)
            else:
                shrineCounters[self.value]-=1
                self.maxCounterLimit(0)
        if pygame.sprite.spritecollideany(self, Cursor_List) == cursor and self.value == -1:
            self.level = int(mouseposy / 40)
            for object in DontDraw_List:
                if object.value == self.level and not self.level == -1:
                    if not object in Button_List:
                        Button_List.add(object)
                    if not object.object in Draw_List:
                        Draw_List.add(object.object)

    def maxCounterLimit(self, typen):
        if typen == 1:
            if seedCounters[self.value] > seedCountersMax[self.value]:
                seedCounters[self.value] = seedCountersMax[self.value]
            elif seedCounters[self.value] < 0:
                seedCounters[self.value] = 0
        elif typen == 0:
            if shrineCounters[self.value] > shrineCountersMax[self.value]:
                shrineCounters[self.value] = shrineCountersMax[self.value]
            elif shrineCounters[self.value] < 0:
                shrineCounters[self.value] = 0
    def update(self):
        global korokSeeds, shrines
        if self.value > -1:
            DrawTextFileFont(str(shrineCounters[self.value]) + "/ " + str(shrineCountersMax[self.value]), "font.ttf", 26, mapColours[self.value], windowSurface, self.x+30, self.y, self.x+90+30, self.y+30)
            DrawTextFileFont(str(seedCounters[self.value]) + "/" + str(seedCountersMax[self.value]), "font.ttf", 26, mapColours[self.value], windowSurface, self.x+30, self.y+30, self.x+90+30, self.y+30)
        elif self.value == -2:
            collectedShrines=120-shrines
            collectedSeeds=900-korokSeeds
            DrawTextFileFont(str(collectedShrines), "font.ttf", 30, (255,255,255), windowSurface, self.x+30, self.y, self.x+90, self.y+30)
            DrawTextFileFont(str(collectedSeeds), "font.ttf", 30, (255,255,255), windowSurface, self.x+30, self.y+30, self.x+90, self.y+30)

def controls():
    global mouseposx, mouseposy
    LEFT = 1
    RIGHT = 3
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == MOUSEMOTION:
            Cursor_List.update()
            cursor.rect.x = mouseposx = event.pos[0]
            cursor.rect.y = mouseposy = event.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                for object in Button_List:
                    try:
                        object.leftclick()
                        collectableTotals()
                    except:
                        LEFT = 1
                        #print("Object has no 'leftclick'")
            if event.button == RIGHT:
                for object in Button_List:
                    try:
                        object.rightclick()
                        collectableTotals()
                    except:
                        RIGHT = 3
                        #print("Object has no 'rightclick'")

#pygame.transform.scale(Image, (Imagesizex, Imagesizey))
#print("initiating objects")
cursor = image(cursorImage, 0, 0)
Cursor_List.add(cursor)
Background = image(BackgroundImage, 0, 0)
Background2 = image(SheikahBackgroundImage, 0, 0)
Background_List.add(Background, Background2)

Plateau = image(imageGroups[0][0], 0, 0)
Hyrule = image(imageGroups[0][1], 0, 0)
Dualing = image(imageGroups[0][2], 0, 0)
Hateno = image(imageGroups[0][3], 0, 0)
Lanayru = image(imageGroups[0][4], 0, 0)
Gerudo = image(imageGroups[0][5], 0, 0)
Highlands = image(imageGroups[0][6], 0, 0)
Lake = image(imageGroups[0][7], 0, 0)
Faron = image(imageGroups[0][8], 0, 0)
Ridgeland = image(imageGroups[0][9], 0, 0)
Tabantha = image(imageGroups[0][10], 0, 0)
Hebra = image(imageGroups[0][11], 0, 0)
Forest = image(imageGroups[0][12], 0, 0)
Mountain = image(imageGroups[0][13], 0, 0)
Akala = image(imageGroups[0][14], 0, 0)
Draw_List.add(Plateau, Hyrule, Dualing, Hateno, Lanayru, Gerudo, Highlands, Lake, Faron, Ridgeland, Tabantha, Hebra, Forest, Mountain, Akala)

PlateauButton = button(ButtonImage, 220, 450, Plateau, 0)
HyruleButton = button(ButtonImage, 280, 290, Hyrule, 1)
DualingButton = button(ButtonImage, 380, 380, Dualing, 2)
HatenoButton = button(ButtonImage, 560, 460, Hateno, 3)
LanayruButton = button(ButtonImage, 540, 270, Lanayru, 4)
GerudoButton = button(ButtonImage, 20, 530, Gerudo, 5)
HighlandsButton = button(ButtonImage, 3, 320, Highlands, 6)
LakeButton = button(ButtonImage, 280, 530, Lake, 7)
FaronButton = button(ButtonImage, 490, 530, Faron, 8)
RidgelandButton = button(ButtonImage, 130, 260, Ridgeland, 9)
TabanthaButton = button(ButtonImage, 2, 200, Tabantha, 10)
HebraButton = button(ButtonImage, 150, 10, Hebra, 11)
ForestButton = button(ButtonImage, 310, 10, Forest, 12)
MountainButton = button(ButtonImage, 440, 160, Mountain, 13)
AkalaButton = button(ButtonImage, 590, 100, Akala, 14)
Button_List.add(PlateauButton, HyruleButton, DualingButton, HatenoButton, LanayruButton, GerudoButton, HighlandsButton, LakeButton, FaronButton, RidgelandButton, TabanthaButton, HebraButton, ForestButton, MountainButton, AkalaButton)

Total = button(ButtonImage, 0, 0, None, -2)
ColourMapButton = button(ColourMapImage, 720, 0, None, -1)
Button_List.add(ColourMapButton, Total)
#print("loading save")
DontDraw_List.add(PlateauButton, HyruleButton, DualingButton, HatenoButton, LanayruButton, GerudoButton, HighlandsButton, LakeButton, FaronButton, RidgelandButton, TabanthaButton, HebraButton, ForestButton, MountainButton, AkalaButton)
DontDraw_List.add(Plateau, Hyrule, Dualing, Hateno, Lanayru, Gerudo, Highlands, Lake, Faron, Ridgeland, Tabantha, Hebra, Forest, Mountain, Akala)
load()
Button_List.remove(PlateauButton, HyruleButton, DualingButton, HatenoButton, LanayruButton, GerudoButton, HighlandsButton, LakeButton, FaronButton, RidgelandButton, TabanthaButton, HebraButton, ForestButton, MountainButton, AkalaButton)
Draw_List.remove(Plateau, Hyrule, Dualing, Hateno, Lanayru, Gerudo, Highlands, Lake, Faron, Ridgeland, Tabantha, Hebra, Forest, Mountain, Akala)
load()
collectableTotals()
while True:
    windowSurface.fill((0,0,0))
    Background_List.draw(windowSurface)
    Draw_List.draw(windowSurface)

    Button_List.draw(windowSurface)
    Button_List.update()
    Cursor_List.draw(windowSurface)
    controls()
    pygame.display.update()
    mainClock.tick(FPS)