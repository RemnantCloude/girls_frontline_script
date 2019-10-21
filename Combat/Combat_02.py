from pyautogui import click
from random import randint

from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general

### 指挥部
def Headquarters():
    click(randint(930, 1006), randint(500, 582))

### 机场
def Airport():
    click(randint(645, 715), randint(496, 567))

### 路径1
def pot1():
    click(randint(955, 1005), randint(135, 180))

### 路径2
def pot2():
    click(randint(1190, 1245), randint(85, 145))

### 单打手拖尸02，一共五战
def Combat_02(current_times):
    # 选择关卡
    CombatWindow.ChooseLevel(2)

    # 交换打手
    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 点击队伍编成
    CombatWindow.Team_Form()
    # 交换打手TODO
    if current_times % 2 == 0:# 奇数次 15
        # 点击3号位打手
        FormationWindow.ChooseFigure(3)
        Delay(2, 3)
        FormationWindow.Figure(1, 4)
        Delay(1, 2)
    else:# 偶数次 G11
        # 点击3号位打手
        FormationWindow.ChooseFigure(3)
        FormationWindow.FigureKindDisplay('AR')
        FormationWindow.Figure(2, 1)
        Delay(1, 2)
    # 返回
    general.Cancel()

    # 部署梯队
    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 点击确定，部署打手队
    CombatWindow.Deploy_Confirm()
    # 点击机场
    Airport()
    Delay(1, 2)
    # 点击确定，部署狗粮
    CombatWindow.Deploy_Confirm()

    # 开始作战
    CombatWindow.Combat_Start()
    # 点击狗粮2次
    Airport()
    Delay(1, 2)
    Airport()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()
    # 随意点击
    CombatWindow.Choose_Cancel()
    Delay(0, 1)
    # 进入计划模式
    CombatWindow.PlanMode()
    # 点击打手队
    Headquarters()
    Delay(1, 2)
    # 规划路径
    pot1()
    Delay(1, 2)
    pot2()
    Delay(1, 2)
    # 执行计划
    CombatWindow.Plan_Confirm()

    # 等待
    Delay(175, 177)

    # 结束回合
    CombatWindow.Combat_End()
    Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()