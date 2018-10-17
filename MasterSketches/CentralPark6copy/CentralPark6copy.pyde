
def setup():
    size(1000,1000)
    frameRate(30)
    background(0)
    
    global slothImg
    global humanImg
    global zebraImg
    global racoonImg
    
    slothImg = loadImage('Images/sloth.jpg')
    racoonImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/racoon.jpg')
    humanImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/human.jpg') 
    zebraImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/zebra.jpg')
  # monkeyImage = loadImage('Images/monkey.jpg')
  
  # capturedSloth = loadImage('..  ..')
  # capturedRacoon = loadImage('..  ..')
  # capturedZebra = loadImage('..  ..')
  # capturedMonkey = loadImage('..  ..')

# baseCPImage = loadImage("TKKTKTKT") #Central Park image base
# basePark2Imag = loadImage("TKTKTK")
# basePark3Imag = loadImage("ttkktk")
# def keyPressed():
#     if key == 'r':
#         new_racoon = Racoon(mouseX, mouseY)
#         racoonList.append(new_racoon)
#     elif key == 'h':
#         new_human = Human(mouseX, mouseY)
#         humanList.append(new_human)
#     elif key == ' ':
#         for human in humanList:
#             human.beginSim()
#         for racoon in racoonList:
#             racoon.beginSim()

def keyPressed():
    for i in range(1,16):
        new_racoon = Racoon(random.randint(0, 1000), random.randint(0, 1000))
        racoonList.append(new_racoon)
    for j in range(1,3):
        new_human = Human(random.randint(0, 1000), random.randint(0, 1000))
        humanList.append(new_human)
    # for k in range(1, 20):
    #     new_zebra = Zebra(random.randint(0,1000), random.randint(0,1000))
    if key == ' ':
        for human in humanList:
            human.beginSim()
        for racoon in racoonList:
            racoon.beginSim()

import random
import math
from random import randint

#global variables

xMax = 1500
yMax = 1500
 
number_of_zebras = 20
number_of_monkeys = 1
number_of_sloths = 2
number_of_racoons = 15
total_number_of_animals = number_of_zebras + number_of_monkeys + number_of_sloths + number_of_racoons 

number_of_humans = 1
 
# class Animal():
    
#     def __init__(self, animalId, speed, memory, knowledgeOfCentralPark, energy, hunger, health):
#        self.age = age
#        self.animalid = animalid
#        self.position
#        self.speed = speed
#        self.memory = memory  #goal stored in memory 
#        self.hunger = hunger
#        self.thirst = randint(0,10)

       
     #def eat: 
  
      
    # def move(self):
    #    print(str(self.animalid) + " is now moving.")
    #    if self.energy <15:
    #         print(str(self.animalid) + " is moving slow!")
    #         print("That " + str(self.species) + " is " + str(self.age) + " years old.")
    #    else: print("That " + str(self.species) + " is moving pretty fast!")  
       
     
# class Zebra(Animal): 
#       super(Zebra, self).__init__()
      
      
# class Zebra: 
    
    
#     zebraImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/zebra.jpg')
      
      
      
      
#      #will add more methods here for each of the animal classes rekated to position and memory, etc- to come!!
#      #heading to water
     
# class Coyote(Animal):
#     super(Coyote, self).__init__()

# class Monkey(Animal):
#     #monkeys move together execpt the young one goes wherever 
#     super(Monkey, self).__init__()

  
# class Sloth(Animal):
#       #heads to the trees
#      super(Sloth, self).__init__()
     
#class Racoon(Animal):
    
  #def __init__(self, animalId, speed, memory, hunger, thirst):
#        self.age = age
#        self.animalid = animalid
#        self.position
#        self.speed = speed
#        self.memory = memory  #goal stored in memory 
#        self.hunger = hunger
#        self.thirst = randint(0,10)


class Racoon():
     def __init__(self, xPos, yPos, startSim=False, memory):
        self.xPos = xPos
        self.yPos = yPos
        
        self.startSim = startSim
    
        self.speed = random.randint(5,10)
        
        self.hunger = random.randint(1,10)
        self.thirst = random.randint(1,10)
        self.age = random.randint(1,20)
        self.memory = memory 
        
        if self.goal = "water":
            if self.water1_Xpos + 50 >= self.xPos &  self.water1_Ypos + 50 >= self.yPos:
                self.direction = 
        
        
          # def move(self):
    #    print(str(self.animalid) + " is now moving.")
    #    if self.energy <15:
    #         print(str(self.animalid) + " is moving slow!")
    #         print("That " + str(self.species) + " is " + str(self.age) + " years old.")
    #    else: print("That " + str(self.species) + " is moving pretty fast!")  
       
        
        self.direction = random.uniform(0, PI*2)
        
     def display(self):
        racoonImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/racoon.jpg')
        image(racoonImg, self.xPos, self.yPos, 50, 75)
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
                
