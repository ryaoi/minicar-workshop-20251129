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
    
    # ここに"a"（左）の制御を書いてみましょう
    # elif command == "a": で始めて、タイヤを-30度にして前進


    
    # ここに"d"（右）の制御を書いてみましょう
    # elif command == "d": で始めて、タイヤを30度にして前進


    
    # そうでなく、もしcommandが"q"なら、終了する
    elif command == "q":
        print("Exit!")
        break