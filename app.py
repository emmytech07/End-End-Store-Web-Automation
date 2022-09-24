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
products = driver.find_elements(by='xpath', value='//div[@class="card h-100"]')
for product in products:
# //div[@class="card h-100"]/div/h4/a for X path
    productName = product.find_element(By.XPATH, value='./div/h4/a').text
    # print(productName)
    if productName== 'iphone X':
        product.find_element(By.XPATH, value='./div/button').click()
    # price = product.find_element(By.XPATH, value='./div/h5').text
    # print(price)
    # content = product.find_element(By.XPATH, value='./div/p').text
    # print(content)
driver.find_element(By.XPATH, value="//a[@class='nav-link btn btn-primary']").click()
