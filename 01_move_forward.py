# Pythonのプログラムは上から下へ順番に実行されます
# #で始まる行はコメントです。プログラムの動きには影響しません

# PiCar-Xを操作するための道具を準備
from picarx import Picarx  # ミニカーを動かすための機能
from time import sleep     # 時間を待つための機能

# PiCar-Xを使えるようにする
px = Picarx()

# 前に進む命令（10はスピード）
px.forward(10)

# 0.5秒待つ
sleep(0.5)

# 止まる命令
px.stop()
