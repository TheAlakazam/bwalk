import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()
dxl = pypot.dynamixel.DxlIO(ports[0])


def back():
    dxl.set_moving_speed({1:50, 2:50, 3:50, 4:50, 5:50, 6:50, 7:50, 8:50})
    dxl.set_goal_position({1:90, 2:-90, 7:90, 8:-90, 5:-150, 6:150})
    time.sleep(5)
    dxl.set_goal_position({7:0, 8:0, 3:-30, 4:30})
    time.sleep(2)
    dxl.set_goal_position({3:0, 4:0})
    time.sleep(2)
    dxl.set_goal_position({1:0, 2:0, 5:0, 6:0, 7:45, 8:-45})
back()

