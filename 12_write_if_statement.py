# PiCar-Xを操作するための道具を準備
from picarx import Picarx
from time import sleep

# PiCar-Xを使えるようにする
px = Picarx()

# 命令を変数に入れる
command = "backward"

# ここに if command == "backward": というif文を書いてみましょう


    # もしcommandが"backward"なら、後退する
    px.backward(50)
    sleep(1)
    px.stop()