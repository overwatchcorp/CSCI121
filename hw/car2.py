def distance(xs):
    distance = (xs[0]**2 + xs[1]**2)**.5
    return distance


class Car:
    def __init__(self, mpg, tank, cash):
        self.mpg = mpg
        self.cash = cash
        self.tank = tank
        self.coords = [0,0]
        self.fuel = tank
    def driveTo(self,x,y):
        fuelcheck = self.fuel - (distance([x - self.coords[0], y - self.coords[1]]))/self.mpg
        if fuelcheck < 0:
             return False
        self.fuel = fuelcheck
        self.coords = [x, y]
        return True
    def getLocation(self):
        return self.coords
    def getGas(self):
        return self.fuel
    def getToFill(self):
        return (self.tank - self.fuel)
    def getMoney(s):
        return s.cash
    def fill(s,p):
        g=s.tank-s.fuel
        r = s.cash-(g*p)
        if r > 0:
            s.fuel = s.tank
            s.cash = r

class GasStation:
    def __init__(s, x, y, p):
        s.x=x
        s.y=y
        s.p=p
    def refillCar(s,c):
        l=c.getLocation()
        d=distance([s.x-l[0],s.y-l[1]])
        if d < .001:
            c.fill(s.p)

