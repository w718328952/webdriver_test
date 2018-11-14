"""
author:seamus
time:10/13/2018
function:learn the methods about login_verification
version:v0.1
"""
from splinter import Browser


def log_in_doban(Name='', PassWrod=''):
	if Name and PassWrod:
		bs = Browser('chrome')
		bs.visit(url='http://www.douban.com/accounts/login?source=main')
		if bs.is_element_present_by_id(id='email'):
			bs.find_by_id(id='email').fill(Name)
			bs.find_by_id(id='password').fill(PassWrod)
			if bs.is_element_present_by_id(id='captcha_field'):
				# bs.find_by_id('captcha_field').fill(code_img)
				while True:
					val = bs.find_by_id(id='captcha_field').first.value
					if val and len(val) > 0:
						bs.find_by_id('captcha_field').fill(val)
						break
					pass
				pass
			bs.find_by_name('login').click()
			# print('log in')  # bs.quit()

if __name__ == '__main__':
	log_in_doban(Name='test_account', PassWrod='test_password')