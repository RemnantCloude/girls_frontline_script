# 少女前线自动练级脚本

# 屏幕范围默认为(1920,1080)

# 主界面

import pyautogui
import time
import random # random.randint(0,9)

import general
import MainWindow
import CombatWindow
import FormationWindow
import Combat_02

# a = input()
# b = input()
# Combat_02.Combat_02(int(a),int(b))
a = input()
Combat_02.Combat_02(int(a[0]),int(a[1]))
