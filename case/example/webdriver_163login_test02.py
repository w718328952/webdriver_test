"""
author:seamus
time:10/12/2018
function:learn the methods about login_email
version:v0.1
"""

from selenium import webdriver
import time

driver = webdriver.Chrome
driver.get(url="http://www.baidu.com")
driver.find_element_by_id(id_="kw").send_keys("163邮箱登录")
time.sleep(1)
driver.find_element_by_id(id_="su").click()
time.sleep(1)
driver.find_element_by_css_selector("#op_email3_username").clear()
driver.find_element_by_css_selector("#op_email3_username").send_keys("wb.2009")
driver.find_element_by_css_selector(".op_email3_password").clear()
driver.find_element_by_css_selector(".op_email3_password").send_keys("918272wenbo.")
driver.find_element_by_xpath("//*[@id='1']/div[1]/div/form/table/tbody/tr[3]/td[2]/a[1]").click()
time.sleep(2)
driver.quit()


