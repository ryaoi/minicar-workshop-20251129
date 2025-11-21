# Pythonのプログラムは上から下へ順番に実行されます
# #で始まる行はコメントです。プログラムの動きには影響しません

# 必要な機能を読み込む（インポートする）
from picarx import Picarx  # ミニカーを動かすための機能
import time                # 時間を扱うための機能


# ミニカーのオブジェクトを作る
px = Picarx()

# カメラを左右に動かす（パン）
# 0度から35度まで少しずつ動かす（右へ）
for angle in range(0, 35):
    px.set_cam_pan_angle(angle)
    time.sleep(0.01)  # 0.01秒待つ
    
# 35度から-35度まで動かす（右から左へ）
for angle in range(35, -35, -1):
    px.set_cam_pan_angle(angle)
    time.sleep(0.01)
    
# -35度から0度に戻す（左から中央へ）
for angle in range(-35, 0):
    px.set_cam_pan_angle(angle)
    time.sleep(0.01)

# カメラを上下に動かす（チルト）
# 0度から35度まで動かす（上へ）
for angle in range(0, 35):
    px.set_cam_tilt_angle(angle)
    time.sleep(0.01)
    
# 35度から-35度まで動かす（上から下へ）
for angle in range(35, -35,-1):
    px.set_cam_tilt_angle(angle)
    time.sleep(0.01)
    
# -35度から0度に戻す（下から中央へ）
for angle in range(-35, 0):
    px.set_cam_tilt_angle(angle)
    time.sleep(0.01)

# ミニカーを停止する
px.stop()
time.sleep(0.2)  # 少し待ってから終了