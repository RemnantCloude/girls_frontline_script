from pyautogui import click
from random import randint
from pyautogui import moveTo, dragRel

from Combat_Linkage_GloryDay import CombatSet
from Window import FormationWindow
from Window import CombatWindow
from general import Delay
import general
import image

### 指挥部
def Headquarters():
    click(randint(726, 772), randint(612, 657))

### 机场
def Airport():
    click(randint(1074, 1112), randint(635, 674))

### 路径1
def pot1_1():
    click(randint(900, 925), randint(578, 603))

### 路径2
def pot2_1():
    click(randint(1022, 1048), randint(515, 543))

### 路径3
def pot3_1():
    click(randint(1140, 1166), randint(556, 582))

### 路径4
def pot4_1():
    click(randint(615, 658), randint(736, 782))

### 路径5
def pot5_1():
    click(randint(965, 998), randint(694, 725))


### 第一回合
def round1():
    # 主力队补充弹药
    Headquarters()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    CombatWindow.Supply()
    # 前进
    pot1_1()
    Delay(2, 3)
    CombatWindow.Choose_Cancel()
    # 部署守家队并补充弹药
    Headquarters()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    Headquarters()
    Delay(1, 2)
    Headquarters()
    Delay(1, 2)
    CombatWindow.Supply()
    # 结束回合
    CombatWindow.Round_End()
    Delay(19, 20)
    # 检测是否进入下一回合
    matching = image.match('e:/code/girls_frontline_script/images/round_end.png', image.capture_screen())
    # 未进入下一回合
    if (matching[0] < 100000000):
        Delay(15, 16)
        CombatWindow.Combat_EndClear()
        Delay(6, 7)

# 第二回合
def round2():
    # 主力队上前
    pot1_1()
    Delay(1, 2)
    pot2_1()
    Delay(2, 3)
    # 检测是否进入战斗
    matching = image.match('e:/code/girls_frontline_script/images/round_end.png', image.capture_screen())
    # 进入战斗
    if (matching[0] < 100000000):
        Delay(13, 14)
        CombatWindow.Combat_EndClear()
    # 部署狗粮
    Headquarters()
    Delay(1, 2)
    pot1_1()
    Delay(2, 3)
    CombatWindow.Choose_Cancel()
    Headquarters()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    # 交换
    Headquarters()
    Delay(1, 2)
    pot1_1()
    Delay(1, 2)
    click(randint(685, 861), randint(560, 623))
    Delay(2, 3)
    CombatWindow.Choose_Cancel()
    CombatWindow.PlanMode()
    pot2_1()
    Delay(1, 2)
    Airport()
    Delay(1, 2)
    CombatWindow.Choose_Cancel()
    pot1_1()
    Delay(1, 2)
    pot3_1()
    Delay(1, 2)
    CombatWindow.Plan_Confirm()
    Delay(67, 68)
    

# 第三回合
def round3():
    CombatWindow.Round_End()
    Delay(21, 22)
    CombatWindow.Combat_EndClear()
    Delay(3, 4)
    # 检测是否进入战斗
    matching = image.match('e:/code/girls_frontline_script/images/round_end.png', image.capture_screen())
    # 进入战斗
    if (matching[0] < 100000000):
        Delay(11, 12)
        CombatWindow.Combat_EndClear()
    Delay(6, 7)

# 第四回合
def round4():
    # 往上拖动界面
    moveTo(randint(1400, 1600), randint(250, 400))
    dragRel(randint(-50, 50), randint(400, 500), 0.5)
    Delay(0, 1)
    Airport()
    Delay(1, 2)
    Airport()
    Delay(1, 2)
    CombatWindow.Supply()
    CombatWindow.PlanMode()
    pot4_1()
    Delay(1, 2)
    CombatWindow.Plan_Confirm()
    Delay(54, 56)
    while(1):
        # 检测是否在战斗中
        matching = image.match('e:/code/girls_frontline_script/images/round_end.png', image.capture_screen())
        # 战斗中
        if (matching[0] < 100000000):
            Delay(1, 2)
        else:
            break
    CombatWindow.Round_End()
    Delay(12, 14)
    CombatWindow.Combat_Animation()


### 随我同行 等着你！
def Combat_13():
    # 选择关卡
    CombatSet.ChooseLevel(3)

    # 往上拖动界面
    moveTo(randint(1400, 1600), randint(250, 400))
    dragRel(randint(-50, 50), randint(400, 500), 0.5)
    Delay(0, 1)
    # 点击指挥部
    Headquarters()
    Delay(1, 2)
    # 部署主力队
    CombatWindow.Deploy_Confirm()
    # 开始作战
    CombatWindow.Combat_Start()

    round1()
    round2()
    round3()
    round4()
