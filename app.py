from selenium import webdriver

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('./chromedriver')

driver.get("http://www.rahulshettyacademy.com/angularpractice/")
driver.fullscreen_window()
# //a[@href="/angularpractice/shop"] Xpath
# //a[text()="Shop"] Xpath
# a[href*="shop"] CSS selector
driver.find_element(By.XPATH, value='//a[text()="Shop"]').click()