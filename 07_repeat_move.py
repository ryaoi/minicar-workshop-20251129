# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 無限に繰り返す
# Trueは「真（本当）」という意味で、常に繰り返し続ける
while True:
    # 前に進む
    px.forward(10)
    
    # 0.5秒待つ
    sleep(0.5)
    
    # 止まる
    px.stop()
    
    # 0.5秒待つ
    sleep(0.5)
    
    # ここまでの動作を繰り返す