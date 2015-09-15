from parts import *
class Robot:
        def __init__(self, name):
                self.legs = Legs()
                self.arms = Arms()
                self.head = Head()
                self.energy = PowerSupply()
                self.name = name
        def move(self, moves=2):
                for x in range(0,moves):
                        if self.energy.checkPower() == 0:
                                print "Cannot move, no power"
                        else:
                                print self.name + self.legs.walk()
                                self.energy.usePower()
        def checkBattery(self):
                print str(self.energy.power) + " energy remaining"
        def recharge(self):
                self.energy.power = 5
                print "Fully charged"
        def lift(self, stuff):
                if self.energy.checkPower() == 0:
                        print "Cannot lift, no power"
                else:
                        print self.name + self.arms.lift(stuff)
                        self.energy.usePower()
        def openObject(self, stuff):
                if self.energy.checkPower() == 0:
                        print "Cannot open, no power"
                else:
                        print self.name + self.arms.openObject(stuff)
                        self.energy.usePower()
        def run(self):
                if self.energy.checkPower() == 0:
                        print "Cannot run, no power"
                else:
                        print self.name + self.legs.run()
                        self.energy.usePower()
        def walk(self):
                if self.energy.checkPower() == 0:
                        print "Cannot walk, no power"
                else:
                        print self.name + self.legs.walk()
                        self.energy.usePower()
        
        def jump(self):
                if self.energy.checkPower() == 0:
                        print "Cannot jump, no power"
                else:
                        print self.name + self.legs.jump()
                        self.energy.usePower()
        def speak(self, words):
                if self.energy.checkPower() == 0:
                        print "Cannot speak, no power"
                else:
                        print self.name + " says " + self.head.speak(words)
                        self.energy.usePower()

