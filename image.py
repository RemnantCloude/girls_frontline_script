# vscode检测不到cv2模块，通过这种添加方式消除报错
from cv2 import cv2
from PIL import ImageGrab
import numpy

# 截图并转换格式
def capture_screen():
    screenshot = ImageGrab.grab().convert('RGB')
    screenshot = numpy.array(screenshot)
    return cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

# 模板匹配
def match(small_pic_path, large_pic):
    small_pic = cv2.imread(small_pic_path)
    small_pic = cv2.cvtColor(small_pic, cv2.COLOR_BGR2GRAY)
    small_pic = cv2.Canny(small_pic, 50, 200)

    large_pic = cv2.cvtColor(large_pic, cv2.COLOR_BGR2GRAY)
    large_pic = cv2.Canny(large_pic, 50, 200)
    
    result = cv2.matchTemplate(large_pic, small_pic, cv2.TM_CCOEFF)
    _, max, _, max_location = cv2.minMaxLoc(result)
    return (max,max_location)