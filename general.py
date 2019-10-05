from pyautogui import click
from time import sleep
from random import randint
from random import uniform

def Delay(x, y):
    sleep(uniform(x, y))

def ReturnToBase():
    click(randint(20, 200), randint(20, 135))
    Delay(3, 4)

def Cancel():
    click(randint(20, 200), randint(20, 135))
    Delay(1, 2)
