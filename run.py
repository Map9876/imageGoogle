from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://www.google.com")
driver.quit()

print('i am fine!')
driver.close() 
