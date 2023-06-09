import pyautogui
import pyperclip
import time

# 打开浏览器
pyautogui.hotkey("win", "r")
pyautogui.typewrite("chrome")
pyautogui.press("enter")

#pyautogui.press("f11")

# 进入 WhatsApp 网页版
time.sleep(3)
pyautogui.typewrite("https://web.whatsapp.com")
pyautogui.press("enter")

# 等待用户扫描二维码登录
time.sleep(5)

# 查找联系人
print("开始查找")
pyautogui.click(252, 168)  # 点击搜索框
#输入中文
pyperclip.copy('测试小号')
pyautogui.hotkey('Ctrl', 'V')
#pyautogui.typewrite("123")  # 输入联系人名称
time.sleep(2)
pyautogui.click(374, 309)  # 选择联系人

pyautogui.click(873, 995)  # 点击输入框
pyautogui.typewrite("message")  # 输入消息
pyautogui.press("enter")  # 发送消息
