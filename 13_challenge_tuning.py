from picarx import Picarx
from time import sleep

# ========================================
# ここの値を自由に変更してチューニングしよう！
# ========================================

# スピード（10〜100で設定可能）
POWER = 50

# 安全な距離（この距離以上なら安全）
SafeDistance = 40

# 危険な距離（この距離未満は危険）
DangerDistance = 20

# 右に曲がる角度（0〜30で設定可能）
TurnRightAngle = 30

# 左に曲がる角度（-30〜0で設定可能）
TurnLeftAngle = -30

# 注意時の動作時間（秒）
CautionTime = 0.1

# 危険時の動作時間（秒）
DangerTime = 0.5

# ========================================

# PiCar-Xを使えるようにする
px = Picarx()

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
        
        # 安全 → まっすぐ前進
        elif distance >= SafeDistance:
            print("→ 🟢 安全！前進します")
            px.set_dir_servo_angle(0)
            px.forward(POWER)
        
        # 注意 → 右に曲がりながら前進
        elif distance >= DangerDistance:
            print("→ 🟡 注意！右に曲がります")
            px.set_dir_servo_angle(TurnRightAngle)
            px.forward(POWER)
            sleep(CautionTime)
        
        # 危険！ → 左に曲がりながら後退
        else:
            print("→ 🔴 危険！後退します")
            px.set_dir_servo_angle(TurnLeftAngle)
            px.backward(POWER)
            sleep(DangerTime)

finally:
    # 終了時に必ず停止
    px.stop()
    print("停止しました")

