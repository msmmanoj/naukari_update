from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

# Read credentials from environment variables (for GitHub Actions secrets)
USERNAME = 'malepatimanoj6@gmail.com'
PASSWORD = 'Mtrgsm@123'

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless for CI/CD
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)  # Let page load

    # Find username and password fields and submit
    driver.find_element(By.ID, "usernameField").send_keys(USERNAME)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)  # Wait for login to complete, adjust as needed

    # Optionally, navigate to profile and update
    # Example: driver.get("https://www.naukri.com/mnjuser/profile")
    # Do further actions...

    print("Login completed successfully!")
finally:
    driver.quit()
