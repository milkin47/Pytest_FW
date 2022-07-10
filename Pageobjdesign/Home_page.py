from selenium.webdriver.common.by import By
from selenium import webdriver
#from checkout_page import checkOut_page
from Pageobjdesign.checkout_page import checkOut_page

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, " a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = checkOut_page(self.driver)
        return checkout
        #self.driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click()

