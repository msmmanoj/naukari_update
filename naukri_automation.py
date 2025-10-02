from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

USERNAME = "malepatimanoj6@gmail.com"
PASSWORD = "Mtrgsm@123"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Go to Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")

    # 2. Wait for username field and enter credentials
    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "usernameField"))
    )
    username_field.clear()
    username_field.send_keys(USERNAME)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwordField"))
    )
    password_field.clear()
    password_field.send_keys(PASSWORD)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()

    # 3. Wait for profile/dashboard page to load (change condition as needed)
    # Here we just wait for the URL to change to something logged-in (update as needed)
    # WebDriverWait(driver, 20).until(
    #     EC.url_contains("naukri.com/mnjuser/")  # Adjust this if your landing URL is different!
    # )

    print("Login successful!")

    # 4. (Optional) Add more automation steps here...

except Exception as e:
    print("Error:", e)
    # Save debug files if workflow runner supports it
    driver.save_screenshot("error.png")
    with open("page_source.html", "w") as f:
        f.write(driver.page_source)

finally:
    driver.quit()
