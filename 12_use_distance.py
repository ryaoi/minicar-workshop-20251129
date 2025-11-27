from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 1秒待つ（超音波センサーが安定するため）
sleep(1)

# スピード
Power = 50

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
        
        # もし距離が0より大きく、かつ20cm以内なら、後退
        if distance > 0 and distance <= DangerDistance:
            print("🔴 危険！後退します")
            px.backward(Power)
            sleep(0.5)
            px.stop()

        # そうでなく、もし40cm以内なら、左に曲がる
        elif distance > DangerDistance and distance <= SafeDistance:
            print("🟡 注意！左に曲がります")
            px.set_dir_servo_angle(-30)
            px.forward(Power)
            sleep(0.5)
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