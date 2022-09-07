import time
from client import RobotClient


robot = RobotClient(address="localhost")
robot.connect()

robot.move_xyz(x=230, y=0, z=250)
time.sleep(1)
robot.move_xyz(x=250, y=0, z=250)
time.sleep(1)
robot.move_xyz(x=230, y=-10, z=250)
time.sleep(1)
robot.move_xyz(x=230, y=0, z=260)