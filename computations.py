from numpy import *


def euclid_dist3D(planet1,planet2):
    return sqrt((planet1.x-planet2.x)**2+(planet1.y-planet2.y)**2+(planet1.z-planet2.z)**2)
def euclid_dist2D(planet1,planet2):
    return sqrt((planet1.x-planet2.x)**2+(planet1.y-planet2.y)**2)

def get_z_comp(planet1,planet2,force):
        return force * (planet2.z-planet1.z)/euclid_dist3D(planet1,planet2)

def get_x_comp(planet1,planet2,force):
    vertical_cos = euclid_dist2D(planet1,planet2)/euclid_dist3D(planet1,planet2)
    horizontal_cos = (planet2.x-planet1.x)/euclid_dist2D(planet1,planet2)
    return force * vertical_cos * horizontal_cos

def get_y_comp(planet1,planet2,force):
    vertical_cos = euclid_dist2D(planet1,planet2)/euclid_dist3D(planet1,planet2)
    horizontal_sin = (planet2.y-planet1.y)/euclid_dist2D(planet1,planet2)
    return force * vertical_cos * horizontal_sin

def get_attraction(planet1,planet2):
    G = 1 #6.67e-11

    return G * planet1.mass * planet2.mass / (euclid_dist3D(planet1,planet2)**2)