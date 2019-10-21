from pyautogui import click
from random import randint

from Combat_2019_Hallowmas import CombatSet
from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(690, 735), randint(483, 534))

### 机场
def Airport():
    click(randint(1333, 1368), randint(769, 807))

### 路径1
def pot1():
    click(randint(1116, 1142), randint(673, 700))

### 路径2
def pot2():
    click(randint(931, 956), randint(690, 714))
    
### 路径3
def pot3():
    click(randint(1169, 1199), randint(572, 600))

### 两队单人形
def Combat_1():
    # 选择关卡
    CombatSet.ChooseLevel(1)

    # 部署梯队
    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 点击确定，部署梯队
    CombatWindow.Deploy_Confirm()
    # 点击机场
    Airport()
    Delay(1, 2)
    # 点击确定，部署梯队
    CombatWindow.Deploy_Confirm()

    # 开始作战
    CombatWindow.Combat_Start()
    # 点击指挥部2次
    Headquarters()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()
    # 随意点击
    click(randint(1600, 1800), randint(750, 900))
    Delay(0, 1)
    # 点击机场2次
    Airport()
    Delay(1, 2)
    Airport()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()
    # 进入计划模式
    CombatWindow.PlanMode()
    # 规划路径
    pot1()
    Delay(1, 2)
    # 随意点击
    click(randint(1600, 1800), randint(750, 900))
    Delay(0, 1)
    Headquarters()
    Delay(0, 1)
    pot2()
    Delay(1, 2)
    # 随意点击
    click(randint(1600, 1800), randint(750, 900))
    Airport()
    Delay(0, 1)
    pot3()
    Delay(1, 2)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(110, 112)

    # 结算动画
    CombatWindow.Combat_Animation()
    ## 如果有碎片就取消注释
    # click(randint(1800, 1900), randint(750, 900))
    # Delay(1, 2)
    click(randint(1800, 1900), randint(750, 900))
