import pytest
from pages.home_page import HomePage

@pytest.mark.web
def test_homepage_logo_visibility(page,config):
    home = HomePage(page)
    home.navigate(config.get_base_url())
    assert home.is_logo_visible()

@pytest.mark.web
def test_click_products_redirects_to_products(page,config):
    home = HomePage(page)
    home.navigate(config.get_base_url())
    home.click_products()
    assert "products" in page.url