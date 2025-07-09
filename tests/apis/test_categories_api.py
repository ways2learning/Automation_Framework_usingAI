from apis.categories_api import CategoriesAPI

def test_get_all_categories():
    api = CategoriesAPI("https://automationexercise.com/api")
    response = api.get_all_categories()
    assert response.status_code == 200

    data = response.json()
    assert "categories" in data
    assert isinstance(data["categories"], list)
    assert len(data["categories"]) > 0

    # Optional: Validate structure
    for category in data["categories"]:
        assert "id" in category
        assert "category" in category
        assert "sub_category" in category
