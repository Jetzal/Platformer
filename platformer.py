
"""
platformer.py
Author: Jett
Credit: *like my brother*
Assignment: (platformer)
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red= Color(0xFE2E64, 1.0)
green = Color(0x5dff00, 1.0)
bluelight = Color(0x81F7F3,1.0)
blue= Color(0x0000ff, 1.0)
white= Color(0xffffff, 1.0)
black= Color(0x000000, 1.0)
thinline = LineStyle(3, red)
blueline = LineStyle(3, blue)
blackline = LineStyle(3, black)
#Walls
class Wall(Sprite):
    wall = RectangleAsset(50, 50, thinline, black)
    def __init__(self, xPos, yPos):
        super().__init__(Wall.wall, (xPos, yPos))
        self.x = xPos
        self.y = yPos
#Sprite
class Ball(Sprite):
    ball = RectangleAsset(30, 30, thinline, white)
    def __init__(self, xPos, yPos):
        super().__init__(Ball.ball, (xPos, yPos))
        self.x = xPos
        self.y = yPos
        self.xvel = 0
        self.yvel = 0
        self.fxcenter = 0.5
        self.fycenter = 0.5
#spring
class spring(Sprite):
    Spring = RectangleAsset(30, 5, blackline, red)
    def __init__(self, xPos, yPos):
        super().__init__(spring.Spring, (xPos, yPos))
        self.x = xPos
        self.y = yPos
#endings sprite
class winner(Sprite):
    win = RectangleAsset(30, 30, blueline, blue)
    def __init__(self, xPos, yPos):
        super().__init__(winner.win, (xPos, yPos))
        self.x = xPos
        self.y = yPos

gravity = 0
Sgravity = 0
#App
class Platformer(App):
    def __init__(self):
        super().__init__()
        self.variablex = 0
        self.variabley = 0
        self.Variableg = 0
        self.spring = 0
        self.winner = 0
        self.Wall = 0
        self.objects =[]
        self.listenKeyEvent('keydown', 'q', self.buildWall)
        self.listenKeyEvent('keydown', 'e', self.buildChara)
        self.listenMouseEvent('mousemove', self.mousemove)
        self.listenKeyEvent('keydown', 'a', self.moveL)
        self.listenKeyEvent('keydown', 'w', self.moveU)
        self.listenKeyEvent('keydown', 'd', self.moveR)
        self.listenKeyEvent('keydown', 's', self.buildSpring)
        self.listenKeyEvent('keydown', 'r', self.buildahh)
        self.listenKeyEvent('keydown', 'p', self.destroyLast)
    #make wall
    def buildWall(self, event):
        x = self.variablex- self.variablex%50
        y = self.variabley- self.variabley%50
        self.Wall = Wall(x-25, y-25)
        self.objects.append(self.Wall)
    #tracks where the  mouse is
    def mousemove(self, event):
        self.variablex = event.x
        self.variabley = event.y
    #make !!!
    def buildahh(self, event):
        if self.winner:
            self.winner.destroy()
        self.winner = winner(self.variablex, self.variabley)
        self.objects.append(self.winner)
    #make Sprite
    def buildChara(self, event):
        global gravity
        if self.Variableg:
            self.Variableg.destroy()
            gravity = 0
        self.Variableg = Ball(self.variablex, self.variabley)
        self.z = self.variablex
        self.objects.append(self.Variableg)
    #make Spring
    def buildSpring(self, event):
        global Sgravity
        self.spring = spring(self.variablex, self.variabley)
        self.objects.append(self.spring)
    #move the Sprite Left
    def moveL(self, event):
        if self.Variableg:
            self.Variableg.x -= 10
            p = self.Variableg.collidingWithSprites(Wall)
            if p:
                self.Variableg.x += 2
    #Up
    def moveU(self, event):
        if self.Variableg:
            global gravity
            if gravity == 0:
                gravity = -7
                p = self.Variableg.collidingWithSprites(Wall)
                if p:
                    self.Variableg.y += 50
    #Right
    def moveR(self, event):
        if self.Variableg:
            self.Variableg.x += 10
            p = self.Variableg.collidingWithSprites(Wall)
            if p:
                self.Variableg.x -= 2
    #Destroy last
    def destroyLast(self, event):
        if self.objects:
            a = self.objects[-1]
            a.destroy()
    #gravity
    def step(self):
        global gravity
        global Sgravity
        if self.spring:
            Sgravity +=0.2
            self.spring.y += Sgravity
            i = self.spring.collidingWithSprites(Wall)
            if i:
                self.spring.y -= Sgravity
                Sgravity = 0
        if self.Variableg:
            gravity +=0.2
            self.Variableg.y += gravity
            p = self.Variableg.collidingWithSprites(Wall)
            o = self.Variableg.collidingWithSprites(spring)
            if p:
                self.Variableg.y -= gravity
                gravity = 0
            if o:
                self.Variableg.y -= gravity
                gravity = -10
        if self.Variableg and winner:
            u = self.Variableg.collidingWithSprites(winner)
            if u:
                print ("winner")
myapp = Platformer()
myapp.run()