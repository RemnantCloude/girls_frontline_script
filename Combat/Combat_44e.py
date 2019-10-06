from pyautogui import click
from pyautogui import moveTo, dragRel
from random import randint, uniform
from time import sleep

import FormationWindow
import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(1245, 1275),randint(1066, 1075))

### 机场
def Airport():
    click(randint(1277, 1321), randint(527, 562))
    
### 路径1
def pot1():
    click(randint(624, 667), randint(534, 575))

### 4-4E拖尸
def Combat_44e(current_times):
    # 选择关卡
    CombatWindow.ChooseLevel(4)
    
    # 交换打手
    # 点击指挥部
    click(randint(1244, 1281),randint(520, 566))
    Delay(1, 2)
    # 点击队伍编成
    CombatWindow.Team_Form()
    # 交换打手
    if current_times % 2 == 0:# 偶数次 15
        # 点击3号位打手
        FormationWindow.ChooseFigure(3)
        Delay(2, 3)
        # 选择替补1
        FormationWindow.Figure(1, 4)
        Delay(1, 2)
    else:# 奇数次 M4
        # 点击3号位打手
        FormationWindow.ChooseFigure(3)
        Delay(2, 3)
        # 选择替补1
        FormationWindow.Figure(1, 3)
        Delay(1, 2)
    # 返回
    general.Cancel()

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
    Headquarters()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()
    # 随意点击
    click(randint(1300, 1700), randint(750, 900))
    Delay(0, 1)
    # 进入计划模式
    CombatWindow.PlanMode()
    # 规划路径
    Airport()
    Delay(1, 2)
    pot1()
    Delay(1, 2)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(97, 100)

    # 结束回合
    CombatWindow.Combat_End()
    Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()