from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 确保您的ChromeDriver路径是正确的
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.google.com")
print(f"ok")
driver.quit()
