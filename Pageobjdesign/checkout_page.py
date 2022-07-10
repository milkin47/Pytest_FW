from selenium.webdriver.common.by import By
#from confirm_page import confirm_page
from Pageobjdesign.confirm_page import confirm_page

class checkOut_page():

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    productList = (By.XPATH, "//div/h4/a")
    button = (By.XPATH, "//div/button")
    Primary_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    success_button = (By.XPATH, "//button[@class='btn btn-success']")

    def getProducts(self):
        return self.driver.find_elements(*checkOut_page.products)

    def getProductlist(self):
        return self.driver.find_element(*checkOut_page.productList)

    def submitButton(self):
        return self.driver.find_element(*checkOut_page.button)

    def primaryButton(self):
        return self.driver.find_element(*checkOut_page.Primary_button)

    def successButton(self):
        self.driver.find_element(*checkOut_page.success_button).click()
        confirmPage = confirm_page(self.driver)
        return confirmPage