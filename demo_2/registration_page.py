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

class User:
    def __init__(self, unique):
        self.first_name = 'Test'
        self.last_name = 'User'
        self.email = f'test{unique}{unique}@gmail.com'
        self.phone = '+111111111111'
        self.password = 'Qwerty123!'

class RegistrationPage(BasePage):

    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    POLICY = (By.ID, "input-agree")
    CONTINUE = (By.CSS_SELECTOR, '[value="Continue"]')

    CONTENT = (By.ID, 'content')
    TEXT_ACCOUNT_CREATED = (By.XPATH, '//*[text()="Your Account Has Been Created!"]')

    TEXT_ERROR_FIRST_NAME = (By.XPATH, '//*[text()="First Name must be between 1 and 32 characters!"]')
    ALERT_ERROR = (By.CSS_SELECTOR, '.alert-danger')

    @allure.step('Click on "Continue"')
    def click_on_continue(self):
        self.click(self.CONTINUE)

    @allure.step('Fill all fields on the page "Registration"')
    def fill_account(self, user: User):
        self.fill(self.FIRST_NAME, user.first_name)
        self.fill(self.LAST_NAME, user.last_name)
        self.fill(self.EMAIL, user.email)
        self.fill(self.PHONE, user.phone)
        self.fill(self.PASSWORD, user.password)
        self.fill(self.CONFIRM_PASSWORD, user.password)

        self.click(self.POLICY, True)
        self.click_on_continue()

    @allure.step('Assert that form "Registration" is visible')
    def check_that_form_is_visible(self):
        assert self.find(self.FIRST_NAME)
        assert self.find(self.LAST_NAME)
        assert self.find(self.EMAIL)
        assert self.find(self.PHONE)
        assert self.find(self.PASSWORD)
        assert self.find(self.CONFIRM_PASSWORD)

        assert self.find(self.POLICY)
        assert self.find(self.CONTINUE)

    @allure.step('Assert that form "Registration" is NOT visible')
    def check_that_form_is_not_visible(self):
        assert self.is_not_find(self.FIRST_NAME)
        assert self.is_not_find(self.LAST_NAME)
        assert self.is_not_find(self.EMAIL)
        assert self.is_not_find(self.PHONE)
        assert self.is_not_find(self.PASSWORD)
        assert self.is_not_find(self.CONFIRM_PASSWORD)

        assert self.is_not_find(self.POLICY)
        assert self.is_not_find(self.CONTINUE)

    @allure.step('Assert that account created')
    def check_that_success_form_is_visible(self):
        assert self.find(self.CONTENT)
        assert self.find(self.TEXT_ACCOUNT_CREATED)

    @allure.step('Assert that text "Your Account Has Been Created!" is not visible')
    def check_that_success_form_is_not_visible(self):
        assert self.is_not_find(self.CONTENT)
        assert self.is_not_find(self.TEXT_ACCOUNT_CREATED)

    @allure.step('Assert that errors is visible')
    def check_that_error_is_visible(self):
        assert self.find(self.TEXT_ERROR_FIRST_NAME)
        assert self.find(self.ALERT_ERROR)

