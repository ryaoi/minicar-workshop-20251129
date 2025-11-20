# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# speedという名前の箱に10という数字を入れる
# この箱のことを「変数」と呼ぶ
speed = 10

# 変数speedの値を使って前進する
px.forward(speed)

# 1秒待つ
sleep(1)

# 止まる
px.stop()