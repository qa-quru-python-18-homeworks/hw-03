from selene import browser, be, have


def test_successful_search(duck_duck_go_page):
    browser.element('//input[@aria-label="Search with DuckDuckGo"]').should(
        be.blank
    ).type("Python").press_enter()
    browser.element("html").should(have.text("Python.org"))


def test_empty_search_results(
    not_too_long_random_digits
):
    browser.element('//input[@aria-label="Search with DuckDuckGo"]').should(
        be.blank
    ).type(not_too_long_random_digits).press_enter()
    browser.element("html").should(have.text("No results found"))


def test_too_long_search(duck_duck_go_page, too_long_random_digits):
    browser.element('//input[@aria-label="Search with DuckDuckGo"]').should(
        be.blank
    ).type(too_long_random_digits).press_enter()
    browser.element("html").should(
        have.text("Search query entered was too long. Please shorten and try again")
    )
