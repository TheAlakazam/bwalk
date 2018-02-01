import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()
dxl = pypot.dynamixel.DxlIO(ports[0])


def back():
    dxl.set_goal_position({5:0, 6:0, 7:18, 8:-18})
    dxl.set_moving_speed({1:100, 2:100, 3:100, 4:100})
    a,b = -25,-35
    c = 40
    dxl.set_goal_position({3:a, 4:b, 1:0})
    time.sleep(0.3)
    dxl.set_goal_position({1:c})
    time.sleep(0.3)
    dxl.set_goal_position({4:0})
    time.sleep(0.8)
    dxl.set_goal_position({3:0, 1:0})
    time.sleep(0.3)
    b,a = 25,35
    dxl.set_goal_position({5:0, 6:0, 7:18, 8:-18})
    c = -40
    dxl.set_goal_position({3:a, 4:b, 2:0})
    time.sleep(0.3)
    dxl.set_goal_position({2:c})
    time.sleep(0.3)
    dxl.set_goal_position({3:0})
    time.sleep(0.8)
    dxl.set_goal_position({2: 0, 4: 0})
    time.sleep(0.3)
    dxl.set_goal_position({1:0, 2:0, 3:0, 4:0})

while True:
    back()

