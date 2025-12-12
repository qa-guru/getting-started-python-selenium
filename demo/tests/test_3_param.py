import pytest


@pytest.mark.parametrize("url, title", [('https://habr.com/ru/feed/', "Публикации / Моя лента / Хабр"),
                                        ('https://www.selenium.dev/', "Selenium")])
def test_mobile_selenium(driver_mobile, url, title):
    driver_mobile.get(url)

    assert driver_mobile.title == title, f"Assertion error: Waiting title {title}, but got {driver_mobile.title}"
    assert driver_mobile.current_url == url, f"Assertion error: Waiting url {url}, but got {driver_mobile.current_url}"
