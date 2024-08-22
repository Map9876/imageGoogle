from selenium import webdriver

# webdriver.Chrome?

browser = webdriver.Chrome()#executable_path = '/opt/anaconda3/bin/chromedriver')
browser.get("http://music.163.com") 
#print(browser.page_source)
print('i am fine!')
browser.close() 
