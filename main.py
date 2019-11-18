# 少女前线脚本

## 屏幕范围默认为(1920,1080)

import pyautogui
from random import randint
from general import Delay

## 选择关卡
from Combat import Combat_02
from Combat import Combat_26

from Combat_Linkage_GloryDay import Combat_11
from Combat_Linkage_GloryDay import Combat_21

current_time = int(input())
repeat_time = int(input())
pyautogui.click(randint(400, 500), randint(0, 70))
while current_time < repeat_time:
    ### 02拖尸练级
    Combat_02.Combat_02(current_time)
    ### 每周boss任务
    # Combat_26.Combat_26()
    # Combat_11.Combat_11()
    print(current_time)
    current_time = current_time + 1
    Delay(2, 3)
pyautogui.alert(text='拖完了~欸嘿~', title='', button='OK')