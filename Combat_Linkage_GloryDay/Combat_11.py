from pyautogui import click
from random import randint

from Combat_Linkage_GloryDay import CombatSet
from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(966, 1017), randint(463, 514))

### 路径1
def pot1():
    click(randint(861, 895), randint(760, 793))

### 路径2
def pot2():
    click(randint(736, 767), randint(734, 769))

### 路径3
def pot3():
    click(randint(1022, 1070), randint(778, 833))

### 荣耀日 跟踪狂
def Combat_11():
    # 选择关卡
    CombatSet.ChooseLevel(1)

    # 部署主力队
    Headquarters()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    CombatWindow.Combat_Start()

    # 补充弹药
    Headquarters()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    CombatWindow.Supply()
    CombatWindow.PlanMode()
    pot1()
    Delay(1, 2)
    pot2()
    Delay(1, 2)
    pot3()
    Delay(1, 2)
    CombatWindow.Plan_Confirm()
    
    Delay(135, 136)
    # 结束回合
    CombatWindow.Combat_Animation()