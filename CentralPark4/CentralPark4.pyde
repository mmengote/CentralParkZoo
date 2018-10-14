def setup():
    size(1000,1000)
    frameRate(30)
    background(0)
    
#global food source,

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
    #define the actual water sources
water1 = Water(10, 88, 450, 400, color(204, 229,255))
water2 = Water(1000, 88, 400, 800, color(204,229,255))
water3 = Water(500, 500, 195, 300, color(204,229,255))

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

    #first cluster 
tree1 = Trees (250, 50, 80, 80, color(0, 51, 0))
tree2 = Trees (50, 400, 40, 40, color(0, 51, 0))
tree3 = Trees (290, 150, 40, 40, color(0, 51, 0))
tree4 = Trees (290, 200, 70, 70, color(0, 51, 0))
tree5 = Trees (300, 300, 40, 40, color(0, 51, 0))
tree6 = Trees (200, 300, 70, 70, color(0, 51, 0))


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
    
lawn1 = Lawn(700, 500, 100, 500, color(102, 204, 0))
lawn2 = Lawn(350, 100, 300, 100, color(102, 204, 0))
lawn3 = Lawn(1100, 600, 150,100, color(102, 204, 0))
lawn4 = Lawn(100, 700, 200, 70, color(102, 204, 0))
lawn5 = Lawn(50, 500, 100, 20, color(102, 204, 0))
lawn6 = Lawn(330, 330, 60, 50, color(102, 204, 0))

def setup():
    size(1280,800)
   
def draw():
    background(255)
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
 

from random import randint

number_of_zebras = 5
number_of_monkeys = 1
number_of_sloths = 2
number_of_racoons = 5
total_number_of_animals = number_of_zebras + number_of_monkeys + number_of_sloths + number_of_racoons 

number_of_humans = 1

# global baseImage, alltreesonImage
# baseImage = loadImage("TKKTKTKT")

global 
class Animal():
    
    def __init__(self, animalId, speed, memory, knowledgeOfCentralPark, energy, hunger, health):
       self.age = age
       self.animalid = animalid
       self.position
       self.speed = speed
       self.memory = memory
       self.knowledgeOfCentralPark = knowledgeOfCentralPark
       self.howbig= howbig
       self.knowledge = knowledge
       self.health = health
       self.energy = randint(0,10)
       
     #def eat: 
  
      
    # def move(self):
    #    print(str(self.animalid) + " is now moving.")
    #    if self.energy <15:
    #         print(str(self.animalid) + " is moving slow!")
    #         print("That " + str(self.species) + " is " + str(self.age) + " years old.")
    #    else: print("That " + str(self.species) + " is moving pretty fast!")  
       
     
class Zebra(Animal): 
     pass 
     #will add more methods here for each of the animal classes rekated to position and memory, etc- to come!!
     
class Monkey(Animal):
     pass

class Sloth(Animal):
     pass
     
class Racoon(Animal):
     pass

class Human: 
        def __init__(self, xPos, yPos, startSim=False):
        self.xPos = xPos
        self.yPos = yPos
        self.caughtZebra = 0
        self.caughtSloth = 0
        self.caughtMonkey = 0
        self.caughtRacoon = 0
        self.startSim = startSim
        self.speed = random.randint(5, 10)
        self.direction = random.uniform(0, PI*2)
                
    def display(self):
        #img needs resizing
        image(humanImg, self.xPos, self.yPos, 100, 110)
        if self.startSim == True:
            self.xPos = self.xPos + self.speed * cos(self.direction) + random.randint(-10,10)
            self.yPos = self.yPos + self.speed * sin(self.direction) + random.randint(-10,10)
            
            if self.xPos >= xMax:
                self.xPos = 0
            elif self.xPos <= 0:
                self.xPos = xMax              
            if self.yPos >= yMax:
                self.yPos = 0
            elif self.yPos <= 0:
                self.yPos = yMax
                    
    def catchRacoon(self):
        self.caughtRacoon += 1
    
    def catchSloth(self):
        self.caughtSloth += 1
        
    def catchMonkey(self):
        self.caughtMonkey += 1
    
    def catchZebra(self): 
        self.caughtZebra += 1
    
    def chase(self, animal):
        self.direction = math.atan((animal.yPos-self.yPos)/(animal.xPos-self.xPos+1)) if (animal.xPos-self.xPos) == 0 else math.atan((animal.yPos-self.yPos)/(animal.xPos-self.xPos+1))
        self.speed = 15
    
    def beginSim(self):
        self.startSim = True
racoonList = []
slothList = []
zebraList = []

maxRacoon = 100
maxSloth = 3
maxZebra = 5
               
     
       
# first_bear = Animal('bear1', 'bear', 14, 'large', 23, 25)
# #print("The first animal is a " + animaly.age + ".")
# #print("the first animal is" + animaly.age + " years old.")

# second_bear = Animal('bear2', "bear", 12, 'small', 12, 9)

# first_monkey = Animal('monkey1', "monkey", 15, 'small', 17, 9)

# first_bear.move()
# second_bear.move()
# first_monkey.move()

import random
import math
xMax = 1500
yMax = 1500
class Racoon:
    def __init__(self, xPos, yPos, startSim=False):
        self.xPos = xPos
        self.yPos = yPos
        self.repNum = 0
        self.startSim = startSim
    
        self.speed = random.randint(5,10)
        self.direction = random.uniform(0, PI*2)
            
    def display(self):
        #img needs resizing
        image(raccoonImg, self.xPos, self.yPos, 50, 75)
        if self.startSim == True:
            self.xPos = self.xPos + self.speed * cos(self.direction) + random.randint(-10,10)
            self.yPos = self.yPos + self.speed * sin(self.direction) + random.randint(-10,10)
            
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
        
def changeDir(self, wolf):
        self.direction = math.atan((self.yPos-human.yPos)/(self.xPos-human.xPos+1)) if (self.xPos-human.xPos) == 0 else math.atan((self.yPos-human.yPos)/(self.xPos-human.xPos+1))
        self.speed = 10
       
  
