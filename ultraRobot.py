from advancedRobot import *
import random
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
