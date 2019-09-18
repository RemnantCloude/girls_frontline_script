import pyautogui
import random

# 编成
## 梯队1
def FormationWindow_Echelon1():
    pyautogui.click(random.randint(0,170),random.randint(165,270))

## 梯队2
def FormationWindow_Echelon2():
    pyautogui.click(random.randint(0,170),random.randint(300,400))

## 人形1
def FormationWindow_Figure1():
    pyautogui.click(random.randint(225,465),random.randint(175,735))

## 人形2
def FormationWindow_Figure2():
    pyautogui.click(random.randint(500,730),random.randint(175,735))

## 人形3
def FormationWindow_Figure3():
    pyautogui.click(random.randint(775,1000),random.randint(175,735))

## 人形4
def FormationWindow_Figure4():
    pyautogui.click(random.randint(1050,1285),random.randint(175,735))

# ## 人形5
# def FormationWindow_Figure5():
#     pyautogui.click(random.randint(218,470),random.randint(175,735))

## 显示种类
def FigureKindDisplay():
    pyautogui.click(random.randint(1645,1896),random.randint(350,500))

### 突击步枪
def AssuaultRifle():
    pyautogui.click(random.randint(800,1050),random.randint(675,785))

### 确认
def FigureKind_Confirm():
    pyautogui.click(random.randint(1200,1600),random.randint(985,1060))

## 人形栏1-1移出梯队
def FormationWindow_Remove():
    pyautogui.click(random.randint(25,255),random.randint(175,580))

## 人形栏1-2人形
def FormationWindow_12():
    pyautogui.click(random.randint(290,530),random.randint(175,580))

## 人形栏1-3人形
def FormationWindow_13():
    pyautogui.click(random.randint(559,800),random.randint(175,580))

## 人形栏1-4人形
def FormationWindow_14():
    pyautogui.click(random.randint(825,1065),random.randint(175,580))

## 人形栏1-5人形
def FormationWindow_15():
    pyautogui.click(random.randint(1090,1335),random.randint(175,580))

## 人形栏1-6人形
def FormationWindow_16():
    pyautogui.click(random.randint(1361,1600),random.randint(175,580))

## 人形栏2-1人形
def FormationWindow_21():
    pyautogui.click(random.randint(25,255),random.randint(630,1050))

## 人形栏2-2人形
def FormationWindow_22():
    pyautogui.click(random.randint(290,530),random.randint(630,1050))

## 人形栏2-3人形
def FormationWindow_23():
    pyautogui.click(random.randint(559,800),random.randint(630,1050))

## 人形栏2-4人形
def FormationWindow_24():
    pyautogui.click(random.randint(825,1065),random.randint(630,1050))

## 人形栏2-5人形
def FormationWindow_25():
    pyautogui.click(random.randint(1090,1335),random.randint(630,1050))

## 人形栏2-6人形
def FormationWindow_26():
    pyautogui.click(random.randint(1361,1600),random.randint(630,1050))

    