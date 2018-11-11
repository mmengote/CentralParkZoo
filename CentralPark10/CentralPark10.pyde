import random
import math
from random import randint

#global variables

xMax = 1000
yMax = 1000

#define global variables

#water color
water_col = color(105,119,131) 
water_stroke = color(0, 25, 51)
#lawn colors
lawn_col = color (90, 116, 82)
lawn_stroke = color (90, 116, 82) 
#tree colors
tree_col = color (0, 51, 0)
tree_stroke = color (0, 51, 0)
#fence color
fence_stroke = color (255)
#building color
building_col = color (87, 87, 87)
building_stroke = color (87, 87, 87)

class Water(object):
    #initiate
    def __init__(self, water_XPos, water_YPos,water_width, water_height, water_col):
        self.water_width = water_width
        self.water_XPos = water_XPos
        self.water_YPos = water_YPos
        self.water_height = water_height
        self.water_col = water_col
    #define key features
    def draw(self):
        fill(self.water_col)
        stroke(water_stroke)
        ellipse(self.water_XPos, self.water_YPos, self.water_width, self.water_height)
    
class Trees(object): 
    #initiate
     def __init__(self, tree_XPos, tree_YPos, tree_width, tree_hgt, tree_col):
        self.tree_XPos = tree_XPos
        self.tree_YPos = tree_YPos
        self.tree_col = tree_col
        self.tree_width = tree_width
        self.tree_hgt = tree_hgt
     #define key features to draw
     def draw(self):
         fill(self.tree_col)
         ellipse(self.tree_XPos, self.tree_YPos, self.tree_width, self.tree_hgt)
         
class Lawn(object):
    def __init__(self, lawn_XPos, lawn_YPos, lawn_height, lawn_width, lawn_col):
        self.lawn_XPos = lawn_XPos
        self.lawn_YPos = lawn_YPos 
        self.lawn_height = lawn_height
        self.lawn_width = lawn_width
        self.lawn_col = lawn_col
        
    def draw(self):
        fill(self.lawn_col)
        stroke(lawn_stroke)
        rect(self.lawn_XPos, self.lawn_YPos, self.lawn_height, self.lawn_width)
        
class Fence (object):
    def __init__(self, fence_xpos1, fence_ypos1, fence_xpos2, fence_ypos2):
        self.fence_xpos1 = fence_xpos1
        self.fence_ypos1 = fence_ypos1
        self.fence_xpos2 = fence_xpos2
        self.fence_ypos2 = fence_ypos2
        
    def draw(self):
        stroke(fence_stroke)
        line (self.fence_xpos1,self.fence_ypos1,self.fence_xpos2,self.fence_ypos2)
        
class Building(object):
    def __init__(self, building_XPos, building_YPos, building_height, building_width, building_col):
        self.building_XPos = building_XPos
        self.building_YPos = building_YPos 
        self.building_height = building_height
        self.building_width = building_width
        self.building_col = building_col
        
    def draw(self):
        fill(self.building_col)
        stroke(building_stroke)
        rect(self.building_XPos, self.building_YPos, self.building_height, self.building_width) 
        
class Racoon():
     def __init__(self, xPos, yPos, startSim=False):
        self.xPos = xPos
        self.yPos = yPos
        
        self.startSim = startSim
     
     def move(self):     
        # self.direction = random.uniform(0, PI*2)
        #print(pixels[self.xPos,self.yPos])
        if random.randint(1,2)==1: #1 is up, 2 is down
            return 0,random.randint(-10,10)
        else:
            return random.randint(-10,10),0

     def display(self):
        racoonImg = loadImage('/Users/DSetton/Desktop/raccoon.png')
        image(racoonImg, self.xPos, self.yPos, 50, 75)
        if self.startSim == True:
            direction_x, direction_y = self.move()
            # self.xPos = self.xPos + self.speed * cos(self.direction) + random.randint(-10,10)
            # self.yPos = self.yPos + self.speed * sin(self.direction) + random.randint(-10,10)
            self.xPos = self.xPos + direction_x
            self.yPos = self.yPos + direction_y
  
        
        if self.xPos >= xMax:
                self.xPos = 0
        elif self.xPos <= 0:
                self.xPos = xMax              
        if self.yPos >= yMax:
                self.yPos = 0
        elif self.yPos <= 0:
                self.yPos = yMax
                

     def beginSim(self):
        self.startSim = True

