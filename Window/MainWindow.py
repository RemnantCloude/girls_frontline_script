from pyautogui import click
from random import randint

from general import Delay

# 主界面
## 捷径栏
def MainWindow_Shortcut():
    click(randint(0, 60), randint(483, 590))
    Delay(1, 2)

## 修理
def MainWindow_Restore():
   click(randint(1230, 1536), randint(267, 425))
   Delay(3, 4)

## 研发
def MainWindow_Research():
    click(randint(1230, 1536), randint(458, 617))
    Delay(3, 4)

## 战斗
def MainWindow_Combat():
    click(randint(1230, 1536), randint(650, 851))
    Delay(3, 4)

## 3D宿舍
def MainWindow_3DDormitory():
    click(randint(1580, 1723), randint(244, 400))
    Delay(3, 4)

## 宿舍
def MainWindow_Dormitory():
    click(randint(1701, 1885), randint(244, 400))
    Delay(3, 4)

## 工厂
def MainWindow_Factory():
    click(randint(1580, 1885), randint(435, 590))
    Delay(3, 4)

## 编成
def MainWindow_Formation():
    click(randint(1580, 1885), randint(624, 622))
    Delay(3, 4)