from selenium import webdriver
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
options.add_argument("webdriver.chrome.driver=/usr/local/bin/chromedriver")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service,  options=options)

driver.get("https://www.google.com")
print(f"ok")
driver.quit()
