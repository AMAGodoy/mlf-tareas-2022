from math import *


def position_to_dof(x, y, z):
    """La función debe recibir (x,y,z) en milimetros y retornar q0, q1 y q2 en grados
    El robot solo entiende grados sexagesimales y enteros"""
    a0, a1 = 94, 125
    a2, a3 = 147, 60.3

    q0 = atan(y/x)
    q2 = acos(((x/cos(q0)-a3)**2+(z-a0)**2-a1**2-a2**2)/(2*a1*a2))
    q1 = pi/2 - atan((z-a0)/(x/cos(q0)-a3)) - atan((a2*sin(q2))/(a1+a2*cos(q2)))

    return int(q0*180/pi), int(q1*180/pi), int(q2*180/pi)


def conversion(q0, q1, q2):
    a0, a1 = 94, 125
    a2, a3 = 147, 60.3
    Q0, Q1, Q2 = radians(q0), radians(q1), radians(q2)

    x = (a1*cos(Q1)+a2*cos(Q1+Q2)+a3)*cos(Q0)
    y = (a1*cos(Q1)+a2*cos(Q1+Q2)+a3)*sin(Q0)
    z = a0+a1*(sin(Q1))+a2*sin(Q1+Q2)

    return x, y, z
