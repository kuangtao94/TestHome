# from baiduHq import login
# driver = webdriver.Firefox(r"D:\Program Files\firefox.exe")
# driver.get("http://www.baidu.com")
# login(driver)
# driver.quit()

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.quit()

# def login():
#     print("WO shi login")