class Robot():
        def __init__(self, name):
                self.legs = Legs()
                self.arms = Arms()
                self.head = Head()
                self.energy = PowerSupply()
                self.name = name
        def move(self, moves):
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
                        print "Cannot move, no power"
                else:
                        print self.name + self.arms.lift(stuff)
                        self.energy.usePower()
        def openObject(self, stuff):
                if self.energy.checkPower() == 0:
                        print "Cannot move, no power"
                else:
                        print self.name + self.arms.openObject(stuff)
                        self.energy.usePower()
        def run(self):
                if self.energy.checkPower() == 0:
                        print "Cannot move, no power"
                else:
                        print self.name + self.legs.run()
                        self.energy.usePower()
        def walk(self):
                if self.energy.checkPower() == 0:
                        print "Cannot move, no power"
                else:
                        print self.name + self.legs.walk()
                        self.energy.usePower()
        
        def jump(self):
                if self.energy.checkPower() == 0:
                        print "Cannot move, no power"
                else:
                        print self.name + self.legs.jump()
                        self.energy.usePower()
        def speak(self, words):
                if self.energy.checkPower() == 0:
                        print "Cannot speak, no power"
                else:
                        print self.name + " says " + self.head.speak(words)
                        self.energy.usePower()
        
class Legs():
        def walk(self):
                return " walked"
        def jump(self):
                return " jumped"
        def run(self):
                return " ran"

class Arms():
        def lift(self, stuff):
                return " lifted " + stuff
        def openObject(self, stuff):
                return " opened " + stuff
	
class PowerSupply():
        def __init__(self):
                self.power = 5
        def usePower(self):
                if self.power > 0:
                        self.power = self.power - 1
                        if self.power == 0:
                                print "Energy drained"
                else:
                        print "No power remaining"
        
        def checkPower(self):
                return self.power
        
class Head():
	def speak (self, words):
		return words

class AdvancedRobot(Robot):
        def __init__(self, name):
                self.legs = Legs()
                self.arms = Arms()
                self.head = Head()
                self.energy = PowerSupply()
                self.name = name
                self.energy.power = 10
        def moveFast(self, moves):
                for x in range(0,moves):
                        if self.energy.checkPower() == 0:
                                print "Cannot move, no power"
                        else:
                                print self.name + self.legs.run()
                                self.energy.usePower()
                        if self.energy.checkPower() == 0:
                                print "Cannot move, no power"
                        else:
                                print self.name + self.legs.jump()
                                self.energy.usePower()
        def control(self, commands):
                for command in commands:
                        if command == "walk":
                                self.walk()
                        elif command == "run":
                                self.run()
                        elif command == "jump":
                                self.jump()
                        else:
                                print str(command) + " command not found"       
                        
        def showControls(self):
                print "The acceptable commands are walk, run, and jump."
                                
class Test:
        def testArms(self):
                robot1 = Robot("robot1")
                robot1.lift("crate")
                robot1.openObject("cat")
        def testLegs(self):
                robot1 = Robot("robot1")
                robot1.run()
                robot1.walk()
                robot1.jump()
                robot1.move(7)
        def testHead(self):
                robot1 = Robot("robot1")
                robot1.speak("hello")
        def testAdvanced(self):
                robot2 = AdvancedRobot("advancedRobot")
                robot2.moveFast(3)
                robot2.recharge()
                robot2.run()
                robot2.walk()
                robot2.jump()
                robot2.recharge()
                robot2.move(7)
                robot2.recharge()
        def testControl(self):
                robot3 = AdvancedRobot("robo")
                robot3.showControls()
                robot3.control(["walk", "run", "jump", "sleep", "jump", "recharge"])
                
            
test1 = Test()
#test1.testArms()
#test1.testLegs()
#test1.testHead()
#test1.testAdvanced()
test1.testControl()
