import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )

@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_input = request.config.getoption("browser_name")
    if browser_input == "chrome":
        service_obj = Service(r"D:\Automation_files\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)

    elif browser_input == "Edge":
        service_obj = Service(r"D:\Automation_files\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.implicitly_wait(4)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
















# @pytest.fixture(scope="class")
# def setup():
#     s = Service(r"D:\Automation_files\msedgedriver.exe")
#     # driver = webdriver.Chrome(service=s)
#     driver = webdriver.Edge(service=s)
#     print("I will be executing first")
#     driver.get("https://www.google.co.in/")
#     time.sleep(3)
#     yield
#     print("I will be executing last")
#     driver.close()
#     driver.quit()
#
# @pytest.fixture()
# def dataload():
#     print("Inputs needed for method")
#     return ["Rahul","gururam", "academy.com"]
#
# @pytest.fixture(params=["rahuk", "gururam", "academy.com"])
# def withparam(request):
#     return request.param

