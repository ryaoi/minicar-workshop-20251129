# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 無限に繰り返す
while True:
    # 前に進む
    px.forward(10)
    
    # 0.5秒待つ
    sleep(0.5)
    
    # ここをpx.backward(10)に変更してみましょう
    px.stop()
    
    # 0.5秒待つ
    sleep(0.5)