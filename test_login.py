from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://sauce-demo.myshopify.com/")
driver.maximize_window()

driver.find_element(By.ID,"customer_login_link").click()
driver.find_element(By.ID,"customer_email").send_keys("mousin115@gmail.com")
driver.find_element(By.ID,"customer_password").send_keys("Mousin143@")
driver.find_element(By.CLASS_NAME,"button").click()

WebDriverWait(driver,10).until(EC.url_contains("/account"))

assert "/account" in driver.current_url

print("Login Successful")

driver.quit()