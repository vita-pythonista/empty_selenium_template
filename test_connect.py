import time
from selenium.webdriver.common.by import By

from helpers.driver_app import Browser

driver = Browser()

driver.open("https://www.google.com")
driver.input(By.CSS_SELECTOR, "[name='q']", "python")
driver.click(By.CSS_SELECTOR, "[type='submit']")
time.sleep(2)
driver.close()