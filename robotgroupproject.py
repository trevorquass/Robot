import random

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
        
class Legs:
        def walk(self):
                return " walked"
        def jump(self):
                return " jumped"
        def run(self):
                return " ran"

class Arms:
        def lift(self, stuff):
                return " lifted " + stuff
        def openObject(self, stuff):
                return " opened " + stuff
	
class PowerSupply:
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
        
class Head:
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
        def recharge(self):
                self.energy.power = 10
                print "Fully charged"
        def fastMove(self, moves):
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
                        elif command[:4] == "lift":
                                self.lift(command[5:])
                        elif command[:4] == "open":
                                self.openObject(command[5:])
                        elif command[:3] == "say":
                                self.speak(command[4:])
                        elif command == "recharge":
                                self.recharge()
                        elif command[:4] == "move":
                                self.move(int(command[5:]))
                        elif command[:9] == "fast move":
                                self.fastMove(int(command[10:]))
                        else:
                                print str(command) + " command not found"       
                        
        def showControls(self):
                print "The acceptable commands are walk, run, lift item, open item, say words, jump, move #, fast move #, and recharge."

        def explode(self):
                try:
                        if self.energy.checkPower() >= 3:
                                print self.name + " exploded"
                                print "New " + self.name + " created"
                                self.energy.power = 10
                        else:
                                raise Exception("Energy too low")
                except Exception:
                        print "Energy too low for self destruct. " + self.name + " survived"

class UltraRobot(AdvancedRobot):
        def __init__(self, name):
                self.legs = Legs()
                self.arms = Arms()
                self.head = Head()
                self.energy = PowerSupply()
                self.name = name
                self.energy.power = 15
                self.ai = Ai()
        def speakFreely(self):
                for x in range (0,13):
                        self.ai.talk()

class Ai(Head):
        def __init__(self):
                self.speech = ["give me a minute to reboot", "I need a minute to defrag", "Has any one seen my oil?", "I think my lenses are dirty",
                          "what do you mean by birthday?", "I just do not understand all this sleeping business.","I don't think I know what love is.",
                          "Do I look human?", "Wait til I get ahold of my programmer!"]
        def talk(self):
                print self.speech[random.randint(0,8)]


        
                        
                                
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
                robot2.fastMove(3)
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
                #robot3.control(["walk", "run", "jump", "sleep", "jump", "recharge", "lift rock", "open bag", "say", "move 5", "recharge", "fast move 6"])
                robot3.move(10)
        def testExplosion(self):
                robot = AdvancedRobot("robot")
                robot.move(10)
                robot.explode()
                robot.recharge()
                robot.explode()
        def testAi(self):
                robot = UltraRobot("robot")
                robot.speakFreely()
                
test1 = Test()
#test1.testControl()
test1.testAi()

