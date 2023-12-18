
from numpy import array
from math import cos

def Vanderpol_Oscilator(U,t):
    
    return array([U[1], U[0]-U[0]**3])



def Duffin_Osciliator_2(U,t):
    k = 0.01
    B = 1 
    
    return array ( [U[1], -U[0]**3-k*U[1]+B*cos(t)] )


def Rayleigh_Osocilator(U,t):
    
    f0 = 1
    
    return array([ U[1] , U[0] - U[0]**3 - U[1] + f0*cos(t) ])


def pruebas(U,t):
    
    return -4 * t + U[0]


def pruebas_2(U,t):

    return array(U[1], -U[0])

def pruebas_3(U,t):

    return array([U[1], U[0] - U[0]**2])


def f(t, U):
    
    return array([U[1], U[0]-U[0]**3])


