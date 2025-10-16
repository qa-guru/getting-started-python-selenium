import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, selector):
        return self.wait.until(EC.presence_of_element_located(selector))

    def is_not_find(self, selector):
        return self.wait.until_not(EC.presence_of_element_located(selector))

    def click(self, selector, force=False):
        if force:
            element = self.wait.until(EC.presence_of_element_located(selector))
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element = self.wait.until(EC.element_to_be_clickable(selector))
            element.click()

    def fill(self, selector, value):
        element = self.find(selector)
        element.send_keys(value)
