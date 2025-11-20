# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 10回繰り返す
for i in range(10):
    # 超音波センサーで距離を測る（単位：cm）
    distance = px.ultrasonic.read()
    
    # 小数点以下2桁に丸める
    distance = round(distance, 2)
    
    # 画面に表示
    print("Distance:", distance, "cm")
    
    # 0.5秒待つ
    sleep(0.5)