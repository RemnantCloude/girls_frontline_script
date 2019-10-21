from pyautogui import click
from random import randint

from Combat_2019_Hallowmas import CombatSet
from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(602, 647), randint(455, 500))

### 路径1
def pot1():
    click(randint(747, 771), randint(464, 493))

### 路径2
def pot2():
    click(randint(866, 897), randint(464, 492))

### 路径3
def pot3():
    click(randint(609, 637), randint(601, 628))

### 赏味期限
def Combat_3():
    # 选择关卡
    CombatSet.ChooseLevel(3)

    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 点击确定，部署主力
    CombatWindow.Deploy_Confirm()

    # 开始作战
    CombatWindow.Combat_Start()
    # 点击主力2次
    Headquarters()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()

    # 移动主力
    pot1()
    Delay(1, 2)
    CombatWindow.Choose_Cancel()
    Headquarters()
    Delay(1, 2)
    # 点击确定，部署狗粮
    CombatWindow.Deploy_Confirm()
    # 进入计划模式
    CombatWindow.PlanMode()
    pot1()
    Delay(1, 2)
    # 规划路径
    pot2()
    Delay(1, 2)
    pot3()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    click(randint(378, 594), randint(447, 503))
    Delay(1, 2)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    # Delay(103, 105)

    # 等待TODO
    Delay(72, 73)
    # 第三战撤退k5
    click(randint(249, 328), randint(575, 615))
    Delay(1, 2)
    CombatWindow.SingleFigure_Retreat()
    # 等待
    Delay(30, 32)

    # 撤退
    Headquarters()
    Delay(0, 1)
    Headquarters()
    Delay(1, 2)
    CombatWindow.Retreat()
    CombatWindow.Combat_Terminate()