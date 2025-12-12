import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    opts = Options()
    # opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1980,1600")
    web_driver = webdriver.Chrome(options=opts)
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def driver_mobile():
    opts = Options()
    # opts.add_argument("--headless=new")
    opts.add_argument(
        "--user-agent=Mozilla/5.0 (Linux; Android 14; Pixel 8) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Mobile Safari/537.36"
    )
    opts.add_argument("--window-size=412,915")
    web_driver = webdriver.Chrome(options=opts)
    yield web_driver
    web_driver.quit()

