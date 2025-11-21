# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 後ろに進む命令
px.backward(10)

# 0.5秒待つ
sleep(0.5)

# 止まる命令
px.stop()
