from picarx import Picarx
from time import sleep

px = Picarx()

sleep(1)

Power = 50
SafeDistance = 40
DangerDistance = 20

# 右に曲がる角度を変数にする
TurnRightAngle = 30  # タイヤを曲げる角度

try:
    while True:
        # 超音波センサーで目の前の距離を測る
        distance = px.ultrasonic.read()
        
        # 測った距離を見やすく整える（小数点以下2桁まで）
        distance = round(distance, 2)
        
        # 画面に結果を表示
        print("距離:", distance, "cm")
        
        # もし距離が0より大きく、かつ20cm以内なら、後退
        if distance > 0 and distance <= DangerDistance:
            print("🔴 危険！後退します")
            px.backward(Power)
            sleep(0.5)
            px.stop()

        # そうでなく、もし40cm以内なら、右に曲がる
        elif distance > DangerDistance and distance <= SafeDistance:
            print("🟡 注意！右に曲がります")
            px.set_dir_servo_angle(TurnRightAngle)
            px.forward(Power)
            sleep(1.7)
            px.stop()
            px.set_dir_servo_angle(0)

        # それ以外（測定できないほど遠い、または40cmより遠い）なら、前進
        else:
            print("🟢 安全！前進します")
            px.forward(Power)
            sleep(1)
            px.stop()

finally:
    px.stop()
