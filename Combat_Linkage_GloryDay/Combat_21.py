from pyautogui import click
from random import randint

from Combat_Linkage_GloryDay import CombatSet
from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters_1():
    click(randint(975, 1008), randint(525, 556))

### 路径1
def pot1_1():
    click(randint(1105, 1130), randint(525, 550))

### 路径2
def pot2_1():
    click(randint(975, 1000), randint(425, 450))

### 指挥部
def Headquarters_2():
    click(randint(975, 1008), randint(560, 590))

### 路径2
def pot2_2():
    click(randint(975, 1000), randint(465, 490))

### 荣耀日 薄暮骑士
def Combat_21():
    # 选择关卡
    CombatSet.ChooseLevel(1)

    # 部署主力队
    Headquarters_1()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    CombatWindow.Combat_Start()

    # 补充弹药
    Headquarters_1()
    Delay(1, 2)
    Headquarters_1()
    Delay(1, 2)
    CombatWindow.Supply()
    CombatWindow.PlanMode()
    pot1_1()
    Delay(1, 2)
    pot2_1()
    Delay(1, 2)
    CombatWindow.Plan_Confirm()
    
    Delay(102, 103)

    # 撤退
    Headquarters_2()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    pot2_2()
    Delay(1, 2)
    Headquarters_2()
    Delay(1, 2)
    click(randint(767, 933), randint(552, 605))
    Delay(2, 3)
    Headquarters_2()
    Delay(1, 2)
    CombatWindow.Retreat()
    # 结束回合
    CombatWindow.Combat_Terminate()