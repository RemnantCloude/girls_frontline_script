from pyautogui import click
from random import randint

from Window import FormationWindow
from Window import CombatWindow
from general import Delay

### 指挥部
def Headquarters():
    click(randint(1246, 1296),randint(520, 565))

### 机场
def Airport():
    click(randint(993, 1036), randint(610, 655))
    
### 路径1
def pot1():
    click(randint(950, 976), randint(734, 759))
    
### 路径2
def pot2():
    click(randint(844, 895), randint(940, 990))

### 3-4E
def Combat_34e():
    # 选择关卡
    CombatWindow.ChooseLevel(4)

    # 点击机场
    Airport()
    Delay(1, 2)
    # 点击确定，部署打手队
    CombatWindow.Deploy_Confirm()
    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 点击确定，部署狗粮队
    CombatWindow.Deploy_Confirm()

    # 开始作战
    CombatWindow.Combat_Start()
    # 点击梯队2次
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
    Delay(0, 1)
    pot2()
    Delay(0, 1)
    # 执行计划
    CombatWindow.Plan_Confirm()
    Delay(2, 4)#TODO

    # # 结算动画
    # CombatWindow.Combat_Animation()