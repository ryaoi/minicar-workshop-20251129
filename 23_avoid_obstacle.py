from picarx import Picarx
import time

# スピード
POWER = 50

# 安全な距離（40cm以上なら安全）
SafeDistance = 40

# 危険な距離（20cm以下は危険）
DangerDistance = 20

def main():
    try:
        px = Picarx()
       
        while True:
            # 距離を測る
            distance = round(px.ultrasonic.read(), 2)
            print("distance: ", distance)
            
            # 40cm以上なら安全 → まっすぐ前進
            if distance >= SafeDistance:
                px.set_dir_servo_angle(0)
                px.forward(POWER)
            
            # 20cm以上40cm未満 → 注意 → 右に曲がりながら前進
            elif distance >= DangerDistance:
                px.set_dir_servo_angle(30)
                px.forward(POWER)
                time.sleep(0.1)
            
            # 20cm未満 → 危険！ → 左に曲がりながら後退
            else:
                px.set_dir_servo_angle(-30)
                px.backward(POWER)
                time.sleep(0.5)

    finally:
        # 終了時に必ず停止
        px.stop()

if __name__ == "__main__":
    main()