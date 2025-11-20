# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# ここに command = input("Enter direction (left/right): ") と書いてみましょう


# もしcommandが"left"なら、左に曲がる
if command == "left":
    px.set_dir_servo_angle(-30)
    px.forward(50)
    sleep(1)
    px.stop()
    px.set_dir_servo_angle(0)

# そうでなく、もしcommandが"right"なら、右に曲がる
elif command == "right":
    px.set_dir_servo_angle(30)
    px.forward(50)
    sleep(1)
    px.stop()
    px.set_dir_servo_angle(0)