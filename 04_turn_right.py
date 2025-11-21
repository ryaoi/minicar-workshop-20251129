# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# タイヤを右に向ける（プラスの値で右）
# ヒント：左は-30だったので、右は+30を使ってみましょう
px.set_dir_servo_angle()  # ここに数字を入れてね！

# 前に進む命令
px.forward(50)

# 1秒待つ
sleep(1)

# 止まる命令
px.stop()

# タイヤを真っ直ぐに戻す
px.set_dir_servo_angle(0)

