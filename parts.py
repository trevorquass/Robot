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
