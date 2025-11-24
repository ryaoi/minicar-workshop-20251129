# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 1秒待つ（超音波センサーが安定するため）
sleep(1)

# 超音波センサーで目の前の距離を測る
distance = px.ultrasonic.read()

# 測った距離を見やすく整える（小数点以下2桁まで）
distance = round(distance, 2)

# 画面に結果を表示
print("距離:", distance, "cm")

