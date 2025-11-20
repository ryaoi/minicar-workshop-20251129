# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep
# リアルタイムでキーを読み取るための道具
import readchar

# PiCar-Xを使えるようにする
px = Picarx()

print("Press keys: w=forward, s=backward, a=left, d=right, q=quit")

# 無限に繰り返す
while True:
    # Enterを押さずにキーを読み取る
    key = readchar.readkey()
    
    # もしkeyが"w"なら、前進する
    if key == "w":
        px.set_dir_servo_angle(0)
        px.forward(80)
        sleep(0.5)
        px.forward(0)
    
    # そうでなく、もしkeyが"s"なら、後退する
    elif key == "s":
        px.set_dir_servo_angle(0)
        px.backward(80)
        sleep(0.5)
        px.forward(0)
    
    # そうでなく、もしkeyが"a"なら、左に曲がる
    elif key == "a":
        px.set_dir_servo_angle(-30)
        px.forward(80)
        sleep(0.5)
        px.forward(0)
    
    # そうでなく、もしkeyが"d"なら、右に曲がる
    elif key == "d":
        px.set_dir_servo_angle(30)
        px.forward(80)
        sleep(0.5)
        px.forward(0)
    
    # そうでなく、もしkeyが"q"なら、終了する
    elif key == "q":
        print("\nExit!")
        break
    
    # タイヤを真っ直ぐに戻す
    px.set_dir_servo_angle(0)