#this library converts the random into integers
from random import randint

#lists of animals included in the simulation
#divided into two types, the zoo animals will have a starting state position of zoolocation.
#local animals will have a starting position of something else. 

zoo_animals = ["Penguins", "Zebras", "Monkeys", "Sloths"]
local_animals = ["Humans", "Squirrels", "Racoons", "Coyotes"]

#this chooses the type of zoo animal that will escape randomly. they're stored in variables.
escapedAnimalRandom = zoo_animals[randint(0,3)]
numberOfescaped = randint(0,100) #maybe change the max to the capacity of population for the zoo

#this is the variable of which animal escaped and how many of them escaped
wantedAnimals = {
    "animal escaped": escapedAnimalRandom,
    "number escaped": numberOfescaped 
}

#random escaped 
#will need to visualize this instead of words eventually.
print wantedAnimals

## where would the penguin go##
