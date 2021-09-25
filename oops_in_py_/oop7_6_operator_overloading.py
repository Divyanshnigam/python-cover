class vehicle(object):
    def __init__(self,speed,maxspeed,colour):
        self.speed=speed
        self.maxspeed=maxspeed
        self.colour=colour
    def __str__(self):
        return str(self.speed) + " " + str(self.maxspeed) + self.colour
red_car = vehicle(10,200,"red")

print(red_car.speed)
print(red_car.maxspeed)
print(red_car.colour)
