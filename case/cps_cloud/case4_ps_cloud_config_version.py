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
import time
import random

'''测试参数配置'''
times = input('请输入测试次数：')
version_list = ['0.5', '1.0', '1.2', '2.0', '2.5', '3.0']



'''google浏览器下载配置'''
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
		 'download.default_directory': 'C:\\Users\\seamus\\Downloads\\configure_data'}
options.add_experimental_option('prefs', prefs)
'''google浏览器启动配置'''
driver = webdriver.Chrome(chrome_options=options)  # 配置浏览器参数时，必须定义配置对象options


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
	driver.quit()


def version_config():
	version_num = random.sample(version_list, 1)
	version = " ".join(version_num)
	return version


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

	for i in range(int(times)):

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
		version_init = driver.find_element_by_id('input_id3').get_attribute('value')
		print(version_init)
		driver.find_element_by_id(id_='input_id3').clear()
		time.sleep(1)
		driver.find_element_by_id(id_='input_id3').send_keys(version_config())

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

		time.sleep(2)
		driver.refresh()

		'''验证配置信息'''
		# 下一步
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="platform_info"]')))
		'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[1]/div/div/button').click()

		# 下一步
		WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step_two"]')))
		'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="step_two"]/li[3]').click()
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[2]/div/div[2]/button[2]').click()

		# 下一步
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/div[2]/button[2]').click()

		# 设置完毕
		time.sleep(2)
		version_set = driver.find_element_by_id('input_id3').get_attribute('value')
		print(version_set)
		driver.refresh()

		if version_init == version_set:
			print('第%i次测试：初始值与设定值一致，请确认配置信息是否与初始信息一致！'%(i+1))
		else:
			print('第%i次测试：版本信息已更新为：'%(i+1), version_set)
		i += 1

if __name__ == '__main__':
	main()