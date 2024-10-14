import time
from os import times
from re import search

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


path = "/home/juli/E2E_UI/chromedriver"  # Replace with your actual path
chrome_options = Options()  # Create a ChromeOptions instance

# Set up the service with the specified path
service = Service(executable_path=path)

# Initialize the driver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.saucedemo.com")
print(driver.title)

time.sleep(1)

Search = driver.find_element(By.NAME, "user-name")
Search.send_keys("standard_user")

# time.sleep(1)

Search = driver.find_element(By.NAME, "password")
Search.send_keys("secret_sauce")

time.sleep(1)
# this is like press ENTER
# Search.send_keys(Keys.ENTER)

press_login = driver.find_element(By.NAME, "login-button")
press_login.click()

time.sleep(1)

press_item = driver.find_element(By.ID, "item_4_title_link")
press_item.click()
time.sleep(1)

press_add_to_cart = driver.find_element(By.ID, "add-to-cart")
press_add_to_cart.click()
# time.sleep(2)

press_shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
press_shopping_cart.click()
time.sleep(1)

if (driver.find_element(By.CLASS_NAME, "cart_item")):
    print('OK')
else:
    print("not ok")
time.sleep(1)

# push the button to make order
press_checkout = driver.find_element(By.ID, "checkout")
press_checkout.click()
time.sleep(1)


# Checkout: Your Information
Search_name = driver.find_element(By.ID, "first-name")
Search_name.send_keys("Ivan")

Search = driver.find_element(By.NAME, "lastName")
Search.send_keys("Ivanov")

Search = driver.find_element(By.NAME, "postalCode")
Search.send_keys("123456")

time.sleep(1)

# continue afterr fill info
press_continue = driver.find_element(By.ID, "continue")
press_continue.click()
time.sleep(1)

# Finish
press_continue = driver.find_element(By.ID, "finish")
press_continue.click()
time.sleep(1)