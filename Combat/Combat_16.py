from pyautogui import click
from random import randint
from time import sleep

import FormationWindow
import CombatWindow
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
    CombatWindow.CombatWindow_TO45()
    CombatWindow.CombatWindow_6()
    general.Delay(2, 4)
    # 点击普通作战
    CombatWindow.NormalCombat()
    general.Delay(2, 4)

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
    # 执行计划
    CombatWindow.Plan_Confirm()
    general.Delay(2, 4)

    # 等待
    sleep(random.uniform(70, 75))

    # 结束回合
    CombatWindow.Combat_End()
    sleep(random.uniform(25, 30))
    
    # 结算动画
    click(randint(1200,1500),randint(600,750))
    general.Delay(2, 4)
    click(randint(1200,1500),randint(600,750))
    general.Delay(2, 4)
    
    # 点击梯队2次
    Airport()
    general.Delay(2, 4)
    Airport()
    general.Delay(2, 4)
    # 补充弹药
    CombatWindow.Supply()
    general.Delay(2, 4)

    # 进入计划模式
    CombatWindow.PlanMode()
    general.Delay(2, 4)
    # 规划路径
    pot2()
    general.Delay(2, 4)
    pot3()
    general.Delay(2, 4)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    sleep(random.uniform(120, 125))

    click(randint(1200,1500),randint(600,750))
    general.Delay(2, 4)

    # 结束回合
    CombatWindow.Combat_End()
    general.Delay(2, 4)
    CombatWindow.Combat_End()
    sleep(random.uniform(12,14))

    # 结算动画
    CombatWindow.Combat_Animation()
