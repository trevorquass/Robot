from robot import *
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
