import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


@pytest.mark.parametrize(
    "url, title",
    [("https://www.selenium.dev/", "Selenium"), ("https://www.google.com/", "Google")],
)
def test_selenium_web(driver, url, title):
    driver.get(url)
    assert driver.title == title
    assert driver.current_url == url
