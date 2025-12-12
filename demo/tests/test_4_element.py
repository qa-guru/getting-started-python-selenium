import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.only
def test_python(driver):
    url = 'https://www.python.org/'
    driver.get(url)

    selector_search = '#id-search-field'

    wait = WebDriverWait(driver, 10)

    # Ждём поле поиска на главной
    search_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector_search))
    )

    search_input.send_keys("selenium")
    selector_submit = '.search-button'

    search_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector_submit))
    )
    search_button.click()

    search_url = '/search/?q=selenium'
    wait.until(EC.url_contains(search_url))

    title = "Welcome to Python.org"
    assert driver.title == title, f"Assertion error: Waiting title {title}, but got {driver.title}"
    assert search_url in driver.current_url, f"Assertion error: Waiting url {search_url}, but got {driver.current_url}"
