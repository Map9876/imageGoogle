from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 确保您的ChromeDriver路径是正确的
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
print(f"ok")
driver.quit()
