from pyautogui import click
from random import randint

from general import Delay

# 编成
def ChooseEchelon(number):
    if number is 1:
        click(randint(0, 170), randint(165, 270))
    elif number is 2:
        click(randint(0, 170), randint(300, 400))
    Delay(1, 2)

# 人形
def ChooseFigure(number):
    if number is 1:
        click(randint(225, 465), randint(175, 735))
    elif number is 2:
        click(randint(500, 730), randint(175, 735))
    elif number is 3:
        click(randint(775, 1000), randint(175, 735))
    elif number is 4:
        click(randint(1050, 1285), randint(175, 735))
    elif number is 5:
        pass
    Delay(1, 2)

## 显示种类TODO
def FigureKindDisplay(kind):
    click(randint(1645, 1896), randint(350, 500))
    if kind is 'HG':
        click(randint(800, 1050), randint(540, 650))
    elif kind is 'SMG':
        click(randint(1073, 1318), randint(540, 650))
    elif kind is 'RF':
        click(randint(1345, 1585), randint(540, 650))
    elif kind is 'AR':
        click(randint(800, 1050), randint(675, 785))
    elif kind is 'MG':
        pass
    elif kind is 'SG':
        pass
    Delay(0, 1)
    # 确认
    click(randint(1200, 1600), randint(985, 1060))
    Delay(2, 3)

## 人形栏1-1移出梯队
def Remove():
    click(randint(25, 255), randint(175, 580))
    
# 人形栏
def Figure(row, number):
    if row is 1:
        if number is 2:
            click(randint(290, 530), randint(175, 580))
        elif number is 3:
            click(randint(559, 800), randint(175, 580))
        elif number is 4:
            click(randint(825, 1065), randint(175, 580))
        elif number is 5:
            click(randint(1090, 1335), randint(175, 580))
        elif number is 6:
            click(randint(1361, 1600), randint(175, 580))
    elif row is 2:
        if number is 1:
            click(randint(25, 255), randint(630, 1050))
        elif number is 2:
            click(randint(290, 530), randint(630, 1050))
        elif number is 3:
            click(randint(559, 800), randint(630, 1050))
        elif number is 4:
            click(randint(825, 1065), randint(630, 1050))
        elif number is 5:
            click(randint(1090, 1335), randint(630, 1050))
        elif number is 6:
            click(randint(1361, 1600), randint(630, 1050))
    Delay(1, 2)
