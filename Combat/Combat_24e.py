from pyautogui import click
from random import randint

from Window import FormationWindow
from Window import CombatWindow
from general import Delay

### 指挥部
def Headquarters():
    click(randint(667, 724), randint(514, 562))
    
### 路径1
def pot1():
    click(randint(1003, 1050), randint(362, 409))

### 2-4e单打手
def Combat_24e():
    # 选择关卡
    CombatWindow.ChooseLevel(4)
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
    Delay(95, 97)

    # 结束回合
    CombatWindow.Round_End()
    Delay(12, 14)

    # 结算动画
    CombatWindow.Combat_Animation()
    
