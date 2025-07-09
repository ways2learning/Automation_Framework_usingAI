import pytest
from apis.products_api import ProductsAPI

@pytest.mark.api
def test_get_all_products(api_client, config):
    products = ProductsAPI(config.get_api_url(), api_client)
    response = products.get_all_products()
    assert response.status_code == 200
    assert "products" in response.json()