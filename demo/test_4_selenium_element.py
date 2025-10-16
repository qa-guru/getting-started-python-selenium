import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


@pytest.mark.python
def test_selenium_web(driver):
    driver.get("https://www.python.org/")

    wait = WebDriverWait(driver, 10)

    # Ждём поле поиска на главной
    search_input = wait.until(
        EC.visibility_of_element_located((By.ID, "id-search-field"))
    )
    search_input.clear()
    search_input.send_keys("selenium")

    # Явно ждём кнопку
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    search_button.click()

    # Ждём переход на страницу поиска (url и title)
    wait.until(EC.url_contains("/search/?q=selenium"))

    assert "search" in driver.current_url.lower()
