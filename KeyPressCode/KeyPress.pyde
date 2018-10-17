coyoteList = []
zebraList = []
raccoonList = []
boarList = []
slothList = []
humanList = []
jaguarList = []

def keyPressed():
     if key == 'z':
        new_zebra= Zebra(mouseX, mouseY)
        zebraList.append(new_zebra)
    if key == 'c':
        new_coyote = Coyote(mouseX, mouseY)
        coyoteList.append(new_coyote)
    elif key == 'r':
        new_raccoon = Raccoon(mouseX, mouseY)
        raccoonList.append(new_raccoon)
    elif key == 'b':
        new_raccoon = Boar(mouseX, mouseY)
        boarList.append(new_boar)
    elif key == 's':
        new_sloth = Sloth(mouseX, mouseY)
        slothList.append(new_sloth)
    elif key == 'j':
        new_zebra= Jaguar(mouseX, mouseY)
        jaguarList.append(new_zebra)
    elif key == 'h':
        new_human = Human(mouseX, mouseY)
        humanList.append(new_human)
        
        
    
