from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# スピードを変数にする
POWER = 50

# try と finally で安全に実行
try:
    # 無限に繰り返す
    while True:
        # 超音波センサーで目の前の距離を測る
        distance = px.ultrasonic.read()
        
        # 測った距離を見やすく整える（小数点以下2桁まで）
        distance = round(distance, 2)
        
        # 画面に結果を表示
        print("距離:", distance, "cm")
        
        # もし20cm以内なら、後退
        if distance <= 20:
            print("→ 🔴 危険！後退します")
            px.backward(POWER)  # POWERを使う
            sleep(0.5)
            px.stop()
        
        # そうでなく、もし40cm以内なら、右に曲がる
        elif distance <= 40:
            print("→ 🟡 注意！右に曲がります")
            px.set_dir_servo_angle(30)
            px.forward(POWER)  # POWERを使う
            sleep(0.5)
            px.stop()
            px.set_dir_servo_angle(0)
        
        # それ以外は前進
        else:
            print("→ 🟢 安全！前進します")
            px.forward(POWER)  # POWERを使う
            sleep(1)
            px.stop()

finally:
    # 終了時に必ず停止
    px.stop()

# 試してみよう：POWER = 50 を POWER = 80 に変更すると、速く動きます！

