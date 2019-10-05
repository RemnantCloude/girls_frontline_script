from pyautogui import click
from random import randint
from random import uniform
from time import sleep

import FormationWindow
import CombatWindow
import general

### 指挥部
def Headquarters():
    click(randint(930,1006),randint(500,582))

### 机场
def Airport():
    click(randint(645,715),randint(496,567))

### 路径1
def pot1():
    click(randint(955,1005),randint(135,180))

### 路径2
def pot2():
    click(randint(1190,1245),randint(85,145))

### 单打手拖尸02，一共五战
def Combat_02(current_times, repeat_times):
    while current_times < repeat_times:
        # 选择关卡
        CombatWindow.ChooseLevel(2)

        # 交换打手
        # 点击指挥部
        Headquarters()
        general.Delay(2, 3)
        # 点击队伍编成
        CombatWindow.Team_Form()
        general.Delay(2, 4)
        # 交换打手
        if current_times % 2 == 0:# 奇数次 15
            # 点击3号位打手
            FormationWindow.ChooseFigure(3)
            general.Delay(2, 4)
            # 选择替补1
            FormationWindow.Figure(1, 4)
            general.Delay(2, 4)
        else:# 偶数次 SOP2
            # 点击3号位打手
            FormationWindow.ChooseFigure(3)
            general.Delay(2, 4)
            # 选择替补1
            FormationWindow.Figure(1, 2)
            general.Delay(2, 4)
        # 返回
        general.Cancel()
        general.Delay(2, 4)

        # 部署梯队
        # 点击指挥部
        Headquarters()
        general.Delay(2, 4)
        # 点击确定，部署打手队
        CombatWindow.Deploy_Confirm()
        general.Delay(2, 4)
        # 点击机场
        Airport()
        general.Delay(2, 4)
        # 点击确定，部署狗粮
        CombatWindow.Deploy_Confirm()
        general.Delay(2, 4)

        # 开始作战
        CombatWindow.Deploy_Confirm()
        general.Delay(2, 4)
        # 点击狗粮2次
        Airport()
        general.Delay(2, 4)
        Airport()
        general.Delay(2, 4)
        # 补充弹药
        CombatWindow.Supply()
        general.Delay(2, 4)
        # 随意点击
        click(randint(1200,1500),randint(600,750))
        general.Delay(2, 4)
        # 进入计划模式
        CombatWindow.PlanMode()
        general.Delay(2, 4)
        # 点击打手队
        Headquarters()
        general.Delay(2, 4)
        # 规划路径
        pot1()
        general.Delay(2, 4)
        pot2()
        general.Delay(2, 4)
        # 执行计划
        CombatWindow.Plan_Confirm()

        # 等待
        sleep(uniform(175,180))

        click(randint(1200,1500),randint(600,750))
        general.Delay(2, 4)

        # 结束回合
        CombatWindow.Combat_End()
        general.Delay(2, 4)
        CombatWindow.Combat_End()
        sleep(uniform(12,14))

        # 结算动画
        CombatWindow.Combat_Animation()
        # 点击几次
        print(current_times)
        current_times = current_times + 1