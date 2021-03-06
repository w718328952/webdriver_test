"""
author:seamus
time:10/16/2018
function:compare_profiles_test03
version:v0.1
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
import difflib
import os
import time


'''google浏览器下载配置'''
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
		 'download.default_directory': 'C:\\Users\\seamus\\Downloads\\configure_data'}
options.add_experimental_option('prefs', prefs)
'''google浏览器启动配置'''
driver = webdriver.Chrome(chrome_options=options)  # 配置浏览器参数时，必须定义配置对象options


global file_name1, file_name2


def main():

	driver.implicitly_wait(5)
	'''隐式等待和显示等待都存在时，超时时间取二者中较大的'''
	driver.maximize_window()
	driver.get(url="http://cpscloud.convenientpowersystems.com/")
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-btn')))

	# 用例测试
	login_test()
	time.sleep(2)
	file1, file2 = equ_config()
	time.sleep(2)
	compare(file1, file2)
	driver.quit()


#  '''火狐浏览器下载配置'''
# 	profile = webdriver.FirefoxProfile()
# 	# 指定下载路径
# 	profile.set_preference('browser.download.dir', 'C:\\Users\\seamus\\Downloads\\configure_data')
# 	# 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
# 	profile.set_preference('browser.download.folderList', 2)
# 	# 在开始下载时是否显示下载管理器
# 	profile.set_preference('browser.download.manager.showWhenStarting', False)
# 	# 对所给出文件类型不再弹出框进行询问
# 	profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/ed')
# 	# '''foxfire浏览器启动配置'''
# 	driver = webdriver.Chrome(firefox_profile=profile)  # 配置浏览器参数时，必须定义配置对象profile

# def main():
# 	driver.implicitly_wait(5)
# 	'''隐式等待和显示等待都存在时，超时时间取二者中较大的'''
# 	driver.maximize_window()
# 	driver.get(url="http://api.91mylover.top/")
# 	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-btn')))
# 	# 用例测试
# 	login_test()
# 	time.sleep(2)
# 	equ_config()
# 	time.sleep(2)
# 	# driver.quit()

'''login_test'''
def login_test():

	driver.find_element_by_id(id_="login-btn").click()

	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'layui-layer1')))
	'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''

	driver.find_element_by_css_selector("#username").clear()
	driver.find_element_by_css_selector("#username").send_keys("bo_wen@echwireless.com")
	driver.find_element_by_css_selector("#password").clear()
	driver.find_element_by_css_selector("#password").send_keys("111111")
	driver.find_element_by_xpath("//*[@id='login-sub']").click()

	WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.CLASS_NAME, value='layui-nav')))
	'''判断元素是否可见，如果可见就返回这个元素'''


def logout_test():

	# logout_test
	# 定位到指定元素
	above = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]")
	# 对定位到的元素执行悬停操作
	ActionChains(driver).move_to_element(above).perform()
	# # 注销
	# driver.find_element_by_xpath('//dd[@id="logout"]').click()  # 未实现


def equ_config():
	# 技术支持工具
	driver.find_element_by_xpath('//*[@id="index-tab1"]/li[2]').click()

	# 在线配置入口
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'onlineTool')))
	'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="onlineTool"]/a').click()

	# 下一步
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="platform_info"]')))
	'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
	time.sleep(5)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[1]/div/div/button').click()

	# 下一步
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step_two"]')))
	'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
	time.sleep(5)
	driver.find_element_by_xpath('//*[@id="step_two"]/li[3]').click()
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div/div[2]/button[2]').click()

	# 下一步
	WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[3]/div/div[2]/button[2]')))
	'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/div[2]/button[2]').click()

	# 更改配置信息
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'leftMsg_3')))
	'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
	time.sleep(1)
	driver.find_element_by_id(id_='input_id3').clear()
	time.sleep(1)
	driver.find_element_by_id(id_='input_id3').send_keys('3.0')

	# 设置完毕
	WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[4]/div/div[2]/button')))
	'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[4]/div/div[2]/button').click()

	# 确定
	WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.XPATH, '//*[@id="sure_opt"]')))
	'''判断某个元素中是否可见并且是enable的，代表可点击'''
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="sure_opt"]').click()

	# 下载配置文件
	WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.ID, 'downloadhex')))
	'''判断某个元素中是否可见并且是enable的，代表可点击'''
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="downloadhex"]').click()
	time.sleep(1)
	name1 = driver.find_element_by_id(id_='hidden_download').get_attribute('download')
	file_name1 = name1.replace('/', '_')
	print(file_name1)
	time.sleep(2)
	driver.refresh()

	'''验证配置信息'''
	# 下一步
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[1]/div/div/button').click()

	# 下一步
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="step_two"]/li[3]').click()
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div/div[2]/button[2]').click()

	# 下一步
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/div[2]/button[2]').click()

	# 设置完毕
	time.sleep(5)
	driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[4]/div/div[2]/button').click()

	# 确定
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="sure_opt"]').click()

	# 下载配置文件
	time.sleep(5)
	driver.find_element_by_xpath('//*[@id="downloadhex"]').click()
	time.sleep(1)
	name2 = driver.find_element_by_id(id_='hidden_download').get_attribute('download')
	file_name2 = name2.replace('/', '_')
	print(file_name2)
	time.sleep(2)

	return file_name1, file_name2


def compare(file1, file2):
	"""子主函数"""
	try:
		f1 = 'C:\\Users\\seamus\\Downloads\\configure_data\\' + file1
		f2 = 'C:\\Users\\seamus\\Downloads\\configure_data\\' + file2
	except  Exception as e:
		print("Error: " + str(e))
		print("Usage : python compareFile.py filename1 filename2")
		sys.exit()

	if f1 == "" or f2 == "":  # 参数不够
		print("Usage : python compareFile.py filename1 filename2")
		sys.exit()

	tf1 = readFile(f1)
	tf2 = readFile(f2)

	d = difflib.HtmlDiff()  # 创建一个实例difflib.HtmlDiff
	writeFile(d.make_file(tf1, tf2))  # 生成一个比较后的报告文件，格式为html


def readFile(filename):
	"""读取文件，并处理"""
	try:
		fileHandle = open(filename, "r")
		text = fileHandle.read().splitlines()
		fileHandle.close()
		return text
	except IOError as e:
		print("Read file error: " + str(e))
		sys.exit()


def writeFile(file):
	"""写入文件"""
	diffFile = open('data\\diff_{}_.html'.format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())), "w")
	diffFile.write("<meta charset='UTF-8'>")
	diffFile.write(file)
	print("The file on {}".format(os.path.abspath(str(diffFile.name))))  # 提示文件生成在什么地方
	diffFile.close()


if __name__ == '__main__':
	main()