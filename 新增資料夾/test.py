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
def send_img(img):
    send_to_clipboard(win32clipboard.CF_DIB, jpg_to_bmp(img))
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

def get_w():
# 获取香港天文台的天气警报接口地址和参数
    url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php'
    params = {'dataType': 'warnsum', 'lang': 'tc'}
    #params = {'dataType': 'warningInfo', 'lang': 'tc'}
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

#全局变量
existing_contents = set()
shure = False
leibaojg = Image.open('leibaojg.jpg')
kurejg = Image.open('kurejg.jpg')
# huangsebaoyu = Image.open('huangsebaoyu.jpg')

print("开始运行")
print("请手动打开到WhatsApp页面")
show_time_sleep_load(1)

print("点击到需要发送的人/群组")
print("倒计时3秒开始启动")
show_time_sleep_load(3)

print("开始天气警报")
while True:
    print("获取api")
    weather_data = get_w()
    driver = webdriver.Chrome()
    url = 'https://www.hko.gov.hk/tc/'
    driver.get(url)
    try:
        p_elem = driver.find_element('xpath', '//*[@id="ps0"]/div/div/div/div[4]/div[1]/p')
        #print('找到目标元素')
        msg =p_elem.text
    except NoSuchElementException:
        #print('未找到目标元素')
        msg = ''
    
    driver.quit()
    
    if weather_data != {}:
        print("api获取完成")
        # for item in weather_data['details']:
        #     contents = item['contents']
        for item in weather_data:
            #contents = item['contents']
            contents = weather_data[item]['name']
            contents += weather_data[item]['issueTime']
        # 对 contents 值进行操作，例如打印出来
            # output_str = '\n'.join(contents)
            # contents_hash = hash(output_str)
            contents_hash = hash(contents)
            if contents_hash not in existing_contents:
                existing_contents.add(contents_hash)
                warn_msg = weather_data[item]['name'] 
                if  weather_data[item]['actionCode'] ==  'CANCEL':
                    warn_msg += '现已取消'
                    if weather_data[item]['name'] =='雷暴警告':
                         warn_msg += '''，各分包請注意：\n檢查由於天雨影響而改變的路面狀況'''
                else:
                    warn_msg += '现已生效'
                    
                    if weather_data[item]['name'] =='酷热天气警告':
                        warn_msg += '''，各分包請注意：\n\n1. 在休息區為工友提供足夠的飲用水\n2. 為工友提供合適的散熱裝置\n3. 為工友安排適當的休息時間*\n\n*每工作2小時至少有15分鐘休息時間以減低熱衰竭或中暑的風險'''
                        send_img(kurejg)
                        time.sleep(2)
                        
                    elif weather_data[item]['name'] =='雷暴警告':
                        warn_msg += '''，各分包請注意：\n\n1. 部署排水措施\n2. 暫停室外高空作業\n3. 暫停電銲工作'''
                        send_img(leibaojg)
                        time.sleep(2)
                        
                    #endif
                #end if
                #print(output_str)
                print(warn_msg)
                send(warn_msg)
                time.sleep(2)
            #endif
        #end for
        #暑热警告
        if msg !='':
            if shure == False:           
                send(msg)
                send('''已生效，請注意防暑措施
                ''')
                print(msg)
                shure = True
        else:
            if shure == True:
                send("工作暑热警告取消")
                print("工作暑热警告取消")
                shure = False
        #end for
    else:
        print("api获取失败或者没有天气警告")
    print("等待60秒")
    show_time_sleep_load(60)
    
#end while
    



