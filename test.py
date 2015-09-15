from ultraRobot import *
import advancedRobot
import robot
import parts
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
                robot3.control(["walk", "run", "jump", "sleep", "jump", "recharge", "lift rock", "open bag", "say", "move 5", "recharge", "fast move 6"])
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
test1.testArms()
test1.testLegs()
test1.testHead()
test1.testAdvanced()
test1.testControl()
test1.testExplosion()
test1.testAi()
