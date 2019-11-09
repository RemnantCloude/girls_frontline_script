from pyautogui import click
from random import randint

from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(656, 719),randint(513, 569))

### 路径1
def pot1():
    click(randint(1050, 1098), randint(643, 698))
    
### 机场
def Airport():
    click(randint(1050, 1098), randint(512, 566))

### 路径2
def pot2():
    click(randint(1019, 1069), randint(261, 310))

### 敌方指挥部
def pot3():
    click(randint(1045, 1106), randint(673, 727))
    
### 1-6
def Combat_16():
    # 选择关卡
    CombatWindow.ChooseLevel(6)
    # 点击普通作战
    CombatWindow.NormalCombat()

    # 点击指挥部
    Headquarters()
    Delay(2, 4)
    # 点击确定，部署第一梯队
    CombatWindow.Deploy_Confirm()

    # 开始作战
    CombatWindow.Combat_Start()
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
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(70, 75)

    # 结束回合
    CombatWindow.Round_End()
    Delay(25,27)
    
    # 结算动画
    click(randint(1200,1500),randint(600,750))
    Delay(2, 4)
    click(randint(1200,1500),randint(600,750))
    Delay(2, 4)
    
    # 点击梯队2次
    Airport()
    Delay(2, 4)
    Airport()
    Delay(2, 4)
    # 补充弹药
    CombatWindow.Supply()

    # 进入计划模式
    CombatWindow.PlanMode()
    # 规划路径
    pot2()
    Delay(2, 4)
    pot3()
    Delay(2, 4)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(120, 122)

    click(randint(1200,1500),randint(600,750))
    Delay(2, 4)

    # 结束回合
    CombatWindow.Round_End()
    Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()
