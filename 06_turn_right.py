# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# タイヤを右に向ける
# ここの-30を30に変更して実行してみましょう
px.set_dir_servo_angle(-30)

# 前に進む命令
px.forward(50)

# 1秒待つ
sleep(1)

# 止まる命令
px.stop()

# タイヤを真っ直ぐに戻す
px.set_dir_servo_angle(0)