from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# スピード
POWER = 50

# 距離の基準を変数にする
SafeDistance = 40   # これより遠いと安全
DangerDistance = 20  # これより近いと危険

try:
    while True:
        # 超音波センサーで目の前の距離を測る
        distance = px.ultrasonic.read()
        
        # 測った距離を見やすく整える（小数点以下2桁まで）
        distance = round(distance, 2)
        
        # 画面に結果を表示
        print("距離:", distance, "cm")
        
        # 距離が0以下 → 測定できないほど遠い！前進
        if distance <= 0:
            print("→ 🔵 めちゃくちゃ遠い！前進します")
            px.forward(POWER)
            sleep(1)
            px.stop()
        
        # 危険な距離なら後退
        elif distance <= DangerDistance:  # 変数を使う
            print("→ 🔴 危険！後退します")
            px.backward(POWER)
            sleep(0.5)
            px.stop()
        
        # 注意が必要な距離なら右に曲がる
        elif distance <= SafeDistance:  # 変数を使う
            print("→ 🟡 注意！右に曲がります")
            px.set_dir_servo_angle(30)
            px.forward(POWER)
            sleep(0.5)
            px.stop()
            px.set_dir_servo_angle(0)
        
        # 安全な距離なら前進
        else:
            print("→ 🟢 安全！前進します")
            px.forward(POWER)
            sleep(1)
            px.stop()

finally:
    px.stop()

# 試してみよう：
# SafeDistance = 40 を SafeDistance = 60 に変更すると、早めに反応します
# DangerDistance = 20 を DangerDistance = 10 に変更すると、ギリギリまで攻めます

