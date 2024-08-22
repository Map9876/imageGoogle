import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
service = Service()
options.add_argument("webdriver.chrome.driver=/usr/local/bin/chromedriver")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service,  options=options)

# 打开网页
driver.get("https://www.google.com.hk/search?q=TV+%E3%82%A2%E3%83%8B%E3%83%A1++imagesize:{resolution}x1024+-eeo.today&tbm=isch&start={page*20}&sa=N&lite=0&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg")

# 等待网页加载
time.sleep(5)

# 获取cookie字符串
cookies = driver.get_cookies()

# 打印cookie字符串
print(f"Cookies: {cookies}")
# 关闭WebDriver
driver.quit()

#写入cookies到文件
# 打开一个文件，用于写入 cookies
with open('cookies.txt', 'w') as file:
    # 将 cookies 对象转换为字符串
    cookies_str = str(cookies)
    # 写入 cookies 字符串到文件
    file.write(cookies_str)

