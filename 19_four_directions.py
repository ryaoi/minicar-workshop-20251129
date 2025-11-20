# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

print("Commands: w=forward, s=backward, a=left, d=right, q=quit")

# 無限に繰り返す
while True:
    # キーボードから入力を受け取る
    command = input("Enter command: ")
    
    # もしcommandが"w"なら、前進する
    if command == "w":
        px.set_dir_servo_angle(0)
        px.forward(50)
        sleep(0.5)
        px.stop()
    
    # そうでなく、もしcommandが"s"なら、後退する
    elif command == "s":
        px.set_dir_servo_angle(0)
        px.backward(50)
        sleep(0.5)
        px.stop()
    
    # そうでなく、もしcommandが"a"なら、左に曲がる
    elif command == "a":
        px.set_dir_servo_angle(-30)
        px.forward(50)
        sleep(0.5)
        px.stop()
        px.set_dir_servo_angle(0)
    
    # そうでなく、もしcommandが"d"なら、右に曲がる
    elif command == "d":
        px.set_dir_servo_angle(30)
        px.forward(50)
        sleep(0.5)
        px.stop()
        px.set_dir_servo_angle(0)
    
    # そうでなく、もしcommandが"q"なら、終了する
    elif command == "q":
        print("Exit!")
        break