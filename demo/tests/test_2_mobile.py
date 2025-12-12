def test_mobile_selenium(driver_mobile):
    url = "https://habr.com/ru/feed/"
    driver_mobile.get(url)
    title = "Публикации / Моя лента / Хабр"

    assert driver_mobile.title == title, f"Assertion error: Waiting title {title}, but got {driver.title}"
    assert driver_mobile.current_url == url, f"Assertion error: Waiting url {url}, but got {driver.current_url}"
