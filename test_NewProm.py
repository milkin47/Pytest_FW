import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

@pytest.mark.major
def test_google():
    s = Service("D:\Automation_files\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.google.co.in/")
    assert driver.title == "Google", "Title is not matching"
    driver.close()
    driver.quit()

@pytest.mark.major
def test_facebook():
    s = Service("D:\Automation_files\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.facebook.com/")
    title = driver.title
    assert "Facebook" in title, "Title is not matching"
    driver.close()
    driver.quit()

def test_insta():
    s = Service("D:\Automation_files\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.instagram.com/?hl=en")
    assert "Instagram" in driver.title, "Title is not matching"
    driver.close()
    driver.quit()

def test_twitter():
    s = Service("D:\Automation_files\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://twitter.com/login")
    assert "Twitter" in driver.title, "Title is not matching"
    driver.close()
    driver.quit()

def test_redbus():
    s = Service("D:\Automation_files\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.redbus.in/")
    assert "Bus" in driver.title, "Title is not matching"
    driver.close()
    driver.quit()
