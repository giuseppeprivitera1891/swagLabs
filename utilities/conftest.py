import pytest


@pytest.fixture(scope="function")
def browser_context(playwright, browser_context_args):
    browser = playwright.chromium.launch(headless=False)
    context = browser_context_args(browser) # isolated browser context
    yield context
    context.close()
    browser.close()

pytest.fixture(scope="function")
def page(browser_context, base_url):
    page = browser = browser_context.new_page()
    page.goto(base_url)
    yield page
    page.close()
