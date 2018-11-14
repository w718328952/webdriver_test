"""
author:seamus
time:10/13/2018
function:equipment_init_config_test02
version:v0.1
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

'''测试次数'''
times = input('请输入测试次数：')

driver = webdriver.Chrome()
driver.maximize_window()


def main():

	driver.get(url="http://cpscloud.convenientpowersystems.com/")
	time.sleep(2)
	login_test()
	equ_config()
	driver.quit()


# login_test
def login_test():

	driver.find_element_by_id(id_="login-btn").click()
	time.sleep(2)
	driver.find_element_by_css_selector("#username").clear()
	driver.find_element_by_css_selector("#username").send_keys("bo_wen@echwireless.com")
	driver.find_element_by_css_selector("#password").clear()
	driver.find_element_by_css_selector("#password").send_keys("111111")
	driver.find_element_by_xpath("//*[@id='login-sub']").click()
	time.sleep(2)


def logout_test():

	# logout_test
	# 定位到指定元素
	above = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]")
	# 对定位到的元素执行悬停操作
	ActionChains(driver).move_to_element(above).perform()
	# # 注销
	# driver.find_element_by_xpath('//dd[@id="logout"]').click()  # 未实现


def equ_config():
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="index-tab1"]/li[2]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="onlineTool"]/a').click()

	for i in range(int(times)):
		time.sleep(5)
		driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[1]/div/div').click()
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="step_two"]/li[3]').click()
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div/div[2]/button[2]').click()
		time.sleep(5)
		driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/div[2]/button[2]').click()
		time.sleep(5)
		driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[4]/div/div[2]/button').click()
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="sure_opt"]').click()
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="downloadhex"]').click()
		time.sleep(5)
		print('第%i次测试：' % (i + 1))
		i += 1
		driver.refresh()




if __name__ == '__main__':
	main()