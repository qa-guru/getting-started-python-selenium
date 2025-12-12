import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_simple_selenium_web():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)

    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url

    driver.quit()
