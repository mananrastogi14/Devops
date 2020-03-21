from selenium import webdriver

drive = webdriver.Chrome()
drive.get('https://www.facebook.com/')
pno = drive.find_element_by_xpath('//*[@id="email"]')
pno.send_keys('MananDemo')

pass = drive.find_element_by_xpath('//*[@id="pass"]')
pass.send_keys('devopsmidsed_21_d')

button = drive.find_element_by_xpath('//*[@id="u_0_b"]')
button.click()