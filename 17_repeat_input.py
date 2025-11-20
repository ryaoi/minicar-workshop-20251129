# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

print("Commands: w=forward, s=backward")

# 無限に繰り返す
while True:
    # キーボードから入力を受け取る
    command = input("Enter command: ")
    
    # もしcommandが"w"なら、前進する
    if command == "w":
        px.forward(50)
        sleep(0.5)
        px.stop()
    
    # そうでなく、もしcommandが"s"なら、後退する
    elif command == "s":
        px.backward(50)
        sleep(0.5)
        px.stop()