import pyautogui
import time
import random

# 主界面
## 捷径栏
def MainWindow_Shortcut():
    pyautogui.click(random.randint(0,60),random.randint(483,590))

## 修理
def MainWindow_Restore():
   pyautogui.click(random.randint(1230,1536),random.randint(267,425))

## 研发
def MainWindow_Research():
    pyautogui.click(random.randint(1230,1536),random.randint(458,617))

## 战斗
def MainWindow_Combat():
    pyautogui.click(random.randint(1230,1536),random.randint(650,851))

## 3D宿舍
def MainWindow_3DDormitory():
    pyautogui.click(random.randint(1580,1723),random.randint(244,400))

## 宿舍
def MainWindow_Dormitory():
    pyautogui.click(random.randint(1701,1885),random.randint(244,400))

## 工厂
def MainWindow_Factory():
    pyautogui.click(random.randint(1580,1885),random.randint(435,590))

## 编成
def MainWindow_Formation():
    pyautogui.click(random.randint(1580,1885),random.randint(624,622))