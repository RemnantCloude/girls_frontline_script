from pyautogui import click
from random import randint
from time import sleep

import FormationWindow
import CombatWindow
import general

### 指挥部
def Headquarters():
    click(randint(667, 724), randint(514, 562))
    
### 路径1
def pot1():
    click(randint(1003, 1050), randint(362, 409))

### 2-4e单打手
def Combat_24e():
    # 选择关卡
    CombatWindow.CombatWindow_4()
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
    sleep(random.uniform(95, 100))

    # 结束回合
    CombatWindow.Combat_End()
    general.Delay(2, 4)
    CombatWindow.Combat_End()
    sleep(random.uniform(12,14))

    # 结算动画
    CombatWindow.Combat_Animation()
    
