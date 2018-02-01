import pypot.dynamixel
import time
from bluedot import BlueDot
from signal import pause


ports = pypot.dynamixel.get_available_ports()
print(ports)

dxl = pypot.dynamixel.DxlIO(ports[0])

dxl.set_goal_position({1:0, 2:0, 3:0, 4:0, 5: 180, 6:-117
                       , 7:70, 8:-70})
dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})

def left():
    dxl.set_goal_position({5:0, 6:0, 7:18, 8:-18})
    a,b = -25,-35
    dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})
    c = 65
    dxl.set_goal_position({3:a, 4:b})
    time.sleep(1)
    dxl.set_goal_position({1:c})
    time.sleep(1)
    dxl.set_goal_position({4:0})
    time.sleep(1)
    dxl.set_goal_position({1: 0, 3: 0})
    time.sleep(1)

def right():
    b,a = 25,35
    dxl.set_goal_position({5:0, 6:0, 7:18, 8:-18})
    dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})
    c = -45
    dxl.set_goal_position({3:a, 4:b})
    time.sleep(1)
    dxl.set_goal_position({2:c})
    time.sleep(1)
    dxl.set_goal_position({3:0})
    time.sleep(1)
    dxl.set_goal_position({2: 0, 4: 0})
    time.sleep(1)
def dpad(pos):
    if pos.top:
        print("Up")
    elif pos.bottom:
        print("Down")
    elif pos.left:
        left()
    elif pos.right:
        right()
    elif pos.middle:
        print("fire")

left()
bd = BlueDot()
bd.when_pressed = dpad
pause()
