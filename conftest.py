import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from typing import Generator

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        }
    }

@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(10000)
    yield page
    page.close()
