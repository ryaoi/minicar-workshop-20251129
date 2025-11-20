# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 命令を変数に入れる
command = "left"

# もしcommandが"right"なら、右に曲がる
if command == "right":
    px.set_dir_servo_angle(30)
    px.forward(50)
    sleep(1)
    px.stop()
    px.set_dir_servo_angle(0)

# ここに elif command == "left": というelifを書いてみましょう


    # もしcommandが"left"なら、左に曲がる
    px.set_dir_servo_angle(-30)
    px.forward(50)
    sleep(1)
    px.stop()
    px.set_dir_servo_angle(0)