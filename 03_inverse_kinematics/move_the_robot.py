import time
from client import RobotClient
from inverse_kinematics import position_to_dof


# Conectarse al robot

r = RobotClient(address="localhost")  # Recuerda usar una dirección válida
r.connect()
r.home()


def move_robot_to_xyz(robot, x, y, z):
    """Función para mover el robot usando cartesianas"""
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)


# Mover el robot (Origen x=185, y=0, z=241; q0 = 0, q1 = 0, q2 = 90)
move_robot_to_xyz(r, x=205, y=-20, z=241)
time.sleep(0.5)
move_robot_to_xyz(r, x=205, y=20, z=241)
time.sleep(0.5)
move_robot_to_xyz(r, x=225, y=20, z=241)
time.sleep(0.5)
move_robot_to_xyz(r, x=225, y=-20, z=241)
time.sleep(0.5)
