import pytest
from playwright.sync_api import sync_playwright
import requests
from utils.config_reader import ConfigReader

# Load config once per session
@pytest.fixture(scope="session")
def config():
    return ConfigReader()

# Create API session client
@pytest.fixture(scope="function")
def api_client():
    session = requests.Session()
    yield session
    session.close()

def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed mode (default is headless)"
    )

# Create Playwright browser context with resolution from config
@pytest.fixture(scope="function")
def browser_context(config, pytestconfig):
    with sync_playwright() as p:
        headed = pytestconfig.getoption("headed")
        browser = p.chromium.launch(headless=True)
        width, height = config.env_config['resolutions'][0]
        context = browser.new_context(
            viewport={"width": width, "height": height}
        )
        yield context
        context.close()
        browser.close()

# Provide a page from the context
@pytest.fixture()
def page(browser_context):
    return browser_context.new_page()