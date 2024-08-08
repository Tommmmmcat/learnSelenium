import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.google.com')
time.sleep(2)
# 搜素假面骑士的信息
search_input = browser.find_element(By.ID, 'APjFqb')
search_input.send_keys('假面骑士')
search_input.send_keys(Keys.RETURN)

# 点击图片的tag
time.sleep(2)
browser.find_element(By.XPATH, value='//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]').click()



time.sleep(20)

browser.quit()