from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Open the website
    driver.get("https://www.saucedemo.com/")

    # Step 2: Enter login credentials
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Step 3: Wait for the products page to load
    time.sleep(2)

    # Step 4: Verify login success by checking URL or page element
    if "inventory" in driver.current_url:
        print("Login successful.")
    else:
        print("Login failed.")
        driver.quit()
        exit()

    # Step 5: Verify the presence of "Sauce Labs Backpack"
    product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    if product.is_displayed():
        print("Product 'Sauce Labs Backpack' is present.")
    else:
        print("Product not found.")

finally:
    # Step 6: Close the browser
    time.sleep(2)
    driver.quit()
