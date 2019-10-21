from pyautogui import click
from random import randint

from general import Delay

# 战斗
def ChooseLevel(level):
    if level is 1:
        click(randint(675, 1090), randint(260, 446))
    elif level is 2:
        click(randint(1345, 1723), randint(362, 519))
    elif level is 3:
        click(randint(593, 977), randint(632, 812))
    elif level is 4:
        click(randint(1246, 1656), randint(722, 911))
    Delay(1, 2)
    ## 开始战斗
    click(randint(848, 1064), randint(817, 920))
    Delay(3, 4)