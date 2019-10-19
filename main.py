# 少女前线自动练级脚本

## 屏幕范围默认为(1920,1080)

import pyautogui
from random import randint

from general import Delay

## 选择关卡
import Combat.Combat_02

current_time = int(input())
repeat_time = int(input())
pyautogui.click(randint(400, 500), randint(0, 70))
while current_time < repeat_time: 
    Combat.Combat_02.Combat_02(current_time)
    print(current_time)
    current_time = current_time + 1
    Delay(2, 3)
pyautogui.alert(text='拖完了~欸嘿~', title='', button='OK')

