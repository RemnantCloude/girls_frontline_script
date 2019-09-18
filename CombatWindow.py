import pyautogui
import random

# 战斗
## 作战任务
### 普通作战
def NormalCombat():
    pyautogui.click(random.randint(1000,1235),random.randint(814,925))

### 0-2
def CombatWindow_02():
    pyautogui.click(random.randint(625,1900),random.randint(625,666))

## 作战中
### 开始作战
def Combat_Start():
    pyautogui.click(random.randint(1655,1870),random.randint(935,1010))

### 结束作战
def Combat_End():
    pyautogui.click(random.randint(1655,1870),random.randint(935,1010))

### 队伍编成
def Team_Form():
    pyautogui.click(random.randint(225,500),random.randint(900,960))

### 确定部署
def Deploy_Confirm():
    pyautogui.click(random.randint(1655,1870),random.randint(935,1010))

### 补充弹药
def Supply():
    pyautogui.click(random.randint(1620,1920),random.randint(790,885))

### 计划模式
def PlanMode():
    pyautogui.click(random.randint(0,250),random.randint(855,920))

### 执行计划
def Plan_Confirm():
    pyautogui.click(random.randint(1665,1890),random.randint(930,1035))
