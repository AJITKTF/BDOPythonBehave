import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

from Utility import configreader


def before_scenario(context, driver):
    browser = configreader.read_config("basic_info", "browser")

    if browser.__eq__("Chrome"):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        context.driver = webdriver.Chrome(options=options)
    elif browser.__eq__("Firefox"):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        context.driver = webdriver.Firefox(options=options)
    elif browser.__eq__("Safari"):
        context.driver = webdriver.Safari()
    elif browser.__eq__("Edge"):
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        context.driver = webdriver.Edge(options=options)


    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    context.driver.get(configreader.read_config("basic_info", "url"))
    context.driver.implicitly_wait(5)

def after_scenario(context, driver):
    context.driver.quit()
   # time.sleep(25)

def after_step(context, steps):
    if steps.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),name="screenshot_failed",
                      attachment_type=AttachmentType.PNG)