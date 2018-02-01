import pypot.dynamixel
import time
from bluedot import BlueDot
from signal import pause


ports = pypot.dynamixel.get_available_ports()
print(ports)

dxl = pypot.dynamixel.DxlIO(ports[0])

dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})

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

def left():
    dxl.set_goal_position({5:0, 6:0, 7:18, 8:-18})
    a,b = -25,-35
    dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})
    c = 55
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
    c = -55
    dxl.set_goal_position({3:a, 4:b})
    time.sleep(1)
    dxl.set_goal_position({2:c})
    time.sleep(1)
    dxl.set_goal_position({3:0})
    time.sleep(1)
    dxl.set_goal_position({2: 0, 4: 0})
    time.sleep(1)


def forward():
    dxl.set_goal_position({1:0,2:0,3:0,4:0, 5:-117, 6:117})
    dxl.set_goal_position({7:70,8:-70})
    c,d=-27,-27
    a,b=-22,-22
    for i in range(5):
        dxl.set_moving_speed({1:100,2:100,3:100,4:100})
        dxl.set_goal_position({3:a,4:b})
        time.sleep(0.3)
        a,b=-a,-b
        dxl.set_goal_position({1:c,2:d})
        c,d=-c,-d
        time.sleep(0.3)
        dxl.set_goal_position({1:0,2:0,3:0,4:0})

def dpad(pos):
    if pos.top:
        forward()
    elif pos.bottom:
        i = 5
        while i:
            back()
            i-=1
    elif pos.left:
        left()
    elif pos.right:
        right()
    elif pos.middle:
        print("fire")
bd = BlueDot()
bd.when_pressed = dpad
pause()
