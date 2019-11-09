from pyautogui import click
from random import randint

from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general
import image

# 第一回合
### 指挥部
def Headquarters_1():
    click(randint(1200, 1240), randint(520, 560))

### 指挥部左下机场
def pot1_1():
    click(randint(1070, 1108), randint(674, 711))

# 第二回合
### 指挥部
def Headquarters_2():
    click(randint(1200, 1240), randint(365, 395))

### 指挥部左下机场
def pot1_2():
    click(randint(1070, 1108), randint(517, 558))

### 路径2
def pot2_2():
    click(randint(1100, 1130), randint(683, 713))

### 岔路口
def pot3_2():
    click(randint(960, 990), randint(820, 850))

### 岔路口左上
def pot4_2():
    click(randint(770, 800), randint(756, 786))

### 岔路口左下
def pot5_2():
    click(randint(850, 880), randint(875, 905))

def pot6_2():
    click(randint(780, 810), randint(965, 995))

### 34n夜战
def Combat_34n():
    # 选择关卡
    CombatWindow.ChooseLevel(4)

    # 部署梯队
    # 点击指挥部
    Headquarters_1()
    Delay(1, 2)
    # 点击确定，部署主力队
    CombatWindow.Deploy_Confirm()
    # 开始作战
    CombatWindow.Combat_Start()

    round1()
    round2()

# 第一回合
def round1():
    # 点击主力队2次
    Headquarters_1()
    Delay(1, 2)
    Headquarters_1()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()
    # 移动到左下机场
    pot1_1()
    # 战斗
    Delay(16, 18)
    CombatWindow.Combat_EndClear()

    # 部署守家队伍
    # 取消选择
    CombatWindow.Choose_Cancel()
    # 点击指挥部
    Headquarters_2()
    Delay(1, 2)
    # 点击确定，部署梯队
    CombatWindow.Deploy_Confirm()
    # 点击守家队2次
    Headquarters_2()
    Delay(1, 2)
    Headquarters_2()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()
    # 结束回合
    CombatWindow.Round_End()
    Delay(4, 5)
    # 检测是否进入下一回合
    matching = image.match('e:/code/girls_frontline_script/images/round_end.png', image.capture_screen())
    # 未进入下一回合
    if (matching[0] < 100000000):
        Delay(22, 23)
        CombatWindow.Combat_EndClear()
        Delay(6, 7)

    # 检测是否进入下一回合
    matching = image.match('e:/code/girls_frontline_script/images/round_end.png', image.capture_screen())
    # 未进入下一回合
    if (matching[0] < 100000000):
        Delay(22, 23)
        CombatWindow.Combat_EndClear()
        Delay(6, 7)

# 第二回合
def round2():
    # 守家梯队撤退
    Headquarters_2()
    Delay(1, 2)
    Headquarters_2()
    Delay(1, 2)
    CombatWindow.Retreat()
    # 选择主力队
    pot1_2()
    Delay(1, 2)
    # 检测小飞机
    matching = image.match('e:/code/girls_frontline_script/images/34n_fly.png', image.capture_screen())
    if (matching[0] > 20000000):
        CombatWindow.Fairy_release()
    pot2_2()
    Delay(18, 19)
    CombatWindow.Combat_EndClear()
    pot2_2()
    Delay(1, 2)
    # 检测小飞机
    matching = image.match('e:/code/girls_frontline_script/images/34n_fly.png', image.capture_screen())
    if (matching[0] > 20000000):
        CombatWindow.Fairy_release()
    pot3_2()
    Delay(18, 19)
    CombatWindow.Combat_EndClear()
    pot3_2()
    Delay(1, 2)
    # 检测boss
    matching = image.match('e:/code/girls_frontline_script/images/34n_boss.png', image.capture_screen())
    # boss出现
    if (matching[0] > 20000000):
        pot4_2()
    else:
        pot5_2()
        Delay(1, 2)
        pot6_2()
    Delay(19, 20)
    CombatWindow.Combat_EndClear()
    # 撤退
    CombatWindow.Combat_Terminate()