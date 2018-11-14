from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class test1(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.baseurl = "http://www.xebest.com"

	#        self.driver.maximize_window()

	def dengLu(self):
		browser = self.driver

		browser.get(self.baseurl)

		browser.find_element_by_link_text(u"请登录").click()
		# 调用isElementExist方法，判断元素是否存在
		flag = test1.isElementExist(self, "div.popup-content")

		if flag:

			browser.find_element_by_id("userName").send_keys("w74581@163.com")
			browser.find_element_by_id("password").send_keys("w123456")
			browser.find_element_by_id("imgLogin").click()
			print(browser.switch_to_alert().text)
			browser.switch_to_alert().accept()


		else:
			print("没有弹框")

	#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
	def isElementExist(self, element):
		flag = True
		browser = self.driver
		try:
			browser.find_element_by_css_selector(element)
			return flag

		except:
			flag = False
			return flag


if __name__ == '__main__':
	unittest.main()