class Human():
     def __init__(self, xPos, yPos, startSim=False):
        self.xPos = xPos
        self.yPos = yPos
        
        self.startSim = startSim
     
     def move(self):     
        # self.direction = random.uniform(0, PI*2)
        #print(pixels[self.xPos,self.yPos])
        if random.randint(1,2)==1: #1 is up, 2 is down
            return 0,random.randint(-10,12)
        else:
            return random.randint(-10,12),2

     def display(self):
        humanImg = loadImage('/Users/DSetton/Desktop/human.png') 
        image(humanImg, self.xPos, self.yPos, 100, 110)
        if self.startSim == True:
            direction_x, direction_y = self.move()
            # self.xPos = self.xPos + self.speed * cos(self.direction) + random.randint(-10,10)
            # self.yPos = self.yPos + self.speed * sin(self.direction) + random.randint(-10,10)
            self.xPos = self.xPos + direction_x
            self.yPos = self.yPos + direction_y
        #something weird happening here - walker vanished outside frame
        if self.xPos >= xMax:
                self.xPos = 0
        elif self.xPos <= 0:
                self.xPos = xMax              
        if self.yPos >= yMax:
                self.yPos = 0
        elif self.yPos <= 0:
                self.yPos = yMax
                

     def beginSim(self):
        self.startSim = True

racoonList = []
new_racoon = Racoon(200, 200)
new_human = Human(400, 400)

water1 = Water(10, 88, 450, 400, water_col)
water2 = Water(1000, 88, 400, 800, water_col)
water3 = Water(500, 500, 195, 300, water_col)
tree1 = Trees (250, 50, 20, 20, color(0, 51, 0))
tree2 = Trees (50, 400, 40, 40, color(0, 51, 0))
tree3 = Trees (290, 150, 40, 40, color(0, 51, 0))
tree4 = Trees (290, 200, 50, 50, color(0, 51, 0))
tree5 = Trees (300, 300, 40, 40, color(0, 51, 0))
tree6 = Trees (200, 300, 30, 30, color(0, 51, 0))
lawn1 = Lawn(700, 500, 100, 500, lawn_col)
lawn2 = Lawn(350, 100, 300, 100, lawn_col)
lawn3 = Lawn(1100, 600, 150,100, lawn_col)
lawn4 = Lawn(100, 700, 200, 70, lawn_col)
lawn5 = Lawn(50, 500, 100, 20, lawn_col)
lawn6 = Lawn(330, 330, 60, 50, lawn_col)
fence1 = Fence(350, 100, 650, 100)
fence2 = Fence(650, 100, 650, 0)
fence3 = Fence(600, 500, 600, 1000)
fence4 = Fence(800, 500, 800, 1000)
fence5 = Fence(600, 500, 800, 500)
building1 = Building(50, 1000, 100, 500, building_col)
building2 = Building(25, 500, 300, 100, building_col)
building3 = Building(100, 600, 150, 100, building_col)


new_racoon.beginSim()
new_human.beginSim()
            
def setup():
    size(1000,1000)
    loadPixels()

def draw():
    background(136,151,128)
    frameRate(25)
    #draw the water
    water1.draw()
    water2.draw()
    water3.draw() 
    #draw first cluster tees
    tree1.draw()
    tree2.draw()
    tree3.draw()
    tree4.draw()
    tree5.draw()
    tree6.draw()
    #draw lawn
    lawn1.draw()
    lawn2.draw()
    lawn3.draw()
    lawn4.draw()
    lawn5.draw()
    lawn6.draw()
    #draw fences
    fence1.draw()
    fence2.draw()
    fence3.draw()
    fence4.draw()
    fence5.draw()
    #draw buildings
    building1.draw()
    building2.draw()
    building3.draw()
    new_racoon.display()
    new_human.display()
    
    
    
    
