from selenium import webdriver

drive = webdriver.Chrome()
drive.get('https://www.facebook.com/')
fname= drive.find_element_by_xpath('//*[@id="u_0_m"]')
fname.send_keys('MananDemo')

lname= drive.find_element_by_xpath('//*[@id="u_0_o"]')
lname.send_keys('Demo')

phno= drive.find_element_by_xpath('//*[@id="u_0_r"]')
phno.send_keys('000000000000')

pass = drive.find_element_by_xpath('//*[@id="u_0_w"]')
pass.send_keys('devopsmidsed_21_d')

button = drive.find_element_by_xpath('//*[@id="u_0_13"]')
button.click()