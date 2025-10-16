import random
import time

import allure
import pytest
from selenium import webdriver

from demo_2.registration_page import User, RegistrationPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')
    yield driver

    driver.quit()


@pytest.fixture
def unique_user():
    unique_data =  str(int(time.time())) + str(random.randint(100, 999))
    user: User = User(unique_data)
    yield user

@pytest.fixture
def registration_page(driver):
    yield RegistrationPage(driver)


@allure.title('Registration user')
def test_register_page_object(registration_page, unique_user):
    registration_page.check_that_form_is_visible()

    registration_page.fill_account(unique_user)

    registration_page.check_that_form_is_not_visible()
    registration_page.check_that_success_form_is_visible()


@allure.title('[Negative] Registration user')
def test_register_page_object_negative(registration_page, unique_user):
    registration_page.check_that_form_is_visible()
    registration_page.click_on_continue()

    registration_page.check_that_form_is_visible()
    registration_page.check_that_error_is_visible()




# def test_register():
#     driver = webdriver.Chrome()
#     driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')
#
#     unique = str(int(time.time())) + str(random.randint(100, 999))
#
#     first_name = 'Test'
#     last_name = 'User'
#     email = f'test{unique}{unique}@gmail.com'
#     phone = '+111111111111'
#     password = 'Qwerty123!'
#
#     driver.find_element(By.ID, 'input-firstname').send_keys(first_name)
#     driver.find_element(By.ID, "input-lastname").send_keys(last_name)
#     driver.find_element(By.ID, "input-email").send_keys(email)
#     driver.find_element(By.ID, "input-telephone").send_keys(phone)
#     driver.find_element(By.ID, "input-password").send_keys(password)
#     driver.find_element(By.ID, "input-confirm").send_keys(password)
#
#     checkbox = driver.find_element(By.ID, "input-agree")
#     driver.execute_script("arguments[0].click();", checkbox)
#
#     driver.find_element(By.CSS_SELECTOR, '[value="Continue"]').click()
#
#     time.sleep(5)
#     assert driver.find_element(By.ID, 'content')
#     assert driver.find_element(By.XPATH, '//*[text()="Your Account Has Been Created!"]')
#
#     driver.quit()
