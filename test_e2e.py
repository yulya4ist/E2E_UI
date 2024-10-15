import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

path = "/home/juli/E2E_UI/chromedriver"
chrome_options = Options()
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.saucedemo.com")
print(driver.title)

# time.sleep(1)

try:
    # авторизация
    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # выбор элемента на странице
    driver.find_element(By.ID, "item_4_title_link").click()

    # add to cart
    driver.find_element(By.ID, "add-to-cart").click()

    # go to cart
    driver.find_element(By.ID, "shopping_cart_container").click()

    # check item in cart
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert cart_item.text == "Sauce Labs Backpack", "No item in the cart"

    # push the button to make order
    driver.find_element(By.ID, "checkout").click()

    # Checkout: Your Information
    driver.find_element(By.ID, "first-name").send_keys("Ivan")
    driver.find_element(By.NAME, "lastName").send_keys("Ivanov")
    driver.find_element(By.NAME, "postalCode").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert confirmation_message == "Thank you for your order!", "ERROR"

    print('SUCCESS TEST')

except:
    print('ERROR')
    driver.quit()


