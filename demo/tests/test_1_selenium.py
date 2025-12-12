def test_fixture_selenium(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    title = "Selenium"

    assert driver.title == title, f"Assertion error: Waiting title {title}, but got {driver.title}"
    assert driver.current_url == url, f"Assertion error: Waiting url {url}, but got {driver.current_url}"
