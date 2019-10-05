from pyautogui import click
from pyautogui import moveTo, dragRel
from pyautogui import screenshot
from random import randint
import PIL.ImageGrab
import operator

from general import Delay

# 战斗
## 作战任务
### 普通作战
def NormalCombat():
    click(randint(1000,1235), randint(814,925))

### 翻页到5.6小关
def TO56():
    moveTo(randint(640, 1880), randint(878, 1052))
    dragRel(randint(-50, 50), randint(-700, -500), 0.5)
    Delay(0, 1)

### 选择关卡
def ChooseLevel(level):
    if level is 1:
        pass
    elif level is 2:
        click(randint(640, 1800), randint(527, 666))
    elif level is 3:
        pass
    elif level is 4:
        click(randint(640, 1800), randint(881, 1015))
    elif level is 5:
        pass
    elif level is 6:
        TO56()
        click(randint(640, 1800), randint(830, 950))
    Delay(1, 2)
    NormalCombat()
    Delay(3, 4)

## 作战中
### 开始作战
def Combat_Start():
    click(randint(1655, 1870), randint(935, 1010))
    Delay(2, 3)

### 结束作战
def Combat_End():
    click(randint(1655, 1870), randint(935, 1010))
    
### 终止作战
def Combat_Terminate():
    click(randint(402, 548), randint(10, 120))
    Delay(1, 2)
    click(randint(1073, 1300), randint(701, 776))
    Delay(3, 4)

### 重新作战
def Combat_Retry():
    click(randint(402, 548), randint(10, 120))
    Delay(1, 2)
    click(randint(621, 849), randint(701, 776))
    Delay(3, 4)

### 队伍编成
def Team_Form():
    click(randint(225,500),randint(900,960))

### 确定部署
def Deploy_Confirm():
    click(randint(1655, 1870), randint(935, 1010))
    Delay(2, 3)

### 补充弹药
def Supply():
    click(randint(1620, 1920), randint(790, 885))
    Delay(1, 2)

### 撤退
def Retreat():
    click(randint(1376, 1615), randint(932, 1009))
    Delay(1, 2)
    click(randint(1000, 1237), randint(701, 786))
    Delay(2, 3)

### 计划模式
def PlanMode():
    click(randint(0, 250), randint(855, 920))
    Delay(0, 1)

### 执行计划
def Plan_Confirm():
    click(randint(1665, 1890), randint(930, 1035))
    Delay(0, 1)

### 取消选择
def Choose_Cancel():
    click(randint(1300, 1700), randint(750, 900))
    Delay(0, 1)

### 战斗妖精AUTO
def Fairy_AUTO():
    click(randint(1760, 1885), randint(307, 350))
    Delay(1, 2)

### 战斗结算
def Combat_EndClear():
    click(randint(1300, 1700), randint(750, 900))
    Delay(2, 3)
    click(randint(1300, 1700), randint(750, 900))
    Delay(1, 2)
    click(randint(1300, 1700), randint(750, 900))
    Delay(1, 2)
    click(randint(1300, 1700), randint(750, 900))
    Delay(2, 3)
    click(randint(1300, 1700), randint(750, 900))
    Delay(0, 1)
        
    
### 结算动画
def Combat_Animation():
    click(randint(1300, 1700), randint(750, 900))
    Delay(4, 6)
    click(randint(1300, 1700), randint(750, 900))
    Delay(2, 4)
    click(randint(1300, 1700), randint(750, 900))
    Delay(4, 6)
