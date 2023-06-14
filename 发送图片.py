import pyautogui
import pyperclip
import time
import requests
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import io
import win32clipboard
from PIL import Image

def send_img(img):
    send_to_clipboard(win32clipboard.CF_DIB
                      , jpg_to_bmp(img))
    send()

def jpg_to_bmp(jpg_image):
    bmp_image = io.BytesIO()
    jpg_image.save(bmp_image, format='BMP')
    bmp_data = bmp_image.getvalue()[14:]
    bmp_image.close()
    return bmp_data

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
def send(message=None):
    #pyautogui.click(873, 995)  # 点击输入框
    #splits = ['雷暴警告', '天文台在6月8日下午11時40分發出之雷暴警告，有效時間延長至今日正午12時，預料香港有局部地區雷暴。', '雷暴發生時，請採取以下預防措施：', '1. 如身處室外，請到安全地方躲避。', '2. 離開水面。切勿在戶外游泳或進行其他戶外水上運動。', '3. 切勿站立於高地或接近導電的物體、樹木或桅杆。']
    
    if message is not None:
        pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

image = Image.open('image.jpg')

send_img(image)