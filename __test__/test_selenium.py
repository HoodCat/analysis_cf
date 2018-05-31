import time
from selenium import webdriver

wd = webdriver.Chrome('C:/cafe24/python_util/webdriver/chromedriver.exe')
wd.get('http://www.cafe24.com')
time.sleep(10)

html = wd.page_source
print(html)

wd.quit()