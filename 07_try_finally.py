# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# tryとfinallyで安全に実行
try:
    # 繰り返し実行する
    # 止めたいときは Ctrl + C を押す
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
        
        # 少し待つ
        sleep(0.5)

finally:
    # プログラムが終了するときに必ず実行される
    # Ctrl + C で止めても、必ずここが実行されて安全に停止する
    px.stop()
    print("停止しました")

