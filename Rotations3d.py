# All of the rotation transformations on one file for convenience

import numpy as np

def rot3x(coor, th):
    rott = np.array([[1, 0, 0], [0, np.cos(th), -np.sin(th)], 
                     [0, np.sin(th), np.cos(th)]])
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def rot3y(coor, th):
    rott = np.array([[np.cos(th), 0, np.sin(th)], [0, 1, 0], 
                      [-np.sin(th), 0, np.cos(th)]])
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor

def rot3z(coor, th):
    rott = np.array([[np.cos(th), -np.sin(th), 0], 
                      [np.sin(th), np.cos(th), 0], [0, 0, 1]])
    coor = coor[:,np.newaxis]
    coor = rott @ coor
    coor = coor[:,0]
    return coor
