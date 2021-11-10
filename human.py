from direct import showbase
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase


class human(ShowBase) :
    def __init__(self) :
        super().__init__()

        self.scene = loader.loadModel("env.egg")

        self.scene.reparentTo(self.render)

        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        self.human = Actor("nik-dragon.egg",{"walk":"nik-dragon.egg",
"run":"nik-dragon.egg"})
        self.human.setScale(0.005, 0.005, 0.005)
        self.human.reparentTo(self.render)

        self.human.loop("walk")
        
        posInterval1 = self.human.posInterval(13,Point3(0, -10, 0), startPos=Point3(0, -10, 0))
        posInterval2 = self.human.posInterval(13,Point3(0, -10, 0), startPos=Point3(0, -10, 0))
        hprInterval1 = self.human.hprInterval(3,Point3(180, 0, 0), startHpr=Point3(0, 0, 0))
        hprInterval2 = self.human.hprInterval(3,Point3(0, 0, 0), startHpr=Point3(180, 0, 0))

        self.human = Sequence(posInterval1, hprInterval1, posInterval2, hprInterval2, name=human)
        self.human.loop()

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
        
    def loadMusic(self):
        music = self.loader.loadMusic(All-Out-Attack.mp3)
        music.play()

game = human()
game.run()