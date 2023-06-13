from selenium import webdriver

# 创建 Chrome 浏览器对象
driver = webdriver.Chrome()

# 打开网页
url = 'https://www.hko.gov.hk/tc/'
driver.get(url)

# 查找目标元素
p_elem = driver.find_element('xpath', '//*[@id="ps0"]/div/div/div/div[4]/div[1]/p')
msg =p_elem.text
# 打印元素
print(msg)

# 关闭浏览器
driver.quit()