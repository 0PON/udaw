class Car:
    def park(self):
        print("park1")
    def speedup(self):
        print("speed up1")
    def refuel(self):
        print("refuel1")
class lorry(Car):
    def park(self):
        print("park2")
    def speedup(self):
        print("not speed up2")
    def refual(self):
        print("refuel2")
class bike(Car):
    def park(self):
        print("park3")
    def speedup(self):
        print("speedup3")
    def refuel(self):
        print('notrefual3')


a=Car()
b=lorry()
c=bike()

a.park()
b.refual()
c.speedup()