import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def init_driver():
    print("-------Setup------")
    global driver
    s = Service("D:\Automation_files\msedgedriver.exe")
    #driver = webdriver.Chrome(service=s)
    driver = webdriver.Edge(service=s)
    driver.get("https://www.google.co.in/")

    yield
    print("--------teardown-----")
    driver.close()
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_verify3():
    assert "Google" in driver.title, "Title not matching"

@pytest.mark.usefixtures("init_driver")
def test_verify4():
    assert driver.current_url == "url"

