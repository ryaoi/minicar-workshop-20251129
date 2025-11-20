from picarx import Picarx
from time import sleep

px = Picarx()

# ここの10を100に変えて実行してみましょう。
px.forward(10)

sleep(0.5)
px.stop()