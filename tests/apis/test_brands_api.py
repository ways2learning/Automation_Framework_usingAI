import pytest
from apis.brands_api import BrandsAPI

@pytest.mark.api
def test_get_all_brands(api_client, config):
    brands = BrandsAPI(config.get_api_url(), api_client)
    response = brands.get_all_brands()
    assert response.status_code == 200
    assert "brands" in response.json()