# =     def move(self): integrate above
#         if self.energy < 15:
#             self.speed = random(2, 5)
#         else:
#             self.speed = random(6,10)
    
     def beginSim(self):
        self.startSim = True
        
       
     def eat(self):
          self.hunger = self.hunger -20
          
     def changeDir(self, human):
         self.direction = math.atan((self.yPos-human.yPos)/(self.xPos-human.xPos+1)) if (self.xPos-human.xPos) == 0 else math.atan((self.yPos-human.yPos)/(self.xPos-human.xPos+1))
             # if self.energy < 15:
             #    self.speed = 10
             # else: 
             #    self.speed = 15    
             

class Human: 
     def __init__(self, xPos, yPos, startSim=False):
            self.xPos = xPos
            self.yPos = yPos
        # self.caughtZebra = 0
        # self.caughtSloth = 0
        # self.caughtMonkey = 0
            self.caughtRacoon = 0
            self.startSim = startSim
        
            self.speed = random.randint(5, 10)
            self.direction = random.uniform(0, PI*2)
                
     def display(self):
        humanImg = loadImage('/Users/DSetton/Documents/Processing/CentralPark6/Images/human.jpg') 
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
    
    # def catchSloth(self):
    #     self.caughtSloth += 1
        
    # def catchMonkey(self):
    #     self.caughtMonkey += 1
    
    # def catchZebra(self): 
    #     self.caughtZebra += 1
    
     def chase(self, racoon):
        self.direction = math.atan((racoon.yPos-self.yPos)/(racoon.xPos-self.xPos+1)) if (racoon.xPos-self.xPos) == 0 else math.atan((racoon.yPos-self.yPos)/(racoon.xPos-self.xPos+1))
        self.speed = 15
    
     def beginSim(self):
        self.startSim = True
        
racoonList = []
# slothList = []
# zebraList = []


# maxSloth = 3
# maxZebra = 5
humanList = []
animalList =[]

maxRacoon = 100
maxHuman = 2


#environment objects

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
    
    #put these in a list, or a dictionary if you want to keep the names
    #then later you write for water in Water, and call the draw command 
    
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
    
    
    
    for human in humanList:
        human.display()
    for racoon in racoonList:
        racoon.display()

   
    print 'racoons caught count: ', len(racoonList)

# def bunPair():
#     toRemove = []
#     newBuns = []
#     for r_i in range(len(bunList)):
#         for b_i in range(r_i+1, len(bunList)):
#             r = bunList[r_i]
#             b = bunList[b_i]
#             if abs(r.xPos - b.xPos) < 10 and abs(r.yPos - b.yPos) < 10 and len(bunList) < maxBun: #finding spatial conditions for reproduction
#                 r.reproduce() #+1 reproduction count
#                 b.reproduce()
#                 babyBun = Rabbit((r.xPos + b.xPos)/2, (r.yPos + b.yPos)/2, startSim=True) #create baby bunny with location midpoint of first 2
#                 r.xPos = random.randint(0, xMax)
#                 r.yPos = random.randint(0, yMax)
#                 b.xPos = random.randint(0, xMax)
#                 b.yPos = random.randint(0, yMax)
#                 newBuns.append(babyBun) #adding new bunny to rabbit list
#                 if r.repNum > 3: #condition for deleting bun
#                     toRemove.append(r_i)
#                 if b.repNum > 3:
#                     toRemove.append(b_i)
#     for deceasedBun_i in sorted(toRemove, reverse=True):
#         bunList.pop(deceasedBun_i)
#     bunList.extend(newBuns)
        
def racoonChase():
    toRemove = []
    for h_i in range(len(humanList)):
        for r_i in range(len(racoonList)):
            h = humanList[w_i]
            r = racoonList[r_i]
            if abs(h.xPos - r.xPos) < 30 and abs(h.yPos - r.yPos) < 30: #finding spatial conditions for reproduction
                h.chase(r)
                r.changeDir(w)
                
def raccoonCatch():
    toRemoveRacoon = []
    toRemoveHuman = []
    newHumans = []
    for h_i in range(len(humanList)):
        for r_i in range(len(racoonList)):
            h = humanList[h_i]
            r = racoonList[r_i]
            if abs(w.xPos - r.xPos) < 10 and abs(w.yPos - r.yPos) < 10: #finding spatial conditions for reproduction
                h.catchRacoon()
                toRemoveRacoon.append(r_i)
                if h.racoonCaught > 3:
                    toRemoveHuman.append(w_i)
                    babyHuman = Wolf(w.xPos + random.randint(-50, 50), w.yPos + random.randint(-50, 50), startSim=True)
                    newHumans.append(babyHuman)
    for deceasedRacoon_i in sorted(toRemoveRacoon, reverse=True):
        racoonList.pop(deceasedBun_i)
    for deceasedHuman_i in sorted(list(set(toRemoveHuman)), reverse=True):
        humanList.pop(deceasedHuman_i)
    humanList.extend(newHumans)
    
racoonChase()
#racoonCatch()
  
