import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

def test_register_user():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://automationexercise.com")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body")))

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.fc-dialog-overlay")))
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.fc-dialog-overlay")))
        except:
            pass

        signup_login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup / Login')]")))
        try:
            signup_login_btn.click()
        except:
            driver.execute_script("arguments[0].click();", signup_login_btn)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'New User Signup!')]")))
        driver.find_element(By.NAME, "name").send_keys("TestUser")

        email = f"testuser{int(time.time())}@example.com"
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)

        driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()

        driver.save_screenshot("after_signup_click.png")

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Enter Account Information')]")))
        except TimeoutException:
            error = driver.find_element(By.CSS_SELECTOR, "p[class='error']")
            print("Signup failed with error:", error.text)
            driver.quit()
            assert False, f"Signup failed: {error.text}"

        driver.find_element(By.ID, "id_gender1").click()
        driver.find_element(By.ID, "password").send_keys("TestPass123")
        Select(driver.find_element(By.ID, "days")).select_by_value("10")
        Select(driver.find_element(By.ID, "months")).select_by_value("5")
        Select(driver.find_element(By.ID, "years")).select_by_value("1990")
        driver.find_element(By.ID, "newsletter").click()
        driver.find_element(By.ID, "optin").click()
        driver.find_element(By.ID, "first_name").send_keys("Test")
        driver.find_element(By.ID, "last_name").send_keys("User")
        driver.find_element(By.ID, "company").send_keys("TestCompany")
        driver.find_element(By.ID, "address1").send_keys("123 Test Street")
        driver.find_element(By.ID, "address2").send_keys("Suite 456")
        Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")
        driver.find_element(By.ID, "state").send_keys("TestState")
        driver.find_element(By.ID, "city").send_keys("TestCity")
        driver.find_element(By.ID, "zipcode").send_keys("12345")
        driver.find_element(By.ID, "mobile_number").send_keys("1234567890")
        driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Account Created!')]")))
        driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
        driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Account Deleted!')]")))
        driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
    finally:
        driver.quit()

