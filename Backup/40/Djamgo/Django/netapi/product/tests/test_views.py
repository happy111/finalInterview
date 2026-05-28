import pytest
from rest_framework.test import APIClient
from product.models import Category

client = APIClient()

@pytest.mark.django_db   #  Pytest creates a temporary test database
def test_list_categories():
    Category.objects.create(name="Home", description="Home items")
    Category.objects.create(name="Fashion", description="Clothes")

    response = client.get("/api/list/")
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_create_category():
    payload = {"name": "Sports", "description": "All sports items"}
    response = client.post("/category/create/", payload, format="json")

    assert response.status_code == 201
    assert response.data["name"] == "Sports"
