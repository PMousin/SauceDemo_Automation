from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://sauce-demo.myshopify.com/")
driver.maximize_window()

# LOGIN
wait.until(EC.element_to_be_clickable((By.ID,"customer_login_link"))).click()

wait.until(EC.presence_of_element_located((By.ID,"customer_email"))).send_keys("mousin115@gmail.com")
driver.find_element(By.ID,"customer_password").send_keys("Mousin143@")

wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"button"))).click()

print("Login Successful")

# HOME
driver.get("https://sauce-demo.myshopify.com/")

# OPEN PRODUCT
wait.until(
    EC.element_to_be_clickable((By.XPATH,"(//a[contains(@href,'/products')])[1]"))
).click()

# ADD TO CART
wait.until(
    EC.element_to_be_clickable((By.ID,"add"))
).click()

# CART
wait.until(
    EC.element_to_be_clickable((By.ID,"minicart"))
).click()

# CHECKOUT
wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME,"checkout"))
).click()

print("Checkout Started")

driver.quit()