import time
from client import RobotClient
from inverse_kinematics import position_to_dof


# Conectarse al robot
r = RobotClient(address="192.168.0.13")
r.connect()
r.home()


r = RobotClient(address="127.0.0.1")
r.connect()
r.home()


def move_robot_to_xyz(robot, x, y, z):
    """Función para mover el robot usando cartesianas"""
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)


# Mover el robot (Origen x=185, y=0, z=241; q0 = 0, q1 = 0, q2 = 90)
move_robot_to_xyz(r, x=185, y=0, z=180)
time.sleep(1)
move_robot_to_xyz(r, x=220, y=0, z=180)
time.sleep(1)
move_robot_to_xyz(r, x=230, y=0, z=180)
time.sleep(1)
move_robot_to_xyz(r, x=200, y=0, z=180)
time.sleep(1)
move_robot_to_xyz(r, x=190, y=0, z=180)
time.sleep(1)
time.sleep(1)
