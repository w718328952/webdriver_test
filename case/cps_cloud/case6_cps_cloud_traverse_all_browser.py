"""
author:seamus
time:10/13/2018
function:equipment_init_config_test02
version:v0.1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# '''google浏览器下载配置'''
# options = webdriver.ChromeOptions()
# prefs = {'profile.default_content_settings.popups': 0,
# 		 'download.default_directory': 'C:\\Users\\seamus\\Downloads\\configure_data'}
# options.add_experimental_option('prefs', prefs)
# '''google浏览器启动配置'''
# driver = webdriver.Chrome(chrome_options=options)  # 配置浏览器参数时，必须定义配置对象options
#
#
# def main():
#
# 	driver.implicitly_wait(5)
# 	'''隐式等待和显示等待都存在时，超时时间取二者中较大的'''
# 	driver.maximize_window()
# 	driver.get(url="http://api.91mylover.top/")
# 	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-btn')))
#
# 	# 用例测试
# 	login_test()
# 	time.sleep(2)
# 	equ_config()
# 	time.sleep(2)
# 	driver.quit()


'''火狐浏览器下载配置'''
profile = webdriver.FirefoxProfile()
# 指定下载路径
profile.set_preference('browser.download.dir', 'C:\\Users\\seamus\\Downloads\\configure_data')
# 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
profile.set_preference('browser.download.folderList', 2)
# 在开始下载时是否显示下载管理器
profile.set_preference('browser.download.manager.showWhenStarting', False)
# 对所给出文件类型不再弹出框进行询问
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/ed')
# '''foxfire浏览器启动配置'''
driver = webdriver.Firefox(firefox_profile=profile)  # 配置浏览器参数时，必须定义配置对象profile

def main():
	driver.implicitly_wait(5)
	'''隐式等待和显示等待都存在时，超时时间取二者中较大的'''
	driver.maximize_window()
	driver.get(url="http://cpscloud.convenientpowersystems.com/")
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-btn')))
	# 用例测试
	login_test()
	time.sleep(2)
	equ_config()
	time.sleep(2)
	# driver.quit()


'''login_test'''
def login_test():

	driver.find_element_by_id("login-btn").click()
	time.sleep(2)
	driver.find_element_by_css_selector("#username").clear()
	driver.find_element_by_css_selector("#username").send_keys("bo_wen@echwireless.com")
	driver.find_element_by_css_selector("#password").clear()
	driver.find_element_by_css_selector("#password").send_keys("111111")
	driver.find_element_by_xpath("//*[@id='login-sub']").click()
	time.sleep(2)


def equ_config():

	driver.find_element_by_xpath('//*[@id="index-tab1"]/li[2]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="onlineTool"]/a').click()
	time.sleep(5)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[1]/div/div').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="step_two"]/li[3]').click()
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div/div[2]/button[2]').click()
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/div[2]/button[2]').click()
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[4]/div/div[2]/button').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="sure_opt"]').click()
	time.sleep(5)
	driver.find_element_by_xpath('//*[@id="downloadhex"]').click()
	time.sleep(2)

	WebDriverWait(driver, 10).until(EC.alert_is_present())
	'''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
	alert = driver.switch_to.alert
	print(alert.text)
	alert.dismiss()

	driver.refresh()


if __name__ == '__main__':
	main()