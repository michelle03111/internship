from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://app.jubelio.com/home/inventory')

username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')

username_input.send_keys('qa.rakamin.jubelio@gmail.com')
password_input.send_keys('Jubelio123!')


login_button = driver.find_element_by_xpath('//button[contains(text(), "Login")]')
login_button.click()

inventory_menu = driver.find_element_by_xpath('//a[contains(text(), "Inventory")]')
inventory_menu.click()

time.sleep(3)


edit_button = driver.find_element_by_xpath('//button[contains(text(), "Edit")]')
edit_button.click()




stock_input = driver.find_element_by_id('stock')
stock_input.clear()
stock_input.send_keys('100')  # Ubah menjadi jumlah stok yang diinginkan

# Simpan perubahan
save_button = driver.find_element_by_xpath('//button[contains(text(), "Save")]')
save_button.click()

# Tunggu hingga perubahan disimpan
time.sleep(3)

# Tutup browser dan akhiri sesi WebDriver
driver.quit()
