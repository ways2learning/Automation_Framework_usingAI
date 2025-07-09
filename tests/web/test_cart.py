import pytest
from pages.cart_page import CartPage

@pytest.mark.web
def test_cart_page_title(page, config):
    cart = CartPage(page)
    cart.navigate(config.get_base_url() + "/view_cart")
    assert "Checkout" in cart.get_title()

@pytest.mark.web
def test_cart_empty_message(page, config):
    cart = CartPage(page)
    cart.navigate(config.get_base_url() + "/view_cart")
    assert cart.is_cart_empty_text_present()