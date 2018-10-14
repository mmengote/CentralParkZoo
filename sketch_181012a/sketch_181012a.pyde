#environment

#agents

from random import randint

#tuples?
localAnimals = ("Raccoons", "Coyotes", "Squirrels", "Humans")
myit = iter(localAnimals)

for x in localAnimals:
    print(x)
    
#Number of Animals that escapes

    
#Local Animals, raccoons is the most complete. 
class Raccoons:
    def _init_ (self, animalId, speed, memory, knowledgeOfCentralPark, energy, hunger, health, age, face, leftarm, rightarm, body, leftleg, rightleg, localAnimal, position):
        self.animalId = animalId
        self.speed = speed
        self.memory = memory
        self.knowledgeOfCentralPark = knowledgeOfCentralPark
        self.energy = energy
        self.hunger = hunger
        self.health = health
        self.age = age
        self.face = face
        self.leftarm = leftarm
        self.rightarm = rightarm
        self.body = body
        self.leftleg = leftleg
        self.rightleg = rightleg
        self.localAnimal = localAnimal
        self.position = position
        
#creates objects within the class
def main():
    r1 = Raccoons()

#need to learn a command of how to keep creating raccoons or animal until a population ends. maybe while something is less than the maximum population, 
#run a piece of code that will create a new instance of the class. 
#global variable of population.


#code that will create a new instance of the class, so basically this code will give birth to new animals. 
        
class Coyotes: 
    def _init_ (self, animalId, speed, memory, energy, health, age, face, leftarm, rightarm, body, leftleg, rightleg, localAnimal):
        self.animalId = animalId
        self.speed = speed
        self.memory = memory
        self.energy = energy
        self.health = health
        self.age = age
        self.face = face
        self.leftarm = leftarm
        self.rightarm = rightarm
        self.body = body
        self.leftleg = leftleg
        self.rightleg = rightleg
        self.localAnimal = localAnimal
        
class Squirrels:
    def _init_ (self, animalId, speed, memory, energy, health, age, face, leftarm, rightarm, body, leftleg, rightleg, localAnimal):
        self.animalId = animalId
        self.speed = speed
        self.memory = memory
        self.energy = energy
        self.health = health
        self.age = age
        self.face = face
        self.leftarm = leftarm
        self.rightarm = rightarm
        self.body = body
        self.leftleg = leftleg
        self.rightleg = rightleg
        self.localAnimal = localAnimal
  
  
#Escaped Animals
    #defines the blueprint of the class.   
    #a1 = LocalAnimal("Racoon", randint(0,10))
    
class Sloths:
    def _init_ (self, animalId, speed, memory, energy, health, age, face, leftarm, rightarm, body, leftleg, rightleg, Animal):
        self.animalId = animalId
        self.speed = speed
        self.memory = memory
        self.energy = energy
        self.health = health
        self.age = age
        self.face = face
        self.leftarm = leftarm
        self.rightarm = rightarm
        self.body = body
        self.leftleg = leftleg
        self.rightleg = rightleg
        self.animal = animal
        
class Penguins: 
    def _init_ (self, animalId, speed, memory, energy, health, age, face, leftarm, rightarm, body, leftleg, rightleg, Animal):
        self.animalId = animalId
        self.speed = speed
        self.memory = memory
        self.energy = energy
        self.health = health
        self.age = age
        self.face = face
        self.leftarm = leftarm
        self.rightarm = rightarm
        self.body = body
        self.leftleg = leftleg
        self.rightleg = rightleg
        self.animal = animal
 
class Monkeys: 
    def _init_ (self, animalId, speed, memory, energy, health, age, face, leftarm, rightarm, body, leftleg, rightleg, Animal):
        self.animalId = animalId
        self.speed = speed
        self.memory = memory
        self.energy = energy
        self.health = health
        self.age = age
        self.face = face
        self.leftarm = leftarm
        self.rightarm = rightarm
        self.body = body
        self.leftleg = leftleg
        self.rightleg = rightleg
        self.animal = animal
        
class Humans: 
    def _init_ (self, animalId, speed, memory, energy, health, age, face, leftarm, rightarm, body, leftleg, rightleg, localAnimal):
        self.animalId = animalId
        self.speed = speed
        self.memory = memory
        self.energy = energy
        self.health = health
        self.age = age
        self.face = face
        self.leftarm = leftarm
        self.rightarm = rightarm
        self.body = body
        self.leftleg = leftleg
        self.rightleg = rightleg
        self.localAnimal = localAnimal


#function that draws the local animal
#if health <= 0 animal dies
#if animal = memory =x. 
#interaction
