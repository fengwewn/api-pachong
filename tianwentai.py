import requests
import json
#from twilio.rest import Client

# 获取香港天文台的天气警报接口地址和参数
url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php'
params = {'dataType': 'warnsum', 'lang': 'tc'}

# 发送请求并获取响应
response = requests.get(url, params=params)

# 解析响应中的 JSON 数据
weather_data = json.loads(response.text)

# 提取天气警报信息
# warning_message_name = weather_data['WTS']['name']
# warning_message_state = weather_data['WTS']['actionCode']
# warning_message_state = weather_data['WTS']['updateTime']
warning_message_name =null

for key1, value1 in weather_data.items():
    print(weather_data[key1]['name'])
    warning_message_name.append(weather_data['WTS']['name'])
    
    