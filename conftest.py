import pytest
import random
import string
from selene import browser


@pytest.fixture(scope="session")
def maximized_browser():
    browser.driver.maximize_window()
    yield
    browser.quit()


@pytest.fixture
def duck_duck_go_page():
    browser.open("https://duckduckgo.com")


@pytest.fixture
def not_too_long_random_digits():
    return "".join(random.choices(string.digits, k=500))


@pytest.fixture
def too_long_random_digits():
    return "".join(random.choices(string.digits, k=1000))
