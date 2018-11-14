from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep # time。sleep()实现延时

# 火狐浏览器专用文件配置方法
profile = webdriver.FirefoxProfile()
# 指定下载路径
profile.set_preference('browser.download.dir', 'd:\\')
# 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
profile.set_preference('browser.download.folderList', 2)
# 在开始下载时是否显示下载管理器
profile.set_preference('browser.download.manager.showWhenStarting', False)
# 对所给出文件类型不再弹出框进行询问
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

browser = webdriver.Firefox(firefox_profile=profile)  # 配置浏览器时，必须定义配置对象profile

browser.get('http://www.xxxxxxx.com')  # 这里地址用的是查询页面，如果没有登录就会跳转到登录页面，登录之后会自动跳到查询页面
# assert 'Yahoo!' in browser  这行不要了

username = browser.find_element_by_name('uid')  # 获取username输入框
username.clear()  # 先清空输入框
username.send_keys(username)  # 输入用户名

password = browser.find_element_by_name('password')  # 获取username输入框
password.clear()  # 先清空输入框
password.send_keys(password)  # 输入密码
password.send_keys(Keys.RETURN)  # 输入密码之后输入RETURN特殊键实现登录，不用再定位登录按钮
browser.implicitly_wait(5)  # 延时5秒等待页面跳转
browser.find_element_by_name('项目').send_keys(ID)  # 定位到项目ID输入框并输入项目ID
browser.find_element_by_id('search').click()  # 定位到搜索按钮，并点击
browser.implicitly_wait(5)  # 延时等待搜索结果
browser.find_element_by_xpath('\\').click()  # 定位到导出按钮，并点击
sleep(3)  # 延时 弹出导出提示框，提示用户到另外一个页面下载导出数据
browser.find_element_by_xpath('\\').click()
# 定位到弹出框上的确定按钮，点击确定隐藏提示框，以方便导出下一个项目的bug列表
browser.get('http://www.yyyyyy.com')  # 跳转到下载页面
filelist = browser.find_elements_by_xpath('\\')  # 定位到文件列表中所有的文件
for file in filelist:
	file.click()  # 点击保存文件