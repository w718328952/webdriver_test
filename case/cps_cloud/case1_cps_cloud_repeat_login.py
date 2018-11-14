"""
author:seamus
time:10/13/2018
function:user_login_test01
version:v0.1
"""

from selenium import webdriver
import time

'''测试次数'''
times = input('请输入测试次数：')


def main():

	global driver
	for i in range(int(times)):

		# login_test
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get(url="http://cpscloud.convenientpowersystems.com/")
		driver.find_element_by_id(id_="login-btn").click()
		time.sleep(2)
		flag = isElementExist("#layui-layer1")

		#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
		if flag:
			driver.find_element_by_css_selector("#username").clear()
			driver.find_element_by_css_selector("#username").send_keys("bo_wen@echwireless.com")
			driver.find_element_by_css_selector("#password").clear()
			driver.find_element_by_css_selector("#password").send_keys("111111")
			driver.find_element_by_xpath("//*[@id='login-sub']").click()
			time.sleep(5)
			result = 'PASS'
		else:
			print("没有弹框")
			result = 'Fail'

		print('第%i次测试：'%(i+1), result)
		driver.quit()
		i += 1


def isElementExist(element):
	flag = True
	try:
		driver.find_element_by_css_selector(element)
		return flag
	except:
		flag = False
		return flag


if __name__ == '__main__':
	main()


