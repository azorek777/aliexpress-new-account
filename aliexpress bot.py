import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ali_log = input('Type your e-mail: ')
ali_pass = input('Type your password: ')

# Initiate the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

# Going to website
browser.get('https://www.aliexpress.com/')

# Switching-off new user coupon notify
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
# Registry
login = browser.find_element_by_xpath('//input[@placeholder="Email address"]')
login.send_keys(ali_log)
password = browser.find_element_by_xpath('//input[@placeholder="Password"]')
password.send_keys(ali_pass)
time.sleep(2)
browser.find_element_by_class_name('fm-button').click()
time.sleep(3)
