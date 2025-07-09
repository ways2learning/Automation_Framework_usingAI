import pytest
from apis.search_api import SearchAPI

@pytest.mark.api
def test_search_existing_product(api_client, config):
    search = SearchAPI(config.get_api_url(), api_client)
    response = search.search_product("tshirt")
    assert response.status_code == 200
    assert any("Tshirt" in p["name"] for p in response.json().get("products", []))