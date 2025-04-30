from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Chrome()
#mendapatkan halaman utama
driver.get("https://app.hive.com/join")

time.sleep(10)

#masukkan semua isian pada halaman
sign_up= driver.find_element(By.XPATH, '//*[@id="mounter-react-root"]/div/div/div/div/div[2]/div/div/div/button').click()

work_email = driver.find_element(By.XPATH, '//*[@id="email"]')
work_email.send_keys('deyrenathaniel@gmail.com')

#continue_email= driver.find_element(By.ID, 'mounter-react-root').click()
wait = WebDriverWait(driver, 15)
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//form//button[contains(text(), "Continue")]')))
continue_button.click()


first_name = driver.find_element(By.XPATH, '//*[@id="firstName"]')
first_name.send_keys('deyren')

last_name = driver.find_element(By.XPATH, '//*[@id="lastName"]')
last_name.send_keys('nathaniel')

phone_number = driver.find_element(By.XPATH, '//*[@id="phone"]')
phone_number.send_keys('082313457568')

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('123456')

#next = driver.find_element(By.XPATH, '//*[@id="mounter-react-root"]/div/div/div/div/div[3]/div/div/form/button').click()


time.sleep(15)
driver.quit