import pyautogui
import random
import time

import FormationWindow
import CombatWindow
import general

### 指挥部
def Headquarters():
    pyautogui.click(random.randint(930,1006),random.randint(500,582))

### 机场
def Airport():
    pyautogui.click(random.randint(645,715),random.randint(496,567))

### 路径1
def pot1():
    pyautogui.click(random.randint(955,1005),random.randint(135,180))

### 路径2
def pot2():
    pyautogui.click(random.randint(1190,1245),random.randint(85,145))

### 02
# 
def Combat_02(current_times, repeat_times):
    while current_times < repeat_times:
        # 选择关卡
        CombatWindow.CombatWindow_02()
        general.Delay_24()
        # 点击普通作战
        CombatWindow.NormalCombat()
        general.Delay_24()

        # 交换打手
        # 点击指挥部
        Headquarters()
        general.Delay_24()
        # 点击队伍编成
        CombatWindow.Team_Form()
        general.Delay_24()
        # 交换打手
        if current_times % 2 == 0:# 奇数次 15
            # 点击3号位打手
            FormationWindow.FormationWindow_Figure3()
            general.Delay_24()
            # 选择替补1
            FormationWindow.FormationWindow_14()
            general.Delay_24()
        else:# 偶数次 SOP2
            # 点击3号位打手
            FormationWindow.FormationWindow_Figure3()
            general.Delay_24()
            # 选择替补1
            FormationWindow.FormationWindow_12()
            general.Delay_24()
        # 返回
        general.Cancel()
        general.Delay_24()

        # 部署梯队
        # 点击指挥部
        Headquarters()
        general.Delay_24()
        # 点击确定，部署打手队
        CombatWindow.Deploy_Confirm()
        general.Delay_24()
        # 点击机场
        Airport()
        general.Delay_24()
        # 点击确定，部署狗粮
        CombatWindow.Deploy_Confirm()
        general.Delay_24()

        # 开始作战
        CombatWindow.Deploy_Confirm()
        general.Delay_24()
        # 点击狗粮2次
        Airport()
        general.Delay_24()
        Airport()
        general.Delay_24()
        # 补充弹药
        CombatWindow.Supply()
        general.Delay_24()
        # 随意点击
        pyautogui.click(random.randint(1200,1500),random.randint(600,750))
        general.Delay_24()
        # 进入计划模式
        CombatWindow.PlanMode()
        general.Delay_24()
        # 点击打手队
        Headquarters()
        general.Delay_24()
        # 规划路径
        pot1()
        general.Delay_24()
        pot2()
        general.Delay_24()
        # 执行计划
        CombatWindow.Plan_Confirm()
        general.Delay_24()

        # 等待
        time.sleep(random.uniform(175,180))

        pyautogui.click(random.randint(1200,1500),random.randint(600,750))
        general.Delay_24()

        # 结束回合
        CombatWindow.Combat_End()
        general.Delay_24()
        CombatWindow.Combat_End()
        time.sleep(random.uniform(12,14))

        # 等待结算动画
        pyautogui.click(random.randint(1200,1500),random.randint(600,750))
        general.Delay_46()
        pyautogui.click(random.randint(1200,1500),random.randint(600,750))
        general.Delay_24()
        pyautogui.click(random.randint(1200,1500),random.randint(600,750))
        general.Delay_46()
        # 点击几次
        print(current_times)
        current_times = current_times + 1