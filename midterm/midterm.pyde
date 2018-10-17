x=[]
y=[]
xSpeed = []
ySpeed = []
populationSize = 10
radius = 12

for i in range(populationSize):
    x.append(random(0,800))
    y.append(random(0,800))
    xSpeed.append(random(-7.5,7.5))
    ySpeed.append(random(-7.5,7.5))

#ENVIRONMENT

def setup():
    size(1366, 768)
    frameRate(60)
    global pupin, low, havemeyer, mudd, fairchild, northern, uris
    pupin = loadShape("Pupin.svg")
    low = loadShape("Low.svg")
    havemeyer = loadShape("havemeyer.svg")
    mudd = loadShape("mudd.svg")
    fairchild = loadShape("fairchild-schermerhorn.svg")
    northern = loadShape("northern-corner.svg")
    uris = loadShape("uris.svg")
    
    
def draw():
    background(102)
    #Draw at coordinate (x,y) at size (question)
    shape(pupin, 450, 146)
    shape(low, 527, 369)
    shape(havemeyer, 415, 232 )
    shape(mudd, 614, 147)
    shape(fairchild, 613, 181)
    shape(northern, 415, 147)
    shape(uris, 523, 211)

#WATER FOUNTAINS
    fill(0,0,255)
    ellipse(537, 500, 10,10)
    ellipse(597, 500, 10,10)
    
#ZEBRA - need to rethink why this works. 
#the population is not working.
#need to figure out how it shouldn't be able to pass through buildings
    for i in range (populationSize):
        x[i] = x[i] + xSpeed[i]
        y[i] = y[i] + ySpeed[i]
        if (x[i] > width - radius) or (x[i] < radius):
            xSpeed[i] = xSpeed[i] * -1
        if (y[i] > height - radius) or (y[i] < radius):
            ySpeed[i] = ySpeed[i] * -1
    
    noStroke()
    fill(255)
    ellipse(x[i],y[i], 6,6)
    
#HUMAN
    fill(96,120,100)
    rect(80, 80, 8,8)
