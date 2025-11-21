# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 超音波センサーで目の前の距離を測る
distance = px.ultrasonic.read()

# 測った距離を見やすく整える（小数点以下2桁まで）
distance = round(distance, 2)

# 画面に結果を表示
print("距離:", distance, "cm")

# 距離が0以下 → 測定できないほど遠い！前進
if distance <= 0:
    print("→ めちゃくちゃ遠い！前進します")
    px.forward(50)
    sleep(1)
    px.stop()

# もし距離が40cm以内なら、ストップ
if distance <= 40:
    print("→ 近い！ストップします")
    px.stop()

# それ以外（40cmより遠い）なら、前進
else:
    print("→ 遠い！前進します")
    px.forward(50)
    sleep(1)
    px.stop()

