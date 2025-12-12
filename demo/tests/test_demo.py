import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_simple_selenium():
    opts = Options()

    # opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1980,900")

    driver = webdriver.Chrome(options=opts)

    url = "https://www.selenium.dev/"

    driver.get(url)

    title = "Selenium"
    assert driver.title == title, f"Assertion error: Waiting title {title}, but got {driver.title}"
    assert driver.current_url == url, f"Assertion error: Waiting url {url}, but got {driver.current_url}"


    driver.quit()
