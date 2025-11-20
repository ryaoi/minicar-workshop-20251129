# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# ここに speed = 100 という変数を書いてみましょう


# 変数speedの値を使って前進する
px.forward(speed)

# 1秒待つ
sleep(1)

# 止まる
px.stop()