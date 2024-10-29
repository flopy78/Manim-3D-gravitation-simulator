from manim import *
from dirConstants import  *
from computations import *

class Planet:
    def __init__(self,scene,id,mass,x0,y0,z0,vx0=0,vy0=0,vz0=0,color=GREEN,collide_coeff=0.9):
        self.id = id
        self.mass = mass
        self.x = x0
        self.y = y0
        self.z = z0
        self.radius = 0.2*self.mass
        self.mobject = Sphere(radius = self.radius,resolution = (20,20))
        self.mobject.set_color(color)
        self.mobject.move_to(XFW*self.x + YFW*self.y + ZFW * self.z)
        scene.add(self.mobject)
        #self.text = Text(XFW*self.x + YFW*self.y + ZFW * self.z)
        #self.text.move_to(RIGHT*self.x + UP*self.y)
        #scene.add(self.text)
        self.vx = vx0
        self.vy = vy0
        self.vz = vz0
        self.collide_coeff = collide_coeff
        
    def update_v(self,planets,dt):
        forceX = 0
        forceY = 0
        forceZ = 0

        for planet in planets:
            if planet.id != self.id:
                dist = euclid_dist3D(self,planet)
                if dist > 0:
                    attraction = get_attraction(self,planet)
                    forceX += get_x_comp(self,planet,attraction)
                    forceY += get_y_comp(self,planet,attraction)
                    forceZ += get_z_comp(self,planet,attraction)
        self.vx += (forceX/self.mass)*dt
        self.vy += (forceY/self.mass)*dt
        self.vz += (forceZ/self.mass)*dt
    
    def collide(self,planets):
        for planet in planets:
            if planet.id != self.id:
                if euclid_dist3D(self,planet) <= (self.radius + planet.radius):
                    self.vx,self.vy,self.vz = -self.vx*self.collide_coeff,-self.vy*self.collide_coeff,-self.vz*self.collide_coeff

    def update_pos(self,dt):
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.z += self.vz*dt
        self.mobject.move_to(XFW*self.x + YFW*self.y + ZFW * self.z)
        #self.text.move_to(RIGHT*self.x + UP*self.y)
    