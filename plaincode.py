import pytest
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utility.baseclass import Base_class
from Pageobjdesign.Home_page import HomePage
from Pageobjdesign.checkout_page import checkOut_page
from Pageobjdesign.confirm_page import confirm_page

class Testtrial(Base_class):
    def test_endtoend(self):
        homePage = HomePage(self.driver)
        checkout = homePage.shopItems()
        products = checkout.getProducts()
        for product in products :
            productName = checkout.getProductlist().text
            if productName == "Blackberry":
                checkout.submitButton().click()
        checkout.primaryButton().click()            #self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        confirmpage = checkout.successButton()           #self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        confirmpage.input_ind()        #self.driver.find_element(By.ID,"country").send_keys("ind")
        self.verfylinkpresence("India")
        confirmpage.wait_10().click()   # wait = WebDriverWait(self.driver,10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
           #self.driver.find_element(By.LINK_TEXT,"India").click()
           #self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
          #self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        successText = confirmpage.final_checkout()
        assert "Success! Thank you!" in successText




















