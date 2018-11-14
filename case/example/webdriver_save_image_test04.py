"""
author:seamus
time:10/12/2018
function:learn the methods about mouse_click
version:v0.1
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# init
url = 'http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%8B%E6%9C%BA&oq=shouji&rsp=1'
xpath = '//ul/li/div/a/img'

# set profile
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', './yourfolder/')
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/jpeg')

# launch driver
driver = webdriver.Firefox(firefox_profile=fp)
driver.maximize_window()
driver.get(url)

for element in driver.find_elements_by_xpath(xpath):
	img_url = element.get_attribute('src')
	img_desc = element.get_attribute('data-desc')

	action = ActionChains(driver).move_to_element(element)
	action.context_click(element)
	action.send_keys(Keys.ARROW_DOWN)
	action.send_keys('v')
	action.perform()  # click save image

driver.close()

