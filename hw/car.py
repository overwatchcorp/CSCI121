def gd(xs):
    gd = (xs[0]**2 + xs[1]**2)**.5
    return gd

class Car:
    def __init__(s, m, t, c):
        s.m = m
        s.c = c
        s.t = t
        s.l = [0,0]
        s.f = t
    def driveTo(s,x,y):
        r=s.f-(gd([x-s.l[0],y-s.l[1]]))/s.m
        if r<0:
             return False
        s.f=r
        s.l=[x, y]
        return True
    def canDriveTo(s, x, y):
        r=s.f-(gd([x-s.l[0],y-s.l[1]]))/s.m
        if r<0:
             return False
        return True
    def getLocation(s):
        return s.l
    def getGas(s):
        return s.f
    def getToFill(s):
        return (s.t - s.f)
    def getMoney(s):
        return s.c
    def fill(s,p):
        g=s.t-s.f
        r=s.c-(g*p)
        if r>0:
            s.f=s.t
            s.c=r

class GasStation:
    def __init__(s, x, y, p):
        s.x=x
        s.y=y
        s.p=p
    def refillCar(s,c):
        l=c.getLocation()
        d=gd([s.x-l[0],s.y-l[1]])
        if d < .001:
            c.fill(s.p)

class Taxi(Car):
    occupied = False
    tripMiles = 0
    def pickup(s):
        if s.occupied:
            return False
        s.occupied = True
        s.tripMiles = 0
        return True
    def getStatus(self):
        return self.occupied
    def driveTo(s,x,y):
        legDistance = gd([x - s.l[0],y - s.l[1]])
        Car.driveTo(s,x,y)
        s.tripMiles += legDistance
    def dropoff(s):
        if s.occupied:
            s.occupied = False
            s.c += 2 + (3 * s.tripMiles)
            return True
        return False

class Dispatcher:
    def __init__ (self):
        self.fleet = []
    def hire (self, newTaxi):
        self.fleet.append(newTaxi)
    def hail(self, x, y):
        avaliableTaxis = [t for t in self.fleet if t.getStatus() == False]
        taxisInRange = [t for t in avaliableTaxis if t.canDriveTo(x, y) == True]
        closestTaxi = None
        closestTaxiDistance = float('inf')
        if len(taxisInRange) > 0:
            for t in taxisInRange:
                location = t.getLocation()
                distanceFromPickup = gd([x - location[0],y - location[1]])
                if distanceFromPickup < closestTaxiDistance:
                    closestTaxi = t
                    closestTaxiDistance = distanceFromPickup
            closestTaxi.driveTo(x, y)
            closestTaxi.pickup()
            return closestTaxi
        return None

