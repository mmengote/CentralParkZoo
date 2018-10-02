class Animal():
    
    def __init__(self, animalid, species, age, howbig, knowledge, energy):
       self.age = age
       self.animalid = animalid
       self.species = species
       self.howbig= howbig
       self.knowledge = knowledge
       self.energy = energy
       
    def move(self):
       print(str(self.animalid) + " is now moving.")
       if self.energy <15:
            print(str(self.animalid) + " is moving slow!")
            print("That " + str(self.species) + " is " + str(self.age) + " years old.")
       else: print("That " + str(self.species) + " is moving pretty fast!")
       
first_bear = Animal('bear1', 'bear', 14, 'large', 23, 25)
#print("The first animal is a " + animaly.age + ".")
#print("the first animal is" + animaly.age + " years old.")

second_bear = Animal('bear2', "bear", 12, 'small', 12, 9)

first_monkey = Animal('monkey1', "monkey", 15, 'small', 17, 9)

first_bear.move()
second_bear.move()
first_monkey.move()