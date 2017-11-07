import random
import tkinter
random.seed()

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') # Was 350 x 280
    c.grid()
    # Create the x-axis.
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    # Create the y-axis.
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    # Plot the points.
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

# Constants: setting these values controls the parameters of your experiment.
injurycost     = 1   # Cost of losing a fight  
displaycost    = 1   # Cost of displaying between two passive birds  
foodbenefit    = 1   # Value of the food being fought over   
init_hawk      = 0
init_dove      = 0
init_defensive = 0
init_evolving  = 0

########
# Your code here
########
class World:
    def __init__ (self):
        self.birds = []
    def update (self):
        [bird.update() for bird in self.birds ]
    def free_food (self, n):
        [ self.birds[random.randint(0, len(self.birds))].eat() for x in range(0, n) ]

class Bird:
    def __init__ (self, world):
        self.health = 100
        self.world = world
        world.birds.append(self)
    def eat (self):
        self.health += foodbenefit
    def injured (self):
        self.health -= injurycost
    def display (self):
        self.health -=  displaycost
    def die (self):
        self.world.birds.remove(self)
    def update (self):
        # health lost to burning calories
        self.health -= 1
        if self.health <= 0:
            self.die()

def birdUpdate(self):
    Bird.update(self)
    if self.health >= 200:
        self.health -= 100
        return True

def randomEat(self, other):
    self.display()
    other.display()
    randomBird = random.randint(0, 1)
    if randomBird == 1:
        self.eat()
    else:
        other.eat()
    return randomBird

class Hawk (Bird):
    species = 'Hawk'
    def update (self):
        shouldReplicate = birdUpdate(self)
        if shouldReplicate == True:
            self.world.birds.append(Hawk(self.world))
    def defend_choice (self):
        return True
    def encounter (self, other):
        othersAction = other.defend_choice()
        myAction = self.defend_choice()
        if othersAction == False and myAction == False:
            randomEat(self, other)
        elif othersAction == True and myAction == True):
            # same as if neither defends, but they fight
            winner = randomEat(self, other)
            # if winner == 1, self eats, other looses
            # else other eats, self looses
            if winner == 1:
                other.injured()
            else:
                self.injured()
        elif myAction == True:
            self.eat()
        else:
            other.eat()

class Dove (Bird):
    species = 'Dove'
    def update (self):
        shouldReplicate = birdUpdate(self)
        if shouldReplicate == True:
            self.world.birds.append(Dove(self.world))
    def defend_choice (self):
        return False
    def encounter (self, other):
        othersAction = other.defend_choice()
        myAction = self.defend_choice()
        if othersAction == True:
            other.eat()
        # we can use else, since a dove will always choose False
        else:
            randomEat(self, other)


########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########
w = World()
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w,None,None)

for t in range(10000):
    w.free_food(10)
    w.conflict(50)
    w.update()
w.status()
#w.evolvingPlot()    # This line adds a plot of evolving birds. Uncomment it when needed.


