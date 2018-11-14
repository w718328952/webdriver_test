"""
author:seamus
time:10/12/2018
function:learn the methods about mouse_click
version:v0.1
"""


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
# import pytesseract
# from PIL import Image


driver = webdriver.Chrome()
driver.get("https://yunpan.360.cn/file/index#/fileManage/my/file/%2F")
time.sleep(1)
driver.find_element_by_css_selector(".quc-input-account").clear()
driver.find_element_by_css_selector(".quc-input-account").send_keys("wb.2009@163.com")
driver.find_element_by_css_selector(".quc-input-password").clear()
driver.find_element_by_css_selector(".quc-input-password").send_keys("Wb918271.")
driver.find_element_by_xpath("//*[@id='login']/div/div[1]/form/p[5]/input").click()
time.sleep(2)

# 鼠标右击操作
right_click = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[3]/div[1]/div/div[2]/ul/li")
ActionChains(driver).context_click(right_click).perform()

# 鼠标悬浮操作
# 定位到指定元素
# above = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]")
# # 对定位到的元素执行悬停操作
# ActionChains(driver).move_to_element(above).perform()  # # 注销
# driver.find_element_by_xpath('//dd[@id="logout"]').click()  # 未实现

# # 屏蔽小广告
# js = 'document.getElementById("TANGRAM__22__wrapper").style.display="none";' #""中为小广告ID
# driver.execute_script(js)



# def image_read():
# 	image = Image.open('test.png')
# 	code = pytesseract.image_to_string(image)
# 	print(code)
