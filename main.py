# 少女前线自动练级脚本

# 屏幕范围默认为(1920,1080)

from pyautogui import click
import pyautogui
from random import randint  # randint(0,9)
import PIL.Image

from general import Delay
import MainWindow
import CombatWindow
import FormationWindow

import Combat.Combat_02

current_time = int(input())
repeat_time = int(input())
click(randint(400, 500), randint(0, 70))
while current_time < repeat_time: 
    Combat.Combat_02.Combat_02(current_time)
    print(current_time)
    current_time = current_time + 1
    Delay(4, 5)
pyautogui.alert(text='拖完了~欸嘿~', title='', button='OK')

