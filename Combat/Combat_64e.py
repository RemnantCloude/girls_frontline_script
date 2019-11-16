from pyautogui import click
from random import randint
from time import sleep

from Window import FormationWindow
from Window import CombatWindow
from general import Delay

# 第一回合
### 指挥部
def Headquarters_1():
    click(randint(614, 667), randint(517, 563)) 
### 路径1
def pot1_1():
    click(randint(647, 671), randint(456, 480))
### 路径2
def pot2_1():
    click(randint(698, 726), randint(372, 396))

# 第二回合战斗之后
### 指挥部
def Headquarters_2():
    click(randint(625, 657), randint(691, 723))
### 路径1
def pot1_2():
    click(randint(647, 671), randint(611, 635))
### 路径2
def pot2_2():
    click(randint(698, 726), randint(524, 550))
### 路径3
def pot3_2():
    click(randint(776, 806), randint(459, 486))
### 路径4
def pot4_2():
    click(randint(781, 810), randint(382, 413))
### 路径5
def pot5_2():
    click(randint(700, 734), randint(185, 219))
### 路径6
def pot6_2():
    click(randint(687, 717), randint(279, 305))

# 第六回合
### 路径5
def pot5_6():
    click(randint(700, 734), randint(436, 464))
### 路径6
def pot6_6():
    click(randint(687, 717), randint(526, 552))
### 左上机场（boss）
def pot7_6():
    click(randint(570, 611), randint(323, 357))
### 路径8
def pot8_6():
    click(randint(889, 922), randint(371, 397))
### 路径9
def pot9_6():
    click(randint(746, 773), randint(360, 382))

# 第七回合
### 路径8
def pot8_7():
    click(randint(889, 922), randint(528, 565))
### 路径10
def pot10_7():
    click(randint(1307, 1346), randint(474, 511))

# 第一回合
def round1():
    # 点击梯队2次
    Headquarters_1()
    Delay(1, 2)
    Headquarters_1()
    Delay(1, 2)
    # 补充弹药
    CombatWindow.Supply()
    # 行动
    pot1_1()
    Delay(2, 3)
    CombatWindow.Choose_Cancel()
    # 部署狗粮队1
    Headquarters_1()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    # 第一回合结束
    CombatWindow.Round_End()

    Delay(21, 23)

# 第二回合
def round2():
    ## 主力队向上1格
    pot1_1()
    Delay(0, 1)
    pot2_1()
    Delay(18, 19)
    CombatWindow.Combat_EndClear()
    ## 狗粮队1向上1格
    Headquarters_2()
    Delay(0, 1)
    pot1_2()
    Delay(2, 3)
    CombatWindow.Choose_Cancel()
    ## 部署狗粮队2
    Headquarters_2()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    ## 第二回合结束
    CombatWindow.Round_End()

    # 等待
    Delay(21, 23)
    CombatWindow.Combat_EndClear()
    Delay(6, 7)

# 第三回合
def round3():
    ## 主力队向上1格
    pot2_2()
    Delay(0, 1)
    pot3_2()
    Delay(18, 19)
    CombatWindow.Combat_EndClear()
    ## 狗粮队1向上1格
    pot1_2()
    Delay(0, 1)
    pot2_2()
    Delay(1, 2)
    ## 狗粮队2向上1格
    Headquarters_2()
    Delay(0, 1)
    pot1_2()
    Delay(2, 3)
    CombatWindow.Choose_Cancel()
    ## 部署狗粮队3
    Headquarters_2()
    Delay(1, 2)
    CombatWindow.Deploy_Confirm()
    ## 第三回合结束
    CombatWindow.Round_End()

    # 等待
    Delay(21, 23)
    CombatWindow.Combat_EndClear()
    Delay(6, 7)

# 第四回合
def round4():
    ## 补充弹药
    pot3_2()
    Delay(0, 1)
    pot2_2()
    Delay(1, 2)
    click(randint(453, 664), randint(509, 573))
    Delay(1, 2)
    pot1_2()
    Delay(1, 2)
    click(randint(406, 611), randint(591, 658))
    Delay(1, 2)
    Headquarters_2()
    Delay(1, 2)
    click(randint(386, 594), randint(670, 733))
    Delay(1, 2)
    Headquarters_2()
    Delay(2, 3)
    CombatWindow.Supply()
    # 返回
    pot1_2()
    Delay(1, 2)
    click(randint(406, 611), randint(591, 658))
    Delay(1, 2)
    pot2_2()
    Delay(1, 2)
    click(randint(453, 664), randint(509, 573))
    Delay(1, 2)
    pot3_2()
    Delay(1, 2)
    click(randint(533, 735), randint(445, 508))
    Delay(1, 2)
    ## 主力队向上1格
    pot4_2()
    Delay(18, 19)
    CombatWindow.Combat_EndClear()
    Delay(6, 7)
    ## 狗粮队1向上1格
    pot2_2()
    Delay(0, 1)
    pot3_2()
    Delay(1, 2)
    ## 第四回合结束
    CombatWindow.Round_End()

    # 等待
    Delay(21, 23)
    CombatWindow.Combat_EndClear()
    Delay(6, 7)

# 第五回合
def round5():
    ## 计划模式
    CombatWindow.PlanMode()
    pot4_2()
    Delay(0, 1)
    pot5_2()
    Delay(0, 1)
    CombatWindow.Choose_Cancel()
    pot3_2()
    Delay(0, 1)
    pot6_2()
    Delay(0, 1)
    CombatWindow.Plan_Confirm()
    Delay(50, 52)
    # 打开妖精
    CombatWindow.Fairy_AUTO()
    ## 第五回合结束
    CombatWindow.Round_End()

    # 等待
    Delay(21, 23)
    CombatWindow.Combat_EndClear()
    Delay(6, 7)

# 第六回合
def round6():
    ## 补给
    pot5_6()
    Delay(1, 2)
    pot5_6()
    Delay(1, 2)
    CombatWindow.Supply()
    ## 计划模式
    CombatWindow.PlanMode()
    pot7_6()
    Delay(0, 1)
    pot8_6()
    Delay(0, 1)
    CombatWindow.Choose_Cancel()
    pot6_6()
    Delay(0, 1)
    pot9_6()
    Delay(0, 1)
    CombatWindow.Plan_Confirm()
    Delay(65, 67)
    ## 第六回合结束
    CombatWindow.Round_End()

    # 等待
    Delay(21, 23)
    CombatWindow.Combat_EndClear()
    Delay(6, 7)

# 第七回合
def round7():
    ## 计划模式
    CombatWindow.PlanMode()
    pot8_7()
    Delay(0, 1)
    pot10_7()
    Delay(0, 1)
    pot8_7()
    Delay(0, 1)
    CombatWindow.Plan_Confirm()
    Delay(63, 65)
    # 关闭妖精
    CombatWindow.Fairy_AUTO()
    ## 撤退
    pot8_7()
    Delay(1, 2)
    pot8_7()
    Delay(2, 3)
    CombatWindow.Retreat()
    CombatWindow.Combat_Terminate()

### 6-4E
def Combat_64e():
    # 选择关卡
    CombatWindow.ChooseLevel(4)

    # 点击指挥部
    Headquarters_1()
    Delay(1, 2)
    # 部署主力队
    CombatWindow.Deploy_Confirm()

    # 开始作战
    CombatWindow.Combat_Start()

    round1()
    round2()
    round3()
    round4()
    round5()
    round6()
    round7()
