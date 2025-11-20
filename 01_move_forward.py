# PiCar-Xを操作するための道具を準備
# picarxからPicarxという機能を読み込む
from picarx import Picarx

# timeからsleepという機能を読み込む（待つための機能）
from time import sleep

# PiCar-Xを使えるようにする
# pxという名前でPiCar-Xを呼び出せるようになる
px = Picarx()

# 前に進む命令
# カッコの中の10はスピードの値（大きいほど速い）
px.forward(10)

# 0.5秒待つ
# この間、PiCar-Xは前進し続ける
sleep(0.5)

# 止まる命令
# この命令がないとPiCar-Xは動き続けてしまう
px.stop()