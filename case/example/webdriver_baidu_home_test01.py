"""
author:seamus
time:10/11/2018
function:learn the methods about HTML
version:v0.1
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# by*使用方法
# driver = webdriver.Chrome()
# driver.get(url="http://www.baidu.com")
# driver.find_element_by_id(id_="kw").send_keys("易冲无线")
# time.sleep(1)
# driver.find_element_by_name(name="wd").send_keys("官网")
# driver.find_element_by_id(id_="su").click()
# time.sleep(2)
# driver.find_element_by_name(name="wd").clear()
# driver.find_element_by_class_name("s_ipt").send_keys("CPS")
# driver.find_element_by_id(id_="su").click()
# time.sleep(1)
# driver.find_element_by_class_name("toindex").click()
# time.sleep(1)
# driver.find_element_by_tag_name("input ")#tag仅能定位到某一点input段落，无法定位到特定元素
# time.sleep(1)
# driver.find_element_by_link_text("新闻").click()
# time.sleep(1)
# driver.quit()

# driver = webdriver.Chrome()
# driver.get("http://www.mayi.com")
# driver.find_element_by_id(id_="loginshow").click()
# time.sleep(2)
# driver.quit()

# Xpath使用方法
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("易冲无线")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@type='submit' and @value='百度一下']").click()
# time.sleep(2)
# driver.quit()

# Css使用方法
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# # driver.find_element_by_css_selector(".s_ipt").send_keys("易冲无线")
# driver.find_element_by_css_selector("span.bg>input.s_ipt").send_keys("易冲无线")  # 不可包含空格
# time.sleep(1)
# driver.find_element_by_css_selector("#su").click()
# # driver.find_element_by_css_selector("span.btn_wr>input.btn").click()#未实现
# driver.set_window_size(1280, 800)
# driver.refresh()
# time.sleep(2)
# driver.quit()

# html常用接口
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_xpath("//*[@id='kw']").size
print(size)

# 返回百度主页顶部和底部文本信息
text = driver.find_element_by_xpath("//*[@id='u1']").text  # 使用什么浏览器，需生成对应浏览器的xpath
text1 = driver.find_element_by_id("cp").text
print(text)
print(text1)

# 返回元素的属性值，可以是ID\NAME\TYPE或其它任意值
attribute = driver.find_element_by_css_selector("#kw").get_attribute("type")
print(attribute)

# 返回元素的结果是否可见，返回结果为TRUE或FALSE
result = driver.find_element(By.ID, "kw").is_displayed()  # By使用时需从selenium中引用对应方法才可使用
print(result)

driver.quit()
