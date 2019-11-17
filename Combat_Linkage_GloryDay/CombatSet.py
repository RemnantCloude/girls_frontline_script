from pyautogui import click
from random import randint

from general import Delay

# 战斗
def ChooseLevel(level):
    if level is 1:
        click(randint(600, 1000), randint(520, 722))
    elif level is 2:
        click(randint(1345, 1770), randint(290, 500))
    elif level is 3:
        click(randint(1200, 1600), randint(690, 880))
    Delay(1, 2)
    ## 开始战斗
    click(randint(848, 1064), randint(817, 920))
    Delay(3, 4)