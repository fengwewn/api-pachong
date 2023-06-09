import pyautogui
import pyperclip
import time
import requests
import json
# # 打开浏览器
# pyautogui.hotkey("win", "r")
# pyautogui.typewrite("chrome")
# pyautogui.press("enter")

# #pyautogui.press("f11")

# # 进入 WhatsApp 网页版
# time.sleep(3)
# pyautogui.typewrite("https://web.whatsapp.com")
# pyautogui.press("enter")

# # 等待用户扫描二维码登录
# time.sleep(5)

# # 查找联系人
# print("开始查找")
# pyautogui.click(252, 168)  # 点击搜索框
# #输入中文
# pyperclip.copy('测试小号')
# pyautogui.hotkey('Ctrl', 'V')
# #pyautogui.typewrite("123")  # 输入联系人名称
# time.sleep(2)
# pyautogui.click(374, 309)  # 选择联系人
def send(message):
    #pyautogui.click(873, 995)  # 点击输入框
    #splits = ['雷暴警告', '天文台在6月8日下午11時40分發出之雷暴警告，有效時間延長至今日正午12時，預料香港有局部地區雷暴。', '雷暴發生時，請採取以下預防措施：', '1. 如身處室外，請到安全地方躲避。', '2. 離開水面。切勿在戶外游泳或進行其他戶外水上運動。', '3. 切勿站立於高地或接近導電的物體、樹木或桅杆。']
    
    
    pyperclip.copy(message)  # 输入消息
    pyautogui.hotkey('Ctrl', 'V')
    pyautogui.press("enter")  # 发送消息

def get_w():
# 获取香港天文台的天气警报接口地址和参数
    url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php'
    #params = {'dataType': 'warnsum', 'lang': 'tc'}
    params = {'dataType': 'warningInfo', 'lang': 'tc'}
    # 发送请求并获取响应
    response = requests.get(url, params=params)

    # 解析响应中的 JSON 数据
    weather_data = json.loads(response.text)
    return weather_data

def show_time_sleep_load(num):
    num1 = num + 1
    i = 1
    for i in range(num1):
    # 输出当前时间，使用 \r 将光标移动到行首
    #current_time = time.strftime("%H:%M:%S", time.localtime())
    #print(f"\r{current_time}", end="")
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"\r{current_time}  {i}/{num} s", end="")
        time.sleep(1)
    print("\n")


#main


existing_contents = set()

print("开始运行")
print("请手动打开到WhatsApp页面")
show_time_sleep_load(10)

print("点击到需要发送的人/群组")
print("倒计时5秒开始启动")
show_time_sleep_load(5)

print("开始天气警报")
while True:
    print("获取api")
    weather_data = get_w()
    if weather_data != None:
        print("api获取完成")
        for item in weather_data['details']:
            contents = item['contents']
        # 对 contents 值进行操作，例如打印出来
            output_str = '\n'.join(contents)
            contents_hash = hash(output_str)
            if contents_hash not in existing_contents:
                existing_contents.add(contents_hash)
                print(output_str)
                send(output_str)
                time.sleep(2)
            #end if
        #end for
        print("等待60秒")
        show_time_sleep_load(60)
    
#end while
    



