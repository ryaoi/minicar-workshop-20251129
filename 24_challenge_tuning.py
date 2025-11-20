from picarx import Picarx
import time

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

def main():
    try:
        px = Picarx()
       
        while True:
            # 距離を測る
            distance = round(px.ultrasonic.read(), 2)
            print("distance: ", distance)
            
            # 安全 → まっすぐ前進
            if distance >= SafeDistance:
                px.set_dir_servo_angle(0)
                px.forward(POWER)
            
            # 注意 → 右に曲がりながら前進
            elif distance >= DangerDistance:
                px.set_dir_servo_angle(TurnRightAngle)
                px.forward(POWER)
                time.sleep(CautionTime)
            
            # 危険！ → 左に曲がりながら後退
            else:
                px.set_dir_servo_angle(TurnLeftAngle)
                px.backward(POWER)
                time.sleep(DangerTime)

    finally:
        # 終了時に必ず停止
        px.stop()

if __name__ == "__main__":
    main()
