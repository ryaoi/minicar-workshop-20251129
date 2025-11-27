from picarx import Picarx
from time import sleep

# ========================================
# ここの値を自由に変更してチューニングしよう！
# ========================================

# スピード（10〜100で設定可能）
Power = 50

# 安全な距離（この距離以上なら安全）
SafeDistance = 50

# 危険な距離（この距離未満は危険）
DangerDistance = 30

# 右に曲がる角度（0〜30で設定可能）
TurnRightAngle = 30

# 注意時の動作時間（秒）
CautionTime = 1.7

# 危険時の動作時間（秒）
DangerTime = 0.5

# ========================================

# PiCar-Xを使えるようにする
px = Picarx()

# 1秒待つ（超音波センサーが安定するため）
sleep(1)

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
            sleep(DangerTime)
            px.stop()

        # そうでなく、もし40cm以内なら、右に曲がる
        elif distance > DangerDistance and distance <= SafeDistance:
            print("🟡 注意！右に曲がります")
            px.set_dir_servo_angle(TurnRightAngle)
            px.forward(Power)
            sleep(CautionTime)
            px.stop()
            px.set_dir_servo_angle(0)

        # それ以外（測定できないほど遠い、または40cmより遠い）なら、前進
        else:
            print("🟢 安全！前進します")
            px.forward(Power)
            sleep(1)
            px.stop()

finally:
    # 終了時に必ず停止
    px.stop()
    print("停止しました")

