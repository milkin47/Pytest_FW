import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def setup_module():
    global driver
    s = Service("D:\Automation_files\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.google.co.in/")

def teardown_module():
    driver.close()
    driver.quit()

def test_verify1():
    assert "Google" in driver.title, "Title not matching"

def test_verify2():
    assert driver.current_url == "url"

