import time
from client import RobotClient


robot = RobotClient(address="192.168.0.13")
robot.connect()

Q0 = 0
Q1 = 0
Q2 = 90

robot.set_joints(q0=Q0, q1=Q1, q2=Q2)

def set_origin():
    robot.set_joints(q0=Q0, q1=Q1, q2=Q2)

def look_up ():
    robot.set_joints(q0=Q0, q1=Q1, q2=120)

def look_down():
    robot.set_joints(q0=Q0, q1=-Q1, q2=70)

def rotate_left():
    robot.set_joints(q0=20, q1=Q1, q2=Q2)

def rotate_right():
    robot.set_joints(q0=-20, q1=Q1, q2=Q2)

