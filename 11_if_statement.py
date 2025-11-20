# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 命令を変数に入れる
command = "forward"

# もしcommandが"forward"なら、前進する
if command == "forward":
    px.forward(50)
    sleep(1)
    px.stop()