# ポチる場所を確認する用
# 実行するとカーソルの座標が出力されるので、それをpoti.jsonに設定する

import pyautogui
import time

time.sleep(1)

x, y = pyautogui.position()
print(f"({x}, {y})")
