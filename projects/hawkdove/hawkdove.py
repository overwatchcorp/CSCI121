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
injurycost     = 10   # Cost of losing a fight  
displaycost    = 1   # Cost of displaying between two passive birds  
foodbenefit    = 8   # Value of the food being fought over   
init_hawk      = 0
init_dove      = 0
init_defensive = 0
init_evolving  = 150

########
# Your code here
########
class World:
    def __init__ (self):
        self.birds = []
    def update (self):
        [bird.update() for bird in self.birds ]
    def free_food (self, n):
        if len(self.birds) > 0:
            [ self.birds[random.randint(0, len(self.birds) - 1)].eat() for x in range(0, n) ]
    def conflict (self, n):
        if len(self.birds) > 0: 
            for x in range(0, n):
                bird1n = random.randint(0, len(self.birds) - 1)
                bird1 = self.birds[bird1n]
                bird2n = bird1n
                while bird2n == bird1n:
                    bird2n = random.randint(0, len(self.birds) - 1)
                bird2 = self.birds[bird2n]
                bird1.encounter(bird2)
    def status(self):
        birdStatuses = {}
        for bird in self.birds:
            if bird.species in birdStatuses:
                birdStatuses[bird.species] += 1
            else:
                birdStatuses[bird.species] = 1
        print(birdStatuses)
    def evolvingPlot(self):
        weights = []
        agressions = []
        for bird in self.birds:
            weights.append(bird.weight)
            agressions.append(bird.agression)
        plot(weights, agressions)

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

### bird helper functions ###

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

### bird species ###

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
        elif othersAction == True and myAction == True:
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

class Defensive(Bird):
    species = 'Defensive'
    def Update(self):
        Dove.update(self)
    def defend_choice(self):
        return True
    def encounter(self, other):
        Dove.encounter(self, other)

# keeps value within min and max bounds
def clip(n, minVal, maxVal):
    if n >= maxVal:
        return maxVal
    elif n <= minVal:
        return minVal
    else:
        return n

class Evolving(Bird):
    species = 'Evolving'
    def __init__ (self, world, a, w):
        Bird.__init__(self, world)
        if w == None:
            self.weight = random.uniform(1.0, 3.0)
        else:
            weightMod = random.uniform(-0.1, 0.1)
            self.weight = clip(w + weightMod, 1.0, 3.0)

        if a == None:
            self.agression = random.uniform(0.0, 1.0)
        else:
            agressionMod = random.uniform(-0.1, 0.1)
            self.agression = clip(a + agressionMod, 0.0, 1.0)

    def update (self):
        self.health -= 0.4 + 0.6 * self.weight
        if self.health <= 0:
            self.die()
        # evolution
        if self.health >= 200:
            self.health -= 100
            self.world.birds.append(Evolving(self.world, self.agression, self.weight))
    def defend_choice(self):
        choice = random.random()
        if choice > self.agression:
            return True
        else:
            return False
    def encounter(self, other):
        othersAction = other.defend_choice()
        myAction = self.defend_choice()
        if myAction == True and othersAction == True:
            myOdds = self.weight / (self.weight + other.weight)
            outcome = random.random()
            if myOdds > outcome:
                self.eat()
                other.injured()
            else:
                other.eat()
                self.injured()
        elif myAction == True and othersAction == False:
            self.eat()
        elif myAction == False and othersAction == True:
            other.eat()
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
w.evolvingPlot()    # This line adds a plot of evolving birds. Uncomment it when needed.


