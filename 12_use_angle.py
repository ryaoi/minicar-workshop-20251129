from picarx import Picarx
from time import sleep

px = Picarx()

POWER = 50
SafeDistance = 40
DangerDistance = 20

# 曲がる角度を変数にする
TurnAngle = 30  # タイヤを曲げる角度

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
            px.set_dir_servo_angle(0)
            px.forward(POWER)
            sleep(1)
            px.stop()
        
        elif distance <= DangerDistance:
            print("→ 🔴 危険！後退します")
            px.set_dir_servo_angle(-TurnAngle)  # 変数を使う（左に）
            px.backward(POWER)
            sleep(0.5)
            px.stop()
            px.set_dir_servo_angle(0)
        
        elif distance <= SafeDistance:
            print("→ 🟡 注意！右に曲がります")
            px.set_dir_servo_angle(TurnAngle)  # 変数を使う（右に）
            px.forward(POWER)
            sleep(0.5)
            px.stop()
            px.set_dir_servo_angle(0)
        
        else:
            print("→ 🟢 安全！前進します")
            px.set_dir_servo_angle(0)
            px.forward(POWER)
            sleep(1)
            px.stop()

finally:
    px.stop()

# 試してみよう：
# TurnAngle = 30 を TurnAngle = 15 に変更すると、緩やかに曲がります
# TurnAngle = 30 を TurnAngle = 40 に変更すると、急カーブになります

