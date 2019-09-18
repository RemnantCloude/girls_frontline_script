import pyautogui
import time
import random # random.randint(0,9)

def Delay_24():
    time.sleep(random.uniform(2,4))
    
def Delay_46():
    time.sleep(random.uniform(4,6))

def ReturnToBase():
    pyautogui.click(random.randint(20,200),random.randint(20,135))

def Cancel():
    pyautogui.click(random.randint(20,200),random.randint(20,135))
