from pyautogui import click
from random import randint

import FormationWindow
import CombatWindow
import general

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
    general.Delay(2, 4)
    # 点击确定，部署第一梯队
    CombatWindow.Deploy_Confirm()
    general.Delay(2, 4)

    # 开始作战
    CombatWindow.Deploy_Confirm()
    general.Delay(2, 4)
    # 点击梯队2次
    Headquarters()
    general.Delay(2, 4)
    Headquarters()
    general.Delay(2, 4)
    # 补充弹药
    CombatWindow.Supply()
    general.Delay(2, 4)
    # 进入计划模式
    CombatWindow.PlanMode()
    general.Delay(2, 4)
    # 规划路径
    pot1()
    general.Delay(2, 4)
    pot2()
    general.Delay(2, 4)
    # 执行计划
    CombatWindow.Plan_Confirm()
    general.Delay(2, 4)

    # 等待
    general.Delay(90, 95)

    # 结束回合
    CombatWindow.Combat_End()
    general.Delay(2, 4)
    CombatWindow.Combat_End()
    general.Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()
    
