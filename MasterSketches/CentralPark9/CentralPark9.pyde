import random
import math
from random import randint

#global variables

xMax = 1000
yMax = 1000

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
        rect(self.lawn_XPos, self.lawn_YPos, self.lawn_height, self.lawn_width)
         
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
        racoonImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/racoon.jpg')
        image(racoonImg, self.xPos, self.yPos, 50, 75)
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

class Human():
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
        humanImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/human.jpg') 
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
water1 = Water(10, 88, 450, 400, color(204, 229,255))
water2 = Water(1000, 88, 400, 800, color(204,229,255))
water3 = Water(500, 500, 195, 300, color(204,229,255))
tree1 = Trees (250, 50, 80, 80, color(0, 51, 0))
tree2 = Trees (50, 400, 40, 40, color(0, 51, 0))
tree3 = Trees (290, 150, 40, 40, color(0, 51, 0))
tree4 = Trees (290, 200, 70, 70, color(0, 51, 0))
tree5 = Trees (300, 300, 40, 40, color(0, 51, 0))
tree6 = Trees (200, 300, 70, 70, color(0, 51, 0))
lawn1 = Lawn(700, 500, 100, 500, color(102, 204, 0))
lawn2 = Lawn(350, 100, 300, 100, color(102, 204, 0))
lawn3 = Lawn(1100, 600, 150,100, color(102, 204, 0))
lawn4 = Lawn(100, 700, 200, 70, color(102, 204, 0))
lawn5 = Lawn(50, 500, 100, 20, color(102, 204, 0))
lawn6 = Lawn(330, 330, 60, 50, color(102, 204, 0))

new_racoon.beginSim()
new_human.beginSim()
            
def setup():
    size(1000,1000)
    loadPixels()

def draw():
    background(255)
    frameRate(25)
    water1.draw()
    water2.draw()
    water3.draw()
    tree1.draw()
    tree2.draw()
    tree3.draw()
    tree4.draw()
    tree5.draw()
    tree6.draw()
    lawn1.draw()
    lawn2.draw()
    lawn3.draw()
    lawn4.draw()
    lawn5.draw()
    lawn6.draw()
    new_racoon.display()
    new_human.display()
    
    
    
    
