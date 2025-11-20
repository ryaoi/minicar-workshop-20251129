# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# キーボードから入力を受け取る
# 入力した文字がcommand変数に入る
command = input("Enter command (forward/backward): ")

# もしcommandが"forward"なら、前進する
if command == "forward":
    px.forward(50)
    sleep(1)
    px.stop()

# そうでなく、もしcommandが"backward"なら、後退する
elif command == "backward":
    px.backward(50)
    sleep(1)
    px.stop()