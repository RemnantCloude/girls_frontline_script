from pyautogui import click
from pyautogui import moveTo, dragRel
from random import randint

from Window import FormationWindow
from Window import CombatWindow
from general import Delay

### 指挥部
def Headquarters():
    click(randint(1245, 1275),randint(1066, 1075))

### 机场
def Airport():
    click(randint(1277, 1321), randint(527, 562))
    
### 路径1
def pot1():
    click(randint(624, 667), randint(534, 575))

### 4-6
def Combat_46():
    # 选择关卡
    CombatWindow.ChooseLevel(6)

    # 向上拖动
    moveTo(randint(627, 1715),randint(200, 450))
    dragRel(randint(-50, 50), randint(800, 900), 0.5)
    Delay(0, 1)
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
    pot1()
    Delay(1, 2)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(100, 102)

    # 结束回合
    CombatWindow.Combat_End()
    Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()