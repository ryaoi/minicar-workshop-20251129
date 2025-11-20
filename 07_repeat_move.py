# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 10回繰り返す
for i in range(10):
    # 前に進む
    px.forward(10)
    
    # 0.5秒待つ
    sleep(0.5)
    
    # 止まる
    px.stop()
    
    # 0.5秒待つ
    sleep(0.5)
    
    # ここまでの動作を繰り返す

# 最後に完全に停止
px.stop()