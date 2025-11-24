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

# 距離が0以下 → 測定できないほど遠い！前進
if distance <= 0:
    print("→ 🔵 めちゃくちゃ遠い！前進します")
    px.forward(50)
    sleep(1)
    px.stop()

# もし20cm以内なら、後退
elif distance <= 20:
    print("→ 🔴 危険！後退します")
    px.backward(50)
    sleep(0.5)
    px.stop()

# そうでなく、もし40cm以内なら、右に曲がる
elif distance <= 40:
    print("→ 🟡 注意！右に曲がります")
    px.set_dir_servo_angle(30)
    px.forward(50)
    sleep(0.5)
    px.stop()
    px.set_dir_servo_angle(0)

# それ以外（40cmより遠い）なら、前進
else:
    print("→ 🟢 安全！前進します")
    px.forward(50)
    sleep(1)
    px.stop()

