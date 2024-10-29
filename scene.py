from manim import *
from numpy import *
from planet import Planet
from computations import *


class Planets3D(ThreeDScene):
    def construct(self):

        #axes = ThreeDAxes()
        #self.add(axes)
        self.set_camera_orientation(theta=110 *DEGREES,phi=45*DEGREES,zoom=0.5)
        planets = [Planet(self,0,10,0,0,0,color=BLUE,collide_coeff=0.9),Planet(self,1,1,3,0,0,vy0=2.5,color=GREEN,collide_coeff=0.9)]#,Planet(self,2,2,-2,1,-3,color=RED,collide_coeff=0.9)]

        #time interval between two images
        dt = 0.1
        #total duration of the animation
        duration = 2

        t = 0
        while t <= duration:
            for planet in planets:
                planet.update_v(planets,dt)
            
            for planet in planets:
                planet.collide(planets)
            
            for planet in planets:
                planet.update_pos(dt)
            self.wait(dt)
            t += dt