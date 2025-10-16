import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument(
        "--user-agent=Mozilla/5.0 (Linux; Android 14; Pixel 8) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Mobile Safari/537.36"
    )
    opts.add_argument("--window-size=412,915")

    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_chrome_mobile_view(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google"
