from pyautogui import click
from random import randint

from Window import FormationWindow
from Window import CombatWindow
from general import Delay

### 指挥部
def Headquarters():
    click(randint(669, 720), randint(514, 562))
    
### 路径1
def pot1():
    click(randint(794, 840), randint(507, 554))

### 路径2
def pot2():
    click(randint(1007, 1053), randint(362, 409))

### 2-6单打手
def Combat_26():
    # 选择关卡
    CombatWindow.ChooseLevel(6)

    # 点击指挥部
    Headquarters()
    Delay(2, 4)
    # 点击确定，部署第一梯队
    CombatWindow.Deploy_Confirm()

    # 开始作战
    CombatWindow.Combat_Start()
    Delay(2, 4)
    # 点击梯队2次
    Headquarters()
    Delay(2, 4)
    Headquarters()
    Delay(2, 4)
    # 补充弹药
    CombatWindow.Supply()
    # 进入计划模式
    CombatWindow.PlanMode()
    # 规划路径
    pot1()
    Delay(2, 4)
    pot2()
    Delay(2, 4)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(90, 95)

    # 结束回合
    CombatWindow.Combat_End()
    Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()
    
