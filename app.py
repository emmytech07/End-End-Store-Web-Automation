from selenium import webdriver

from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver')
driver.fullscreen_window()
driver.get("http://www.rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
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
driver.find_element(By.CSS_SELECTOR, value="button[class='btn btn-success']").click()
driver.find_element(By.XPATH, value="//input[@id='country']").send_keys('ind')
wait =WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located(By.LINK_TEXT,"India"))
driver.find_element(By.LINK_TEXT, "India").click()
