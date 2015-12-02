"""
tutorial4.py
by E. Dennison
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1665
SCREEN_HEIGHT = 945

class background(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)



class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0



class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    
    def __init__(self, width, height):
        super().__init__(width, height)
        BG = ImageAsset("images/starfield.jpg")
        bgsprite = background(BG, (0,0))
        bgsprite.width = SCREEN_WIDTH
        bgsprite.height = SCREEN_HEIGHT
        SpaceShip((800,450))
        
        
    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
