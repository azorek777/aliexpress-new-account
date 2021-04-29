import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ali_log = input('Type your e-mail: ')
ali_pass = input('Type your password: ')

# Initiate the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

# Going to website
browser.get('https://www.aliexpress.com/')

# Checking if aliexpress suggest to use new user coupon
coupon = browser.find_elements_by_class_name('btn-close')
coupon_exist = len(coupon)
if coupon_exist > 0:
    browser.find_element_by_class_name('btn-close').click()
    time.sleep(2)
# Registry button
browser.find_element_by_class_name('user-account-port').click()
browser.find_element_by_class_name('join-btn').click()
time.sleep(2)
# Checking if aliexpress suggest to login by google
google = browser.find_elements_by_class_name('batman-channel-image')
logintype = len(google)
if logintype > 0:
    browser.find_element_by_css_selector('span.batman-channel-other').click()
# Registry by email
browser.find_element_by_class_name('fm-switch-action').click()
time.sleep(1)
# Registry
login = browser.find_element_by_xpath('//input[@placeholder="Email address"]')
login.send_keys(ali_log)
password = browser.find_element_by_xpath('//input[@placeholder="Password"]')
password.send_keys(ali_pass)
time.sleep(2)
browser.find_element_by_class_name('fm-button').click()
time.sleep(5)
# Checking success of registry
success = browser.find_elements_by_class_name('_4N5wQ')
success_check = len(success)
if success_check > 0:
    print('Account created successful')
# Countdown to exit
for time_left in range(5):
    print('Program will be closed in: ', 5 - time_left, 's')
    time.sleep(1)
browser.quit()
