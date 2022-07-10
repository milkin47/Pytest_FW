from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class confirm_page():

    def __init__(self, driver):
        self.driver = driver

    input = (By.ID, "country")
    wait = (By.LINK_TEXT, "India")
    India = (By.LINK_TEXT,"India")
    checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR,"[type='submit']")
    success_msg = (By.CLASS_NAME,"alert-success")

    def input_ind(self):
        return self.driver.find_element(*confirm_page.input).send_keys("ind")

    def wait_10(self):
        return self.driver.find_element(*confirm_page.India)

    def final_checkout(self):
        self.driver.find_element(*confirm_page.checkbox).click()
        self.driver.find_element(*confirm_page.submit).click()
        return self.driver.find_element(*confirm_page.success_msg).text