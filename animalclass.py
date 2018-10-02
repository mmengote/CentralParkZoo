class Bear():
    
    def __init__(self, age, bearid, howbig, knowledge, energy):
       self.age = age
       self.bearid = bearid
       #self.color= color
       self.howbig= howbig
       self.knowledge = knowledge
       self.energy = energy
       
    def move(self):
       print(str(self.bearid) + " is now moving.")
       if self.energy <15:
            print("He is moving slow!")
       else: print("He is moving pretty fast!")
       
first_bear = Bear(12, 'Joe', 'large', 23, 25)
# print("The first animal is a " + animaly.age + ".")
# print("the first animal is" + animaly.age + " years old.")

second_bear = Bear(13, "Mark", 'small', 12, 9)

first_bear.move()
second_bear.move()