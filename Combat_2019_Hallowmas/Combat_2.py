from pyautogui import click
from random import randint

from Combat_2019_Hallowmas import CombatSet
from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(857, 900), randint(350, 394))

### 路径1
def pot1():
    click(randint(1050, 1087), randint(785, 830))

### 1AR+1HG/2HG
def Combat_2():
    # 选择关卡
    CombatSet.ChooseLevel(2)

    # 部署梯队
    # 点击指挥部
    Headquarters()
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

    # 进入计划模式
    CombatWindow.PlanMode()
    # 规划路径
    pot1()
    Delay(1, 2)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(83, 85)

    # 回合结束
    CombatWindow.Round_End()
    Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()
    ## 如果有碎片就取消注释
    click(randint(1800, 1900), randint(750, 900))
    Delay(1, 2)
    click(randint(1800, 1900), randint(750, 900))
    Delay(2, 3)
