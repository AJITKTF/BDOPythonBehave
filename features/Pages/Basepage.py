import time
from encodings.punycode import selective_find

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage(object):
    def __init__(self, driver):
        self.driver = driver


    def finding_element(self, locator_type, locator_value):
        element = None
        if locator_type == 'xpath':
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type == 'id':
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type == 'name':
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_type == 'class':
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        return element

    def click_element(self, locator_type, locator_value):
        element = self.finding_element(locator_type, locator_value)
        self.wait_method()
        element.click()

    def send_text(self, locator_type, locator_value, user_text):
        element = self.finding_element(locator_type, locator_value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(user_text)

    def display_element(self, locator_type, locator_value):
        element = self.finding_element(locator_type, locator_value)
        return element.is_displayed()

    def wait_method(self):
        time.sleep(2)

    def scroll_to_view(self,locator_type, locator_value):
        element = self.finding_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def select_element(self, locator_type, locator_value):
        element = self.finding_element(locator_type, locator_value)
        dropdown_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(element))
        dropdown_option.click()

    def wait_until_element(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((locator_type, locator_value)))

    def getvalue_element(self, locator_type, locator_value, text_value):
        element = self.finding_element(locator_type, locator_value)
        data1 = element.text.__contains__(text_value)
        return data1





