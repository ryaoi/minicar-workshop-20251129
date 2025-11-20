# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# タイヤを左に向ける
# マイナスの値（-30）で左に曲がる
px.set_dir_servo_angle(-30)

# 前に進む命令
px.forward(50)

# 1秒待つ
# この間、PiCar-Xは左に曲がりながら前進し続ける
sleep(1)

# 止まる命令
px.stop()

# タイヤを真っ直ぐに戻す
px.set_dir_servo_angle(0)