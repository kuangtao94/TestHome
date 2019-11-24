#coding:utf-8
from selenium import webdriver
from time import sleep
import time

#谷歌
#无痕浏览器
option = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings_popups":0,
         "download.default_directory":"D:\\xiazai\\"}
option.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=option)


#火狐
# profile = webdriver.ChromeProfile()
# profile.set_preference("browser.download.dir","d:\\xiazai\\")
# profile.set_preference("browser.download.folderList",2)
# profile.set_preference("browser.download.manager.showWhenStarting","False")
# profile.set_preference("browser,helperApps.neverAsk.saveToDisk","application/vnd.ms-excel")
# driver = webdriver.Firefox(firefox_profile=profile)



driver.get('http://192.168.0.111/crm/index.php?m=user&a=login')
driver.find_element_by_name('name').send_keys('fu')
driver.find_element_by_name('password').send_keys('fu123')
driver.find_element_by_name('submit').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a').click()           #点击线索
sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div/div/button').click()          #点击
sleep(1)
driver.find_element_by_xpath('//*[@id="excelExport"]').click()                                  #点击导出线索
sleep(1)
driver.switch_to_alert().accept()