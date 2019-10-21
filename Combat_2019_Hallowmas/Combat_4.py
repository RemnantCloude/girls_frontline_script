from pyautogui import click
from random import randint

from Combat_2019_Hallowmas import CombatSet
from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(618, 657), randint(387, 424))

### 机场
def Airport():
    click(randint(623, 661), randint(749, 774))

### 路径1
def pot1():
    click(randint(946, 965), randint(589, 615))

### 路径2
def pot2():
    click(randint(821, 843), randint(532, 555))

### 防腐剂
def Combat_4():
    # 选择关卡
    CombatSet.ChooseLevel(4)

    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 部署梯队
    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 点击确定，部署主力
    CombatWindow.Deploy_Confirm()
    # 点击机场
    Airport()
    Delay(1, 2)
    # 点击确定，部署狗粮
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

    # 进入计划模式
    CombatWindow.PlanMode()
    # 规划路径
    pot1()
    Delay(1, 2)
    pot2()
    Delay(1, 2)
    pot1()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(80, 82)

    # 撤退
    Headquarters()
    Delay(0, 1)
    Headquarters()
    Delay(1, 2)
    CombatWindow.Retreat()
    CombatWindow.Combat_Terminate()