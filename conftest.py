import pytest
from pytest_playwright.pytest_playwright import browser


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

